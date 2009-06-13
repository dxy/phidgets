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
    Sensor.__init__(self)
    self.__max = 100
    self.__min = -40
    self.__label = 'temperature'
    self.__product_name = 'Temperature Sensor'
    self.__product_number = '1125'

  def __GetValue(self):
    return self.__value

  def __SetValue(self, value):
    self.__value = ((value * 222.22 ) / 1000) - 61.11

  def __GetLabel(self):
    return self.__label

  value = property(__GetValue, __SetValue)
  label = property(__GetLabel)
