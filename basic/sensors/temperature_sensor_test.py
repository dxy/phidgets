#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2009 Daisuke Yabuki. All Rights Reserved.

"""Test for sensors.temperature_sensor"""

__author__ = 'dxy@acm.org (Daisuke Yabuki)'

import unittest
import temperature_sensor

class UnitTest(unittest.TestCase):
  def setUp(self):
    self.sensor = temperature_sensor.TemperatureSensor()

  def tearDown(self):
    pass

  def testSensor(self):
    self.sensor.value = 400
    self.assertAlmostEqual(self.sensor.value, 27.778)

  def testLabel(self):
    self.assertEqual(self.sensor.label, 'temperature')

def main():
  unittest.main()


if __name__ == '__main__':
  main()
