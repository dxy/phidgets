#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2008 Daisuke Yabuki. All Rights Reserved.

"""A class representing a Phidget sensor."""

class Sensor(object):
  """
  Attributes:
    value:
      A float value calculated based on a raw sensor reading with the formula
      documented in the sensor's manual.
    max:
      A float value representing the maximum value supported for the sensor
      documented in the manual.
    min:
      A float value representing the minimum value supported for the sensor
      documented in the manual.
    label:
      A simple string representing the name of the sensor. This is used
      as a filename to save the reading in. So it shouldn't containt
      a white space.
    product_name:
      The descriptive name of a sensor model. This is meant to be used for
      telling users about the sensor. So this could be a string including
      white spaces.
    product_number:
      The product number of a sensor model. This is meant to be used for
      telling users about the sensor. So this could be a string including
      "-" or some alphabets in addition to numbers.
  """

  def __init__(self):
    self.__value = 0
    self.__max = 0
    self.__min = 0
    self.__label = ''
    self.__product_name = ''
    self.__product_number = ''

  def __GetValue(self):
    "Getter for 'value' property."
    return self.__value

  def __SetValue(self, value):
    """Setter for 'value' property.

    Args:
      value:
        A float value representing the row reading observed with a sensor.
    """
    self.__value = value

  value = property(__GetValue, __SetValue, doc='value calulated from sensor')

  def __GetMax(self):
    "Getter for 'max' property."
    return self.__max

  def __SetMax(self, max):
    """Setter for 'max' property.

    Args:
      max:
        A float value representing the maximum reading the sensor supports.
    """
    self.__max = max

  max = property(__GetMax, __SetMax, doc='maximum sensor value')

  def __GetMin(self):
    "Getter for 'min' property."
    return self.__min

  def __SetMin(self, min):
    """Setter for 'min' property.

    Args:
      min:
        A float value representing the minimum reading the sensor supports.
    """
    self.__min = min

  min = property(__GetMin, __SetMin, doc='minimum sensor value')

  def __GetLabel(self):
    "Getter for 'label' property."
    return self.__label

  def __SetLabel(self, label):
    """Setter for 'label' property.

    Args:
      label:
        A string representing the name of the sensor.
    """
    self.__label = label

  label = property(__GetLabel, __SetLabel, doc='label of sensor name')

  def __GetProductName(self):
    "Getter for 'product_name' property."
    return self.__product_name

  def __SetProductName(self, product_name):
    """Setter for 'product_name' property.

    Args:
      product_name:
        A string representing the descriptive name of the sensor.
    """
    self.__product_name = product_name

  product_name = property(__GetProductName, __SetProductName,
                          doc='sensor product name')

  def __GetProductNumber(self):
    "Getter for 'product_number' property."
    return self.__product_number

  def __SetProductNumber(self, product_number):
    """Setter for 'product_number' property.

    Args:
      product_name:
        A string representing the product number of the sensor.
    """
    self.__product_number = product_number

  product_number = property(__GetProductNumber, __SetProductNumber,
                            doc='sensor product number')

