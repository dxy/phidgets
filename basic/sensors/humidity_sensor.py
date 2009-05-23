#!/usr/bin/python

from sensor import *

class HumiditySensor(Sensor):
  def __init__(self):
    self.value = 0
    self.max = 95 
    self.min = 10
    self.label = 'humidity'
    self.product_name = 'Humidity Sensor'
    self.product_number = '1125'

  def SetValue(self, value):
    # cf. 1125.pdf
    self.value = ((value * 190.6 ) / 1000) - 40.2

