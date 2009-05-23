#!/usr/bin/python

from sensor import *

class PrecisionLightSensor(Sensor):
  def __init__(self):
    self.value = 0
    #self.max = 0
    #self.min = 0
    self.label = 'luminosity'
    self.product_name = 'Precision Light Sensor'
    self.product_number = '1127'

  def SetValue(self, value):
    # cf. 1127.pdf
    self.value = value

