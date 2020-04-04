#!/usr/bin/python3

import sys
import datetime
import json

import RPi.GPIO as GPIO
from threading import Timer
from pi_sht1x import SHT1x

DATA = 14
SCK = 15

def writeJson(json):
    f = open("./currentdata.json", "w")
#    f = open("/var/www/html/currentdata.json", "w")
    f.write(json + "\n")
    f.close()

def compose(tem, hum):
    data = {}

    temperature_data = {}
    temperature_data["unit"] = "°C"
    temperature_data["value"] = tem

    data["temperature"] = temperature_data

    humidity_data = {}
    humidity_data["unit"] = "%"
    humidity_data["value"] = hum
    data["humidity"] = humidity_data

    data["timestamp"] = datetime.datetime.now().timestamp()

    return data

def measure():
  with SHT1x(DATA, SCK, GPIO.BCM) as sensor:
    tem = sensor.read_temperature()
    hum = sensor.read_humidity(tem)

    return tem, hum

measurement = measure()
data = compose(measurement[0], measurement[1])
json_data = json.dumps(data)

print(json_data)

writeJson(json_data)

