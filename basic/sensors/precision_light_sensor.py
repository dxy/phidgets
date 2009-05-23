#!/usr/bin/python

from sensor import *

class PrecisionLightSensor(Sensor):
  """Phidgets 1127 Precision Light Sensor.

  cf. http://www.phidgets.com/documentation/Phidgets/1127.pdf

  Attributes:
    value: luminosity (in lux) calculated from raw sensor value.
    max: maximum value the sensor measures.
    min: minimum value the sensor measures.
    label: a string used as a filename for saving data.
    product_name: a string containing product name.
    product_number: a string containing product #.
  """

  def __init__(self):
    self.value = 0
    #self.max = 0
    #self.min = 0
    self.label = 'luminosity'
    self.product_name = 'Precision Light Sensor'
    self.product_number = '1127'

  def SetValue(self, value):
    self.value = value

