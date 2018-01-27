#!/usr/bin/env python3

from random import *

from paper import Paper
from pen import Pen
from path import Path
from point import Point


fuscia = Pen(weight = 0.25, color = "#f09")
cyan = Pen(weight = 0.25, color = "#0ff")
black = Pen(weight = 0.5)

paper = Paper(pens = [cyan, black], width = 105, height = 73)

def drawGuide(p1, p2): 
  return Path(points = [p1, p2]).setPen(fuscia)

def drawDash(p1, p2):
  return Path(points = [p1, p2]).setPen(black)

def dashAlongLine(line, g):
  l = line.length()
  d = 0
  i = 0

  while d <= l - 10:
    if i % 2 == 0:
      ld = random() * g * 3 + 1

      drawDash(
        Point(line.pointAtDistance(d).x + random() / 4 - 0.25, line.pointAtDistance(d).y + random() / 4 - 0.25),
        line.pointAtDistance(d + ld)
      )
      d += ld
    else:
      d += random() * g + 1

    print(l, d)
    i += 1

squareSize = 34
square = Path(points = [
  Point(paper.center.x + squareSize / 2, paper.center.y + squareSize / 2),
  Point(paper.center.x + squareSize / 2, paper.center.y - squareSize / 2),
  Point(paper.center.x - squareSize / 2, paper.center.y - squareSize / 2),
  Point(paper.center.x - squareSize / 2, paper.center.y + squareSize / 2)
], closed = True).setPen(cyan)

numLines = 40

for i in range(numLines):
  guideA = drawGuide(
    Point(square.bottomLeft.x - squareSize / (numLines - 1) * i, square.bottomLeft.y),
    Point(square.topLeft.x - squareSize / (numLines - 1) * i, square.topLeft.y)
  )
  guideA.points[1].move(random() / 2 - 0.25, random() -0.5 - 10)
  guideA.points[0].move(random() / 2 - 0.25, random() * - 2 + 1)

  dashAlongLine(guideA, i / (random() * 8 + 6))

black.setBox()
black.rotate(randint(0, 4) * 90, paper.center)

black.saveGcode("dashes.nc")
paper.save("dashes.svg")
