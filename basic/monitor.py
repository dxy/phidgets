#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2008 Daisuke Yabuki. All Rights Reserved.

"""Continuously reads data from Phidgets sensors and save them to files.

Based on sensor configuration, the script reads data from sensors
and stores it to files so that it can be uploaded to pachube by another script.
"""

__author__ = 'dxy@acm.org (Daisuke Yabuki)'

#import settings
from phidget_text_lcd import *

# A directory to save sensor reading data.
data_dir_path = '/Users/dxy/Documents/phidgets/data/'

# A list of sensors connected to analog input port 0 to 7
analog_sensors = [TemperatureSensor,       # 0
                  HumiditySensor,          # 1
                  BlankSensor,             # 2
                  BlankSensor,             # 3
                  BlankSensor,             # 4
                  BlankSensor,             # 5 TODO(dxy): VibrationSensor
                  BlankSensor,             # 6 TODO(dxy): MotionSensor
                  PrecisionLightSensor]    # 7

def main():
  unit = PhidgetTextLCD(analog_sensors, data_dir_path)
  unit.Poll()

if __name__ == '__main__':
  main()
