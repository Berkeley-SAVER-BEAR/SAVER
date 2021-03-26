from robot import Robot
from models import Arduino, Drive, KerberosSDR, SpeedController
from constants import *
import time

arduino = Arduino()
thrusters = SpeedController(arduino)
drive = Drive(thrusters)
#imu = Imu()
radio = KerberosSDR()
    

def accelerate_test(duration):
    # start with scale of 0.1, increment by 0.3 for each iteration
    for x in range(0.1, 1.1, 0.3):
        # keeps current speed for duration
        drive.tank_drive(1, 1, x)
        time.sleep(duration)
    drive.drive.tank_drive(0, 0, 0)
    time.sleep(3)


def decelerate_test(duration):
    # start with scale of 1, decrement by 0.3 for each iteration
    for x in range(1, 0.0, -0.3):
        drive.tank_drive(1, 1, x)
        # keeps current speed for duration
        time.sleep(duration)
    drive.drive.tank_drive(0, 0, 0)
    time.sleep(3)

    
def manualtest():
    robot = Robot(drive, radio, arduino)
    
    # test acceleration and deceleration
    robot.run(accelerate_test(1))
    time.sleep(2)
    robot.run(decelerate_test(1))


if __name__ == "__manualtest__":
    manualtest()