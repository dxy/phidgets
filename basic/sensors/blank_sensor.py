#!/usr/bin/python

from sensor import *

class BlankSensor(Sensor):
  """A class for an analog input port with no sensor connected.
  """
  def __init__(self):
    self.value = 0
    self.product_name = ''

