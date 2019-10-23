import pygame as pg
import random
import sys


화면크기 = (400, 400)
칸 = 20
FPS = 10
위 = (-1, 0)
왼쪽 = (0, -1)
오른쪽 = (0, 1)
아래 = (1, 0)
pg.init()
화면 = pg.display.set_mode(화면크기)
도화지 = pg.Surface(화면.get_size())
도화지.fill((255,255,255))
시계 = pg.time.Clock()

def 네모_그리기(표면, 좌표, 색깔):
  새_좌표 = (좌표[1]*칸, 좌표[0]*칸)
  사각형 = pg.Rect(새_좌표, (칸, 칸))
  pg.draw.rect(표면, 색깔, 사각형)


class Apple():
    def __init__(self):
      self.새로만들기()
    def 새로만들기(self):
      self.위치 = (random.randrange(0, 화면크기[0]/칸), \
        random.randrange(0, 화면크기[1]/칸))
    def 옮기기(self, 좌표):
      self.위치 = 좌표
    def 그리기(self):
        네모_그리기(도화지, self.위치, (255,0,0))


class Snake():
    def __init__(self, 머리색깔=(0,0,0), 몸색깔=(100,100,100)):
        self.몸 = []
        self.머리 = (화면크기[0]/칸/2, 화면크기[0]/칸/2)
        self.몸색깔 = 몸색깔
        self.머리색깔 = 머리색깔
        self.방향 = 위
        pass

    def 움직이기(self):
        새_머리 = (self.머리[0]+self.방향[0], self.머리[1]+self.방향[1])
        # 몸을 머리에 집어 넣는다
        self.몸.insert(0, self.머리)
        # 몸 마지막(꼬리)를 자른다
        global 사과
        if 새_머리 == 사과.위치:
          while True:
            사과.새로만들기()
            if 사과.위치 in self.몸:
              continue
            if 사과.위치 == self.머리:
              continue
            break

        else:
          self.몸.pop()
        # 새로운 머리를 만들어준다.
        self.머리 = 새_머리

    def 살아있나(self):
        # 칸 크기를 넘지 않았을 때
        if self.머리[0] > 화면크기[0]/칸 or self.머리[1] > 화면크기[1]/칸:
            return False
        if self.머리[0] < 0 or self.머리[1] < 0:
            return False
        # 지 꼬리에 닿았을 때
        if self.머리 in self.몸:
          return False
        return True

    def 그리기(self):
        global 도화지
        네모_그리기(도화지, self.머리, self.머리색깔)
        for 요소 in self.몸:
          네모_그리기(도화지, 요소, self.몸색깔)

    def 머리돌리기(self, 방향):
        self.방향 = 방향

사과 = Apple()
뱀 = Snake()
사과.그리기()
뱀.그리기()

while True:
  events = pg.event.get()
  if events:
    for event in events:
      if event.type == pg.QUIT:
        sys.exit(0)
      if event.type == pg.KEYDOWN:
        if event.key == pg.K_UP:
          뱀.머리돌리기(위)
        elif event.key == pg.K_DOWN:
          뱀.머리돌리기(아래)
        elif event.key == pg.K_LEFT:
          뱀.머리돌리기(왼쪽)
        elif event.key == pg.K_RIGHT:
          뱀.머리돌리기(오른쪽)

  뱀.움직이기()
  화면.fill((255,255,255))
  도화지.fill((255,255,255))

  뱀.그리기()
  if not 뱀.살아있나():
      sys.exit(0)
  사과.그리기()
  화면.blit(도화지, (0,0))
  pg.display.flip()
  시계.tick(FPS)