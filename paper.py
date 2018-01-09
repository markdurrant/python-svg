#!/usr/bin/env python3
import textwrap

from point import Point

class Paper():

  def __init__(self, pens = [], width = 640, height = 480, color = None):
    self.label = "paper"
    self.pens = pens
    self.width = width
    self.height = height
    self.color = color
    
    self.top = 0
    self.right = self.width
    self.bottom = self.height
    self.left = 0

    self.topLeft      = Point(0, 0)
    self.topCenter    = Point(self.width / 2, 0)
    self.topRight     = Point(self.width, 0)
    self.leftCenter   = Point(0, self.height / 2)
    self.center       = Point(self.width / 2, self.height / 2)
    self.rightCenter  = Point(self.width, self.height / 2)
    self.bottomLeft   = Point(0, self.height)
    self.bottomCenter = Point(self.width / 2, self.height)
    self.bottomRight  = Point(self.width, self.height)

  def render(cls):
    paperTag = '<?xml version="1.0" encoding="utf-8"?>' \
               '<svg version="1.1" xmlns="http://www.w3.org/2000/svg" ' \
               'xmlns:xlink="http://www.w3.org/1999/xlink" ' \
               'width="{}" height="{}" viewbox="0 0 {} {}">' \
               .format(cls.width, cls.height, cls.width, cls.height)

    for pen in cls.pens:
      paperTag += "\n" + textwrap.indent(pen.render(), "  ") 

    return paperTag + '</svg>'

  def save(cls, filename):
    f = open(filename,'w')
    f.write(cls.render())
    f.close()
    
    print("saved " + filename)

  def getLog(cls):
    log = "\u2B1A Paper [ width = {}, height = {} ]" \
      .format(cls.width, cls.height)
    penLog = ""

    if cls.color:
      log = log.replace("]", ", color = {}]".format(cls.color))

    for i, pen in enumerate(cls.pens):
      penLog += "\n" + pen.getLog().replace("Pen", "Pen[" + str(i) + "]")

    return log + textwrap.indent(penLog, "  ")

  def log(cls):
    print(cls.getLog())
