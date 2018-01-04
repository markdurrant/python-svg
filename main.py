#!/usr/bin/env python3

from paper import Paper
from pen import Pen
from path import Path
from point import Point

myDrawing = Paper(width = 400, height = 400)

size = 100
center = { 'x': myDrawing.width / 2, 'y': myDrawing.height / 2}

myX = center['x']
myY = center['y']

myDrawing.pens = [Pen(
  paths = [Path(
    points = [
      Point(myX + size, myY + size),
      Point(myX + size, myY - size),
      Point(myX - size, myY - size),
      Point(myX - size, myY + size)
    ],
    closed = True
  )],
  weight = 10
)]

myPath = myDrawing.pens[0].paths[0]

myPath.rotate(45)

def movePoint(point):
  direction = myPath.center.angleTo(point)
  length = myPath.center.distanceTo(point)
  factor = 1.5

  print("direction", direction, "length", length)

  point.moveVector(direction, length * factor - length)

movePoint(myPath.points[0])
movePoint(myPath.points[1])
movePoint(myPath.points[2])
movePoint(myPath.points[3])


myDrawing.save("test.svg")
