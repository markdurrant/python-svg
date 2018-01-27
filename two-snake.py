#!/usr/bin/env python3

from random import *

from paper import Paper
from pen import Pen
from path import Path
from point import Point

fuscia = Pen(weight = 0.5, color = "#f09")
cyan = Pen(weight = 0.5, color = "#09f")
black = Pen(weight = 0.35)

paper = Paper(pens = [cyan, fuscia, black], width = 105, height = 73)

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

def drawDot(p):
  pList = []
  
  for i in range(5):
    point = p.clone()
    point.moveVector(360 / 5 * i, 0.25)
    pList.append(point)

  Path(points = pList, closed = True).setPen(fuscia)
    

square = getSquare(paper.center, 36)
randomise(square, 3)

gapSize = 0.5

pointA = square.points[2]
pointB = square.points[1]
pointF = square.points[0]
pointG = square.points[3]

guideAB = Path(points = [pointA, pointB])
guideGF = Path(points = [pointG, pointF])
guideBF = Path(points = [pointB, pointF])
guideAG = Path(points = [pointA, pointG])

positionBF = gapSize + (guideBF.length() - gapSize * 2) * random()
positionAG = gapSize + (guideBF.length() - gapSize * 2) * random()

pointC = guideBF.pointAtDistance(positionBF - gapSize)
pointD = guideBF.pointAtDistance(positionBF)
pointE = guideBF.pointAtDistance(positionBF + gapSize)

pointH = guideAG.pointAtDistance(positionAG + gapSize)
pointI = guideAG.pointAtDistance(positionAG)
pointJ = guideAG.pointAtDistance(positionAG - gapSize)

guideJC = Path(points = [pointJ, pointC])
guideHE = Path(points = [pointH, pointE])

def snake(guide1, guide2):
  numLines = 70
  pointList = []

  for l in range(numLines + 1):
    if l % 2 == 0:
      pointList.append(guide1.pointAtDistance(guide1.length() / numLines * l))
      pointList.append(guide2.pointAtDistance(guide2.length() / numLines * l))
    else: 
      pointList.append(guide2.pointAtDistance(guide2.length() / numLines * l))
      pointList.append(guide1.pointAtDistance(guide2.length() / numLines * l))

  return Path(points = pointList).setPen(black)

snakeA = snake(guideAB, guideJC)
snakeB = snake(guideGF, guideHE)

black.setBox()
black.rotate(randint(0, 1) * 90, paper.center)

paper.save("two-snake.svg")