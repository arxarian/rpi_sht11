#!/usr/bin/python3

import sys
from threading import Timer
import RPi.GPIO as GPIO
from pi_sht1x import SHT1x

DATA = 14
SCK = 15

def measure():
  with SHT1x(DATA, SCK, GPIO.BCM) as sensor:
    tem = sensor.read_temperature()
    hum = sensor.read_humidity(tem)
    print("Temperature: " + str(tem) + "\nHumidity: " + str(hum) + "\n\n")

interval = 1

if len(sys.argv) > 1:
  interval = sys.argv[1]

measure()
while True:
  t = Timer(interval, measure)
  t.start()
  t.join()
