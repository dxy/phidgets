#!/usr/bin/python

from sensor import *

class HumiditySensor(Sensor):
  """Phidgets 1125 Humidity Sensor.

  cf. http://www.phidgets.com/documentation/Phidgets/1125.pdf

  Attributes:
    value: relative humidity calculated from raw sensor value.
    max: maximum value the sensor measures.
    min: minimum value the sensor measures.
    label: a string used as a filename for saving data.
    product_name: a string containing product name.
    product_number: a string containing product #.
  """
  def __init__(self):
    self.value = 0
    self.max = 95 
    self.min = 10
    self.label = 'humidity'
    self.product_name = 'Humidity Sensor'
    self.product_number = '1125'

  def SetValue(self, value):
    self.value = ((value * 190.6 ) / 1000) - 40.2

