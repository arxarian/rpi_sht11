#!/usr/bin/python3

class Measurements:
    def __init__(self):
        self.totalTemperature = 0
        self.totalHumidity = 0
        self.totalMeasurements = 0

    def add(self, temperature, humidity):
        self.totalTemperature += temperature
        self.totalHumidity += humidity
        self.totalMeasurements += 1

    def average(self):
        averageTemperature = self.totalTemperature / self.totalMeasurements
        averageHumidity = self.totalHumidity / self.totalMeasurements
        return averageTemperature, averageHumidity

    def reset(self):
        self.__init__()
