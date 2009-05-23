#!/usr/bin/python

from sensor import *

class TemperatureSensor(Sensor):
  def __init__(self):
    self.value = 0
    self.max = 100
    self.min = -40
    self.label = 'temperature'
    self.product_name = 'Temperature Sensor'
    self.product_number = '1125'

  def SetValue(self, value):
    """Setter for value property.

    Args:
      value:
        The measured value with the sensor.

    Exceptions:
      
    """
    # cf. 1125.pdf
    self.value = ((value * 222.22 ) / 1000) - 61.11

  def GetValue(self):
    return self.value

  #value = property(GetValue, SetValue)

