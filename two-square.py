#!/usr/bin/env python3

from random import random

from paper import Paper
from pen import Pen
from path import Path
from point import Point

fuscia = Pen(weight = 0.5, color = "#f09")
cyan = Pen(weight = 0.5, color = "#09f")
black = Pen(weight = 0.5)

paper = Paper(pens = [black], width = 105, height = 73)

def getSquare(p, size):
  square = Path(points = [
    Point(p.x + size / 2, p.y + size / 2),
    Point(p.x + size / 2, p.y - size / 2),
    Point(p.x - size / 2, p.y - size / 2),
    Point(p.x - size / 2, p.y + size / 2)
  ], closed = True)

  return square

def randomise(path, distance):
  for p in path.points:
    p.moveVector(360 * random(), distance * random())


bigSize = 38
smallSize = random() * 8 + 4

bigSquare = getSquare(paper.center, bigSize).setPen(cyan)
smallSquare = getSquare(Point(
  paper.center.x + bigSize * random() - bigSize / 2,
  paper.center.y + bigSize * random() - bigSize / 2),
smallSize).setPen(cyan)


randomise(bigSquare, 4)
randomise(smallSquare, 2)


guideA = Path(points = [bigSquare.points[0], smallSquare.points[0]]).setPen(fuscia)
guideB = Path(points = [bigSquare.points[1], smallSquare.points[1]]).setPen(fuscia)
guideC = Path(points = [bigSquare.points[2], smallSquare.points[2]]).setPen(fuscia)
guideD = Path(points = [bigSquare.points[3], smallSquare.points[3]]).setPen(fuscia)

numLines = 14

for l in range(numLines + 1):
  Path(points = [
    guideA.pointAtDistance((guideA.length() / numLines) * l),
    guideB.pointAtDistance((guideB.length() / numLines) * l),
    guideC.pointAtDistance((guideC.length() / numLines) * l),
    guideD.pointAtDistance((guideD.length() / numLines) * l)
  ], closed = True).setPen(black)

paper.save("two-square.svg")