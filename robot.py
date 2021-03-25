from models import Drive, KerberosSDR, Arduino
import math

class Robot:
    def __init__(self, drive: Drive, radio: KerberosSDR, arduino: Arduino):
        self.drive = drive
        self.radio = radio
        self.arduino = arduino

    def run(self, method="simple_drive"):
        #self.arduino.update()

        getattr(self, method)()

    def simple_drive(self):
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
        if degree <= 5:
            self.drive.tank_drive(1, 0.9572)
        elif degree <= 10:
            self.drive.tank_drive(1, 0.9156)
        elif degree <= 22.5:
            self.drive.tank_drive(1, 0.8124)
        elif degree <= 45:
            self.drive.tank_drive(1, 0.6)
        elif degree <= 67.5:
            self.drive.tank_drive(1, 0.2473)
        elif degree <= 180:
            self.drive.tank_drive(0.5, -0.5)
        elif degree >= 355:
            self.drive.tank_drive(0.9572, 1)
        elif degree >= 350:
            self.drive.tank_drive(0.9156, 1)
        elif degree >= 337.5:
            self.drive.tank_drive(0.8124, 1)
        elif degree >= 315:
            self.drive.tank_drive(0.6, 1)
        elif degree >= 292.5:
            self.drive.tank_drive(0.2473, 1)
        else:
            self.drive.tank_drive(-0.5, 0.5)        
