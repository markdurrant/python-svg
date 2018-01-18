#!/usr/bin/env python3

from random import *

from paper import Paper
from pen import Pen
from path import Path
from point import Point


fuscia = Pen(weight = 0.5, color = "#f09")
cyan = Pen(weight = 0.5, color = "#09f")
black = Pen(weight = 0.25)

paper = Paper(pens = [black, cyan, fuscia], width = 148, height = 105)

def drawDot(p):
  size = 0.5

  p1 = Point(p.x, p.y)
  p2 = Point(p.x, p.y)
  p3 = Point(p.x, p.y)

  p1.moveVector(0, size)
  p2.moveVector(120, size)
  p3.moveVector(240, size)

  return Path(points = [
    p1, 
    p2,
    p3
  ], closed = True).setPen(fuscia)

squareSize = 50
square = Path(points = [
  Point(paper.center.x + squareSize / 2, paper.center.y + squareSize / 2),
  Point(paper.center.x + squareSize / 2, paper.center.y - squareSize / 2),
  Point(paper.center.x - squareSize / 2, paper.center.y - squareSize / 2),
  Point(paper.center.x - squareSize / 2, paper.center.y + squareSize / 2)
], closed = True)

divisions = 24

pointList = []

for r in range(divisions):
  for c in range(divisions):
    p = Point(
          square.right + c * squareSize / (divisions - 1),
          square.top + r * squareSize / (divisions - 1)
        )

    pointList.append(p)


spotLight = Point(square.right + squareSize * random(), square.top + squareSize * random())
spotLight2 = Point(square.right + squareSize * random(), square.top + squareSize * random())
spotLight3 = Point(square.right + squareSize * random(), square.top + squareSize * random())

# drawDot(spotLight)

for p in pointList:
  d = p.distanceTo(spotLight)
  a = p.angleTo(spotLight)

  m = (40 - d) / 6 

  if m > d:
    m = d

  p.moveVector(a, m)
  
for p in pointList:
  d = p.distanceTo(spotLight2)
  a = p.angleTo(spotLight2)

  m = (40 - d) / 6 

  if m > d:
    m = d

  p.moveVector(a, m)

for p in pointList:
  d = p.distanceTo(spotLight3)
  a = p.angleTo(spotLight3)

  m = (40 - d) / 6 

  if m > d:
    m = d

  p.moveVector(a, m)
  p.moveVector(random() * 360, 0.1)

for i in range(divisions):
  rowList = []
  colList = []
  
  for p in range(divisions):
    rowList.append(pointList[i * divisions + p])  
    colList.append(pointList[i + p * divisions])  

  Path(rowList).setPen(black)
  Path(colList).setPen(black)


paper.save('grid.svg')