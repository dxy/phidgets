#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2009 Daisuke Yabuki. All Rights Reserved.

"""Test for sensors.humidity_sensor"""

__author__ = 'dxy@acm.org (Daisuke Yabuki)'

import unittest
import humidity_sensor

class UnitTest(unittest.TestCase):
  def setUp(self):
    self.sensor = humidity_sensor.HumiditySensor()

  def tearDown(self):
    pass

  def testSensor(self):
    self.sensor.value = 320
    #self.assertEqual(self.sensor.value, 20.791999999999994)
    self.assertAlmostEqual(self.sensor.value, 20.792)

  def testLabel(self):
    self.assertEqual(self.sensor.label, 'humidity')

def main():
  unittest.main()


if __name__ == '__main__':
  main()
