#!/usr/bin/python3

import mysql.connector

class DB_Measurements:
    def __init__(self):
        self.table = "measurements"
        self.db = mysql.connector.connect(
            host="localhost",
            user="measurer",
            passwd="thefifthfloor",
            database="measurements"
        )
        self.cursor = self.db.cursor()
        self.__createTableIfNotExists()

    def __createTableIfNotExists(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS " + str(self.table) + " (id INT AUTO_INCREMENT PRIMARY KEY, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, temperature DECIMAL(16,14), humidity DECIMAL(16,14))") 

    def add(self, temperature, humidity):
        sql = "INSERT INTO " + str(self.table) + " (temperature, humidity) VALUES (%s, %s)"
        val = (temperature, humidity)
        self.cursor.execute(sql, val)

        self.db.commit()

    def printAll(self):
        self.cursor.execute("SELECT * FROM " + str(self.table))

        myresult = self.cursor.fetchall()

        for x in myresult:
            print(x)
