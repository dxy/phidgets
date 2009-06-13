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
    Sensor.__init__(self)
    self.__max = 95
    self.__min = 10
    self.__label = 'humidity'
    self.__product_name = 'Humidity Sensor'
    self.__product_number = '1125'

  def __GetValue(self):
    return self.__value

  def __SetValue(self, value):
    self.__value = ((value * 190.6 ) / 1000) - 40.2

  def __GetLabel(self):
    return self.__label

  value = property(__GetValue, __SetValue)
  label = property(__GetLabel)
