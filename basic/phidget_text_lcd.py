#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2008 Daisuke Yabuki. All Rights Reserved.

"""A one line summary of the module or script, terminated by a period.

Leave one blank line. The rest of this doc string should contain an
overall description of the module or script. Optionally, it may also
contain a brief description of exported classes and functions.

  ClassFoo: One line summary.
  FunctionBar(): One line summary.
"""

__author__ = 'dxy@acm.org (Daisuke Yabuki)'

import datetime
import os
import sys
import time
from Phidgets.PhidgetException import *
from Phidgets.Events.Events import *
from Phidgets.Devices.InterfaceKit import *
from Phidgets.Devices.TextLCD import *
from sensors.blank_sensor import *
from sensors.humidity_sensor import *
from sensors.precision_light_sensor import *
from sensors.temperature_sensor import *


class PhidgetTextLCD(object):
  """
  A class modelled after a Phidget InterfaceKit with an integrated LCD.
  It contains a list of objects, which are subclasses of Sensor object.

  Attributes:
      analog_sensors: a list containing objects of one of subclasses of Sensor
      data_dir: a string of directory path to save sensor reading data in
  """

  def __init__(self, analog_sensors, data_dir):
    """Initializes the members."""
    self.interfaceKit = InterfaceKit()
    self.textLCD = TextLCD()

    self.data_dir = data_dir

    # instantiate classes according to actual sensor port configuration
    self.sensors = []
    for sensor in analog_sensors:
      aSensor = self.Factory(sensor)
      self.sensors.append(aSensor)

    try:
      # Interface Kit
      self.interfaceKit.openPhidget()
      self.interfaceKit.waitForAttach(10000)
      print "%s (serial: %d) attached!" % (
        self.interfaceKit.getDeviceName(), self.interfaceKit.getSerialNum())

      # get initial value from each sensor
      i = 0
      for sensor in self.sensors:
        #print sensor.product_name
        #print sensor.value
        sensor.value = self.interfaceKit.getSensorValue(i)
        i += 1

      self.interfaceKit.setOnSensorChangeHandler(self.SensorChanged)

      # Text LCD
      self.textLCD.openPhidget()
      self.textLCD.waitForAttach(10000)
      print "%s attached!" % (self.textLCD.getDeviceName())

      self.textLCD.setCursorBlink(False)

    except PhidgetException, e:
      print "Phidget Exception %i: %s" % (e.code, e.message)
      sys.exit(1)

  def SensorChanged(self, e):
    """A call back method called when a value changes."""
    sensor = self.sensors[e.index]
    sensor.value = e.value
    # TODO(dxy): maybe update LCD

  def Factory(self, klass, *args):
    """A factory to instantiate an object for a given Sensor class."""
    try:
      anObject = apply(klass, args)
      #print klass.__name__ + " instantiated"
      return anObject
    except:
      print "failed to instantiate a sensor class " + klass.__name__
      sys.exit(1)

  def Poll(self):
    """A loop to update time on LCD and save data to files."""
    while 1:
      now = datetime.datetime.today()
      self.textLCD.setDisplayString(0, now.strftime("%Y/%m/%d %H:%M:%S"))
      second = int(now.strftime("%S"))
      if second % 15 == 0:
        self.SaveValues()
      time.sleep(1)

  def SaveValues(self):
    """Save value for each sensor in the sensors list to a file."""
    for sensor in self.sensors:
      if sensor.__class__ == BlankSensor:
        continue
      data_file_path = os.path.join(self.data_dir, sensor.label)
      try:
        data_file = open(data_file_path, 'w')
        data_file.write("%f\n" % sensor.value)
        data_file.close()
      except IOError, e:
        print "failed to write data %s" % e
