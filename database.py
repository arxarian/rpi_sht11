#!/usr/bin/python3

import mysql.connector

class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="measurer",
            passwd="thefifthfloor",
            database="measurements"
        )
        self.cursor = self.db.cursor()
        self.CreateTableIfNotExists()

    def CreateTableIfNotExists(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS measurements (id INT AUTO_INCREMENT PRIMARY KEY, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, temperature DECIMAL(16,14), humidity DECIMAL(16,14))") 

    def AddMeasurement(self, temperature, humidity):
        sql = "INSERT INTO measurements (temperature, humidity) VALUES (%s, %s)"
        val = (temperature, humidity)
        self.cursor.execute(sql, val)

        self.db.commit()

    def PrintAll(self):
        self.cursor.execute("SELECT * FROM measurements")

        myresult = self.cursor.fetchall()

        for x in myresult:
            print(x)
