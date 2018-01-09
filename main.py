#!/usr/bin/env python3

from random import *

from paper import Paper
from pen import Pen
from path import Path
from point import Point


fuscia = Pen(weight = 1, color = "#f09")
cyan = Pen(weight = 1, color = "#09f")
black = Pen(weight = 1)

paper = Paper(pens = [cyan, fuscia, black], width = 105, height = 148)

paper.log()


squareSize = 40
square = Path(points = [
  Point(paper.center.x + squareSize / 2, paper.center.y + squareSize / 2),
  Point(paper.center.x + squareSize / 2, paper.center.y - squareSize / 2),
  Point(paper.center.x - squareSize / 2, paper.center.y - squareSize / 2),
  Point(paper.center.x - squareSize / 2, paper.center.y + squareSize / 2)
], closed = True)

guideTop = Point(square.right + squareSize * random(), square.bottom)
guideBottom = Point(square.right + squareSize * random(), square.topCenter.y - uniform(8, 20))

guide = Path(points = [guideTop, guideBottom])

numLines = 34

for o in range(1, numLines - 1):
  offset = o * (square.bottom - square.top) / (numLines - 1)

  Path(points = [
    Point(square.bottomLeft.x, square.bottomLeft.y - offset),
    guide.pointAtDistance(guide.length() / (numLines - 1) * o),
    Point(square.bottomRight.x, square.bottomRight.y - offset),
  ]).setPen(black)

Path(points = [
  square.topLeft,
  square.bottomLeft,
  square.bottomRight,
  square.topRight,
  guide.points[1]
], closed = True).setPen(black)

paper.save("test.svg")
