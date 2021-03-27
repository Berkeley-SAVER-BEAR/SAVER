from robot import Robot
from models import Arduino, Drive, KerberosSDR, SpeedController
from constants import *
import time

TEST_SCALE = 0.1
DURATION = 3
TURNTIME = 2

class ManualTestAcceleration:
        def __init__(self):
            self.arduino = Arduino()
            self.thrusters = SpeedController(self.arduino)
            self.drive = Drive(self.thrusters)
            #imu = Imu()
            self.radio = KerberosSDR()

            self.robot = Robot(self.drive, self.radio, self.arduino)

            for i in range(8):
                self.drive.tank_drive(0, 0, TEST_SCALE)
            #return drive, radio, arduino
            
        #def main():
        #    drive, radio, arduino = initialize()
        #    robot = Robot(drive, radio, arduino)
            #test_scale = 0.1
            #duration = 3
            #turntime = 2

            #for i in range(8):
            #    drive.tank_drive(0, 0, test_scale)

            #accelerate_test(drive, duration)
            #decelerate_test(drive, duration)
            #manualtest(drive, duration)

        def accelerate_test(self, duration=DURATION):
            # start with scale of 0.1, increment by 0.3 for each iteration
            self.drive.tank_drive(0, 0, duration)
            time.sleep(3)
            for i in range(1, 10, 3):
                x = i / 10
                # keeps current speed for duration
                self.drive.tank_drive(1, 1, x)
                time.sleep(duration)
            self.drive.tank_drive(0, 0, 0)


        def decelerate_test(self, duration=DURATION):
            # start with scale of 1, decrement by 0.3 for each iteration
            self.drive.tank_drive(0, 0, duration)
            time.sleep(3)
            for i in range(1, 10, 3):
                x = (11 - i) / 10
                self.drive.tank_drive(1, 1, x)
                # keeps current speed for duration
                time.sleep(duration)
            self.drive.tank_drive(0, 0, 0)

            
        def manualtest(self, duration=DURATION):
            
            # test acceleration and deceleration
            self.accelerate_test(duration)
            time.sleep(3)
            self.decelerate_test(duration)


#if __name__ == "__main__":
#    main()
