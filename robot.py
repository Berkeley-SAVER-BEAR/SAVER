from models import Drive, KerberosDR, Imu, Arduino

class Robot:
    def __init__(self, drive: Drive, radio: KerberosSDR, imu: Imu, arduino: Arduino):
        self.drive = drive
        self.radio = radio
        self.imu = imu
        self.arduino = arduino

    def run(self, method="simple_drive"):
        self.arduino.update()

        getattr(self, method)()

    def simple_drive(self):
        """Turns in place if at an obtuse angle, 
        turns slightly when at an acute angle, 
        and runs straight when within 15 degrees"""
        
        doa = radio.get_DOA()
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
            self.drive.tank_drive(-1, 1)
