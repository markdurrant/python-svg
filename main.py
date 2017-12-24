#!/usr/bin/env python3

from paper import Paper
from pen import Pen
from path import Path
from point import Point

myDrawing = Paper()

size = 100
center = { 'x': myDrawing.width / 2, 'y': myDrawing.height / 2}

myDrawing.pens = [Pen(
  paths = [Path(
    points = [
      Point(center['x'] + size, center['y']),
      Point(center['x'], center['y'] + size),
      Point(center['x'] - size, center['y']),
      Point(center['x'], center['y'] - size)
    ],
    closed = True
  )],
  weight = 10
)]


myDrawing.save("test.svg")
