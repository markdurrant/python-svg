#!/usr/bin/env python3

from random import *

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

square = getSquare(paper.center, 36).setPen(cyan)
randomise(square, 7)

guideA = Path(points = [square.points[0], square.points[1]]).setPen(fuscia)
guideB = Path(points = [square.points[3], square.points[2]]).setPen(fuscia)

numLines = 80

pointList = []

for l in range(numLines + 1):
  if l % 2 == 0:
    pointList.append(guideA.pointAtDistance(guideA.length() / numLines * l))
    pointList.append(guideB.pointAtDistance(guideB.length() / numLines * l))
  else: 
    pointList.append(guideB.pointAtDistance(guideB.length() / numLines * l))
    pointList.append(guideA.pointAtDistance(guideB.length() / numLines * l))

snake = Path(points = pointList).setPen(black)

snake.rotate(randint(0, 3) * 90)

black.saveGcode("snake.nc")
paper.save("snake.svg")