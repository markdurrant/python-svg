#!/usr/bin/env python3

from random import *

from paper import Paper
from pen import Pen
from path import Path
from point import Point


fuscia = Pen(weight = 0.5, color = "#f09")
cyan = Pen(weight = 0.75, color = "#09f")
black = Pen(weight = 0.25)

paper = Paper(pens = [cyan, black], width = 105, height = 73)

def drawGuide(p1, p2): 
  return Path(points = [p1, p2]).setPen(fuscia)

def drawDash(p, length):
  dash = Path(points = [
    Point(p.x, p.y + length / 2),
    Point(p.x, p.y - length / 2)
  ]).rotate(random() * 360)
  
  return dash

squareSize = 34
square = Path(points = [
  Point(paper.center.x + squareSize / 2, paper.center.y + squareSize / 2),
  Point(paper.center.x + squareSize / 2, paper.center.y - squareSize / 2),
  Point(paper.center.x - squareSize / 2, paper.center.y - squareSize / 2),
  Point(paper.center.x - squareSize / 2, paper.center.y + squareSize / 2)
], closed = True)

spotlight = Point(
  paper.center.x + random() * squareSize - squareSize / 2,
  paper.center.y + random() * squareSize - squareSize / 2
)

for i in range(1, 600):
  dashPoint = Point(
    paper.center.x + random() * squareSize - squareSize / 2,
    paper.center.y + random() * squareSize - squareSize / 2
  )

  if i % 2 == 0:
    dashPen = black
  else:
    dashPen = black 

  drawDash(dashPoint, 2.5 - abs(dashPoint.distanceTo(spotlight)) / 8).setPen(dashPen)

# black.saveGcode("dashes.nc")
paper.save("dashes.svg")
