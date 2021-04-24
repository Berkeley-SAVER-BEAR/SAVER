from robot import Robot
<<<<<<< HEAD
from models import Arduino, Drive, KerberosSDR, SpeedController, Lidar
=======
from models import Arduino, Drive, KerberosSDR, SpeedController, Imu
>>>>>>> 68d09383723e6a5830bdb41a6682d308abb413fe
from constants import *
import time

def initialize():
    arduino = Arduino()
    thrusters = SpeedController(arduino)
    drive = Drive(thrusters)
    imu = Imu()
    radio = KerberosSDR()
    lidar = Lidar()

<<<<<<< HEAD
    return drive, radio, arduino, lidar
=======
    return drive, radio, arduino, imu
>>>>>>> 68d09383723e6a5830bdb41a6682d308abb413fe

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
