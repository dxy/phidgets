#!/usr/bin/python

class Sensor(object):
  def __init__(self):
    self.value = 0
    self.max = 0
    self.min = 0
    self.label = ''
    self.product_name = ''
    self.product_number = ''

  def GetValue(self):
    return self.value

  def SetValue(self, value):
    self.value = value

  #value = property(GetValue, SetValue)
