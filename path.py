#!/usr/bin/env python3

import textwrap

from point import Point

class Path():

  def __init__(self, points = [], closed = False):
    self.label = "Path"
    self.points = points
    self.closed = closed

    if len(self.points) > 0:
      self.setBox()

  def setBox(cls):
    top = cls.points[1].y
    bottom = cls.points[1].y
    right = cls.points[1].x
    left = cls.points[1].x

    for point in(cls.points):
      if point.y < top:
        top = point.y
      if point.y > bottom:
        bottom = point.y
      if point.x < right:
        right = point.x
      if point.x > left:
        left = point.x

    hCenter = left + (right - left) / 2
    vCenter = top + (bottom - top) / 2

    cls.left = left
    cls.right = right
    cls.top = top
    cls.bottom = bottom

    cls.topLeft      = Point(left, top)
    cls.topCenter    = Point(hCenter, top)
    cls.topRight     = Point(right, top)
    cls.leftCenter   = Point(left, vCenter)
    cls.center       = Point(hCenter, vCenter)
    cls.rightCenter  = Point(right, vCenter)
    cls.bottomLeft   = Point(left, bottom)
    cls.bottomCenter = Point(hCenter, bottom)
    cls.bottomRight  = Point(right, bottom)

  def makeClosed():
    cls.closed = True
    
    return cls

  def makeOpen():
    cls.closed = False
    
    return cls

  def addPoints(cls, points, index = None):
    if not index:
      cls.points += points
    else:
      for i, point in enumerate(points):
        cls.points.insert(index + i, point)
    
    cls.setBox()
    
    return cls

  def removePoints(cls, number = 1, index = None):
    if not index: 
      del cls.points[len(cls.points) - number:]
    else: 
      for _ in range(number):
        del cls.points[index]
    
    cls.setBox()
    
    return cls

  def move(cls, x, y):
    for point in cls.points:
      point.move(x, y)

    cls.setBox()
    
    return cls

  def moveVector(cls, direction, length):
    for point in cls.points:
      point.moveVector(direction, length)

    cls.setBox()

    return cls

  def rotate(cls, angle, origin = None):
    if not origin:
      origin = cls.center

    for point in cls.points:
      point.rotate(angle, origin)

    cls.setBox()

    return cls

  def scale(cls, factor):
    for point in cls.points:
      direction = cls.center.angleTo(point)
      length = cls.center.distanceTo(point)

      point.moveVector(direction, length * factor - length)
    
    cls.setBox()

    return cls

  def render(cls):
    pathTag = ""

    for i, point in enumerate(cls.points):
      if i == 0:
        pathTag += "M "
      else:
        pathTag += " L"

      pathTag += str(point.x) + " " + str(point.y)

    if cls.closed == True:
      pathTag += " Z"

    return '<path d="' + pathTag + '"/>'

  def getLog(cls):
    log = "\u2B20  Path [ closed = {} ]".format(cls.closed)
    pointLog = ""

    for i, point in enumerate(cls.points):
      pointLog += "\n" + point.getLog().replace("Point", "Point[" + str(i) + "]")

    return log + textwrap.indent(pointLog, "  ")

  def log(cls):
    print(cls.getLog())
