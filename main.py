#!/usr/bin/env python3

from random import *

from paper import Paper
from pen import Pen
from path import Path
from point import Point


fuscia = Pen(weight = 0.5, color = "#f09")
cyan = Pen(weight = 0.25, color = "#09f")
black = Pen(weight = 2.5)

paper = Paper(pens = [black], width = 105, height = 148)

def drawGuide(p1, p2): 
  return Path(points = [p1, p2]).setPen(fuscia)


squareSize = 60
square = Path(points = [
  Point(paper.center.x + squareSize / 2, paper.center.y + squareSize / 2),
  Point(paper.center.x + squareSize / 2, paper.center.y - squareSize / 2),
  Point(paper.center.x - squareSize / 2, paper.center.y - squareSize / 2),
  Point(paper.center.x - squareSize / 2, paper.center.y + squareSize / 2)
], closed = True).setPen(cyan)

pointA = Point(square.topLeft.x, square.topLeft.y + uniform(4, 16))
pointB = square.bottomLeft.clone()
pointC = square.bottomRight.clone()
pointD = Point(square.topRight.x, square.topRight.y + uniform(4, 16))

pointE = Point(square.right + squareSize * random(), square.topCenter.y - uniform(2, 8))
pointF = Point(square.right + squareSize * random(), square.bottom + uniform(1, 4))


guideX = drawGuide(pointA, pointB)
guideY = drawGuide(pointE, pointF)
guideZ = drawGuide(pointD, pointC)

numLines = 16
numLines = numLines - 1

for l in range(1, numLines):
  offset = l * (square.bottom - square.top) / numLines

  Path(points = [
    guideX.pointAtDistance(guideX.length() / numLines * l),
    guideY.pointAtDistance(guideY.length() / numLines * l),
    guideZ.pointAtDistance(guideZ.length() / numLines * l),
  ]).setPen(black)

Path(points = [pointA, pointB, pointF, pointC, pointD, pointE], closed = True).setPen(black)

black.saveGcode("test.nc")
paper.save("test.svg")
