from robot import Robot
from models import Arduino, Drive, KerberosSDR, SpeedController
from constants import *
import time

def initialize():
    arduino = Arduino()
    thrusters = SpeedController(arduino)
    drive = Drive(thrusters)
    #imu = Imu()
    radio = KerberosSDR()
    return drive, radio, arduino
    
def main():
    drive, radio, arduino = initialize()
    robot = Robot(drive, radio, arduino)
    test_scale = 0.1
    duration = 3
    turntime = 2

    for i in range(8):
        drive.tank_drive(0, 0, test_scale)

    #accelerate_test(drive, duration)
    #decelerate_test(drive, duration)
    manualtest(drive, duration)

def accelerate_test(drive, duration):
    # start with scale of 0.1, increment by 0.3 for each iteration
    drive.tank_drive(0, 0, duration)
    time.sleep(3)
    for i in range(1, 10, 3):
        x = i / 10
        # keeps current speed for duration
        drive.tank_drive(1, 1, x)
        time.sleep(duration)
    drive.tank_drive(0, 0, 0)


def decelerate_test(drive, duration):
    # start with scale of 1, decrement by 0.3 for each iteration
    drive.tank_drive(0, 0, duration)
    time.sleep(3)
    for i in range(1, 10, 3):
        x = (11 - i) / 10
        drive.tank_drive(1, 1, x)
        # keeps current speed for duration
        time.sleep(duration)
    drive.tank_drive(0, 0, 0)

    
def manualtest(drive, duration):
    
    # test acceleration and deceleration
    accelerate_test(drive, duration)
    time.sleep(3)
    decelerate_test(drive, duration)


if __name__ == "__main__":
    main()
