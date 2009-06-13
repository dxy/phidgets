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
    Sensor.__init__(self)
    #self.__max = 0
    #self.__min = 0
    self.__label = 'luminosity'
    self.__product_name = 'Precision Light Sensor'
    self.__product_number = '1127'

  def __GetValue(self):
    return self.__value

  def __SetValue(self, value):
    self.__value = value

  def __GetLabel(self):
    return self.__label

  value = property(__GetValue, __SetValue)
  label = property(__GetLabel)
