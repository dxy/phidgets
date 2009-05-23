#!/usr/bin/python

from sensor import *

class BlankSensor(Sensor):
  def __init__(self):
    self.value = 0
    self.product_name = ""

