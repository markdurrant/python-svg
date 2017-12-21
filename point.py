#!/usr/bin/env python3

import math
import copy

class Point():
  
  def __init__(self, x = 0, y = 0):
    self.label = "Point"
    self.x = x
    self.y = y

  def move(cls, x = 0, y = 0):
    if x and y == 0:
      y = x

    cls.x += x
    cls.y += y

  def moveVector(cls, direction = 0, length = 0):
    angle = math.radians(direction - 90)

    cls.x += math.cos(angle) * length
    cls.y += math.sin(angle) * length

  def rotate(cls, angle, origin):
    radians = math.radians(angle)

    x1 = cls.x - origin.x
    y1 = cls.y - origin.y

    x2 = x1 * math.cos(radians) - y1 * math.sin(radians)
    y2 = x1 * math.sin(radians) + y1 * math.cos(radians)

    cls.x = x2 + origin.x
    cls.y = y2 + origin.y

  def distanceTo(cls, point):
    a = cls.x - point.x
    b = cls.y - point.y

    if a == 0:
      distance = b
    elif b == 0:
      distance = a
    else:
      distance = math.fabs(math.sqrt(a * a + b * b))

    return distance

  def angleTo(cls, point):
    a = cls.x - point.x
    b = cls.y - point.y

    angle = math.degrees(math.atan2(b, a))

    if angle < 0:
      angle += 360

    angle -= 90

    if angle < 0:
      angle += 360

    return angle

  def equalTo(cls, point):
    if cls.x == point.x and cls.y == point.y:
      return True
    else:
      return False

  def clone(cls):
    return copy.deepcopy(cls)

  def getLog(cls):
    return "\u2022 Point [ x = {}, y = {} ]".format(cls.x, cls.y)

  def log(cls):
    print(cls.getLog())