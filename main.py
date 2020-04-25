#!/usr/bin/python3

import sys
import time
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

import sensors
import measurements
import db_current
import db_measurements

averageInterval = 600 # seconds
lastTimestamp = datetime.timestamp(datetime.now())

def measure():
    global averageInterval
    global lastTimestamp

    measurement = sht11.measure()
    currentMeasurement.update(measurement[0], measurement[1])

    timestamp = datetime.timestamp(datetime.now())
    measurements.add(measurement[0], measurement[1])

    if (timestamp - lastTimestamp) > averageInterval:
        averageMeasurements = measurements.average()

        print(datetime.now())
        print("average temperature: " + str(averageMeasurements[0]) + " °C")
        print("average humidity: " + str(averageMeasurements[1]) + " %")

        allMeasurements.add(averageMeasurements[0], averageMeasurements[1])
        lastTimestamp = timestamp

sht11 = sensors.SHT11()
measurements = measurements.Measurements()
currentMeasurement = db_current.DB_CurrentMeasurement()
allMeasurements = db_measurements.DB_Measurements()

scheduler = BackgroundScheduler()
scheduler.add_job(measure, 'interval', seconds = 3)
scheduler.start()

# come to sleep my baby
while True:
    time.sleep(5)
