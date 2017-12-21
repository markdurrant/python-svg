#!/usr/bin/env python3

from paper import Paper
from pen import Pen
from path import Path
from point import Point

myDrawing = Paper()

# myPoint = Point(0, 0)
# myPoint2 = myPoint.clone()
# myPoint2.move(10, 10)
# myPoint.log()
# myPoint2.log()

# size = 100
# center = { 'x': myDrawing.width / 2, 'y': myDrawing.height / 2}

# myDrawing.pens = [Pen(
#   paths = [Path(
#     points = [
#       Point(center['x'] + size, center['y']),
#       Point(center['x'], center['y'] + size),
#       Point(center['x'] - size, center['y']),
#       Point(center['x'], center['y'] - size)
#     ],
#     closed = True
#   )],
#   weight = 10
# )]

# myPath = myDrawing.pens[0].paths[0]
# myPath.topLeft.log()
# myPath.setBox()

# myPath2 = Path()
# myPath.log()

myPath = Path(points = [Point(0, 0), Point(0, 10), Point(10, 10)])
myPath.addPoints([Point(10, 0)])
myPath.addPoints([Point(20, 20)], 1)

myPath.move(10, 10).log()
# myPath.log()

myDrawing.save("test.svg")