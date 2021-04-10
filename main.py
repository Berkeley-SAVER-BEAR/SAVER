from robot import Robot
from models import Arduino, Drive, KerberosSDR, SpeedController, Imu
from constants import *
import time

def initialize():
    arduino = Arduino()
    thrusters = SpeedController(arduino)
    drive = Drive(thrusters)
    imu = Imu()
    radio = KerberosSDR()

    return drive, radio, arduino, imu

def main():
    models = initialize()

    robot = Robot(*models)
    
    #delay
    #time.sleep(2)

    while True:
        robot.run()
        time.sleep(1 / CYCLES_PER_SECOND)
        #time.sleep(3)

if __name__ == "__main__":
    main()
