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

        degree = (round(self.radio.get_DOA(), 4) + 45) %360 - 180
        #if degree <= 5 or degree <= 355:
            #self.tankdrive(1,1)
        angle = round(math.radians(degree), 4)
        forward = round(2 * math.cos(angle), 4)
        turn = round(math.sin(angle) / 2, 4)
        self.drive.arcade_drive(forward, turn)
        
