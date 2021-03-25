from robot import Robot
from models import Arduino, Drive, KerberosSDR, SpeedController
from constants import *
import time

def initialize():
    arduino = Arduino()
    left_thruster = SpeedController(arduino, LEFT_THRUSTER_PORT)
    right_thruster = SpeedController(arduino, RIGHT_THRUSTER_PORT)
    drive = Drive(left_thruster, right_thruster)
    #imu = Imu()
    radio = KerberosSDR()

    return drive, radio, arduino

def main():
    models = initialize()

    robot = Robot(*models)

    while True:
        robot.run()
        time.sleep(1 / CYCLES_PER_SECOND)
        #time.sleep(2)

if __name__ == "__main__":
    main()
