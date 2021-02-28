from models import Drive, KerberosSdr, Imu, Arduino

class Robot:
    def __init__(self, drive: Drive, radio: KerberosSdr, imu: Imu, arduino: Arduino):
        self.drive = drive
        self.radio = radio
        self.imu = imu
        self.arduino = arduino

    def run(self):
        self.arduino.update()
        self.drive.tank_drive(1, 1)