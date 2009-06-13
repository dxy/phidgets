#!/usr/bin/python

class Sensor(object):
  def __init__(self):
    self.__value = 0
    self.__max = 0
    self.__min = 0
    self.__label = ''
    self.__product_name = ''
    self.__product_number = ''

  def __GetValue(self):
    return self.__value

  def __SetValue(self, value):
    self.__value = value

  value = property(__GetValue, __SetValue)

  def __GetMax(self):
    return self.__max

  def __SetMax(self, max):
    self.__max = max

  max = property(__GetMax, __SetMax)

  def __GetMin(self):
    return self.__min

  def __SetMin(self, min):
    self.__min = min

  min = property(__GetMin, __SetMin)

  def __GetLabel(self):
    return self.__label

  def __SetLabel(self, label):
    self.__label = label

  label = property(__GetLabel, __SetLabel)

  def __GetProductName(self):
    return self.__product_name

  def __SetProductName(self, product_name):
    self.__product_name = product_name

  product_name = property(__GetProductName, __SetProductName)

  def __GetProductNumber(self):
    return self.__product_number

  def __SetProductNumber(self, product_number):
    self.__product_number = product_number

  product_number = property(__GetProductNumber, __SetProductNumber)



