import time
import board
import busio
import adafruit_lidarlite

class Lidar:
    def __init__(self):
        # Possible problem when debugging is multiple instances of the i2c connection
        # here and in the Imu. If so, instantiate it in main.initalize() and then 
        # pass it in as an argument in the constructors of the Lidar and Imu.
        i2c = busio.I2C(board.SCL, board.SDA)

        self.sensor = adafruit_lidarlite.LIDARLite(i2c)

    def distance(self):
        """May throw a RuntimeError, make sure to handle that"""
        return self.sensor.distance()