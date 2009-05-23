#!/usr/bin/python

from sensor import *

class TemperatureSensor(Sensor):
  """Phidgets 1125 Temperature Sensor.

  cf. http://www.phidgets.com/documentation/Phidgets/1125.pdf

  Attributes:
    value: temperature calculated from raw sensor value.
    max: maximum value the sensor measures.
    min: minimum value the sensor measures.
    label: a string used as a filename for saving data.
    product_name: a string containing product name.
    product_number: a string containing product #.
  """
  def __init__(self):
    self.value = 0
    self.max = 100
    self.min = -40
    self.label = 'temperature'
    self.product_name = 'Temperature Sensor'
    self.product_number = '1125'

  def SetValue(self, value):
    self.value = ((value * 222.22 ) / 1000) - 61.11

