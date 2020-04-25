#!/usr/bin/python3

import sys
import time
from datetime import datetime

import sensors
import db_current
import db_measurements

sht11 = sensors.SHT11()
currentMeasurement = db_current.DB_CurrentMeasurement()
measurements = db_measurements.DB_Measurements()

totalTemperature = 0
totalHumidity = 0
totalMeasurements = 0
averageInterval = 15 # seconds
lastTimestamp = datetime.timestamp(datetime.now())

while True:
    measurement = sht11.measure()
    currentMeasurement.Update(measurement[0], measurement[1])

    timestamp = datetime.timestamp(datetime.now())
    totalTemperature += measurement[0]
    totalHumidity += measurement[1]
    totalMeasurements += 1

    print(timestamp - lastTimestamp)

    if (timestamp - lastTimestamp) > averageInterval:
        averageTemperature = totalTemperature  / totalMeasurements
        averageHumidity = totalHumidity  / totalMeasurements
        print("average temperature: " + str(averageTemperature) + " °C")
        print("average humidity: " + str(averageHumidity) + " %")

        measurements.Add(measurement[0], measurement[1])
        totalTemperature = 0
        totalHumidity = 0
        totalMeasurements = 0
        lastTimestamp = timestamp

    time.sleep(5)
