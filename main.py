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

pointE = Point(square.right + squareSize * random(), square.topCenter.y - uniform(2, 6))
pointF = Point(square.right + squareSize * random(), square.bottom + uniform(2, 6))


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


# guideTop = Point(square.right + squareSize * random(), square.bottom)
# guideBottom = Point(square.right + squareSize * random(), square.topCenter.y - uniform(8, 20))

# guide = Path(points = [guideTop, guideBottom])

# numLines = 34

# for o in range(1, numLines - 1):
#   offset = o * (square.bottom - square.top) / (numLines - 1)

#   Path(points = [
#     Point(square.bottomLeft.x, square.bottomLeft.y - offset),
#     guide.pointAtDistance(guide.length() / (numLines - 1) * o),
#     Point(square.bottomRight.x, square.bottomRight.y - offset),
#   ]).setPen(black)

# Path(points = [
#   square.topLeft,
#   square.bottomLeft,
#   square.bottomRight,
#   square.topRight,
#   guide.points[1]
# ], closed = True).setPen(black)

paper.save("test.svg")
