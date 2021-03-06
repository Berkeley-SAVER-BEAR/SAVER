from models import Drive, KerberosSDR, Arduino, Imu
import math
from constants import *

class Robot:
    def __init__(self, drive: Drive, radio: KerberosSDR, arduino: Arduino, imu: Imu):
        self.drive = drive
        self.radio = radio
        self.arduino = arduino
        self.imu = imu

    def run(self, method="simple_drive"):
        #self.arduino.update()

        getattr(self, method)(SCALE)

    def simple_drive(self, scale):
        """Turns in place if at an obtuse angle, 
        turns slightly when at an acute angle, 
        and runs straight when within 15 degrees"""
        
        '''doa = self.radio.get_DOA()
        doa -= (doa // 180) * 360 # get it into -180 to 180

        if doa < -90:
            self.drive.tank_drive(1, -1)            
        elif doa < -15:
            self.drive.tank_drive(1, 0)
        elif doa < 15:
            self.drive.tank_drive(1, 1)
        elif doa < 90:
            self.drive.tank_drive(0, 1)
        else:
            self.drive.tank_drive(-1, 1)'''

        degree = (round(self.radio.get_DOA(), 4) + 45) %360
        #degree = (round(self.manualtest._____, 4) + 45) %360

        if degree <= 5:
            self.drive.tank_drive(1, 0.9572, scale)
        elif degree <= 10:
            self.drive.tank_drive(1, 0.9156, scale)
        elif degree <= 22.5:
            self.drive.tank_drive(1, 0.8124, scale)
        elif degree <= 45:
            self.drive.tank_drive(1, 0.6, scale)
        elif degree <= 67.5:
            self.drive.tank_drive(1, 0.2473, scale)
        elif degree <= 180:
            self.drive.tank_drive(0.5, 0, scale)
        elif degree >= 355:
            self.drive.tank_drive(0.9572, 1, scale)
        elif degree >= 350:
            self.drive.tank_drive(0.9156, 1, scale)
        elif degree >= 337.5:
            self.drive.tank_drive(0.8124, 1, scale)
        elif degree >= 315:
            self.drive.tank_drive(0.6, 1, scale)
        elif degree >= 292.5:
            self.drive.tank_drive(0.2473, 1, scale)
        else:
            self.drive.tank_drive(0, 0.5, scale)        
