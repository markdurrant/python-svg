#!/usr/bin/env python3

import textwrap
import copy

from point import Point

class Path():

  def __init__(self, points = None, closed = False):
    self.label = "Path"

    if points is None:
      self.points = []
    else:
      self.points = points
      self.setBox()

    self.closed = closed

  def setBox(cls):
    top = cls.points[0].y
    bottom = cls.points[0].y
    right = cls.points[0].x
    left = cls.points[0].x

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

  def length(cls):
    length = 0
    
    for p, point in enumerate(cls.points[:-1]):
      length += point.distanceTo(cls.points[p + 1])

    if cls.closed == True:
      length += cls.points[0].distanceTo(cls.points[-1])

    return length

  def pointAtDistance(cls, distance):
    pointAD = None

    for p, point in enumerate(cls.points[:-1]):
      segmentLength = point.distanceTo(cls.points[p + 1])

    if distance > segmentLength:
      distance = distance - segmentLength
    elif distance >= 0:
      angle = point.angleTo(cls.points[p + 1])

      pointAD = Point(point.x, point.y)
      pointAD.moveVector(angle, distance)

      distance = distance - segmentLength
      
    return pointAD

  def intersectsSelf():
    print("NOT YET IMPLIMENTED")

  def intersections():
    print("NOT YET IMPLIMENTED")

  def equalTo():
    print("NOT YET IMPLIMENTED")

  def clone(cls):
    return copy.deepcopy(cls)

  def setPen(cls, pen):
    pen.paths.append(cls)

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

  def renderGCode(cls):
    gCode = ""

    for i, p in enumerate(cls.points):
      gCode += "\nG1 X{} Y{}".format(p.x, p.y)

      if i == 0:
        gCode += "\nM03 S1000"

    if cls.closed == True:
      gCode += "\G1 X{} Y{}".format(cls.points[0].x, cls.points[0].y)

    gCode += "\nM05 S1000"

    return gCode

  def getLog(cls):
    log = "\u2B20  Path [ closed = {} ]".format(cls.closed)
    pointLog = ""

    for i, point in enumerate(cls.points):
      pointLog += "\n" + point.getLog().replace("Point", "Point[" + str(i) + "]")

    return log + textwrap.indent(pointLog, "  ")

  def log(cls):
    print(cls.getLog())
