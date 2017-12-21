#!/usr/bin/env python3
import textwrap

from path import Path

class Pen():

  def __init__(self, paths = [], weight = 2, color = "#000"):
    self.label = "Pen"
    self.paths = paths
    self.weight = weight
    self.color = color

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