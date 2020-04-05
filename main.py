#!/usr/bin/python3

import sys

import database
import sensors

from threading import Timer

SHT11 = sensors.SHT11()
measurement = SHT11.measure()

DB = database.Database()
DB.AddMeasurement(measurement[0], measurement[1])
DB.PrintAll()
