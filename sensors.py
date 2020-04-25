#!/usr/bin/python3

import RPi.GPIO as GPIO
from pi_sht1x import SHT1x

class SHT11:
    def __init__(self):
        self.DATA = 14
        self.SCK = 15

    def measure(self):
        with SHT1x(self.DATA, self.SCK, GPIO.BCM) as sensor:
            tem = sensor.read_temperature()
            hum = sensor.read_humidity(tem)

            return tem, hum
