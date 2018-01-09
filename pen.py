#!/usr/bin/env python3
import textwrap

from path import Path
from point import Point

class Pen():

  def __init__(self, paths = None, weight = 2, color = "#000"):
    self.label = "Pen"

    if paths is None:
      self.paths = []
    else: 
      self.paths = paths

    self.weight = weight
    self.color = color

    if paths:
      self.setBox()

  def setBox(cls):
    top = cls.paths[0].top
    bottom = cls.paths[0].bottom
    right = cls.paths[0].right
    left = cls.paths[0].left

    for path in(cls.paths):
      if path.top < top:
        top = path.top
      if path.bottom > bottom:
        bottom = path.bottom
      if path.right < right:
        right = path.right
      if path.left > left:
        left = path.left

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

  def setWeight(cls, weight):
    cls.weight = weight

    return weight

  def setColor(cls, color):
    cls.color = color

    return cls

  def addPaths(cls, paths, index = None):
    if not index:
      cls.paths += paths
    else: 
      for i, path in enumerate(paths):
        cls.paths.insert(index + i, path)

    cls.setBox()

    return cls

  def removePaths(cls, number = 1, index = None):
    if not index:
      del cls.paths[len(cls.paths) - number:]
    else:
      for _ in range(number):
        del cls.paths[index]

    cls.setBox()

    return cls

  def move(cls, x, y):
    for path in cls.paths:
      path.move(x, y)

    cls.setBox()

    return cls

  # def moveVector(cls, direction, length):
  #   # for 

  def render(cls):
    penTag = '<g style="fill: none; stroke-linecap: round;' \
      'stroke-linejoin: round; stroke-width: {}; stroke: {};">' \
      .format(cls.weight, cls.color)

    for path in cls.paths:
      penTag += "\n  " + path.render()

    return penTag + '\n</g>'

  def getLog(cls):
    log = "\u2571 Pen [ weight = {},  color = {}]".format(cls.weight, cls.color)
    pathLog = ""

    for i, path in enumerate(cls.paths):
      pathLog += "\n" + path.getLog().replace("Path", "Path[" + str(i) + "]")

    return log + textwrap.indent(pathLog, "  ")

  def log(cls):
    print(cls.getLog()) 