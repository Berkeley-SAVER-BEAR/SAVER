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

    #uncomment depending on what test we want

    #turnrighttest(drive, duration, test_scale)
    #turnlefttest(drive, duration, test_scale)
    #straighttestparams(drive, duration, test_scale)
    turntest(drive)
    #straighttest(drive, duration, test_scale, turntime)
    #straightspeed(drive, duration, test_scale, turntime)
    
    # for timing purposes
    #t = returntime()
    #print(time.asctime(time.localtime(t)))

    
def turnrighttest(drive, duration, scale):
    drive.tank_drive(0, 0, scale)
    time.sleep(duration)
    drive.tank_drive(0.5, 0, scale)
    #self.drive.tank_drive(1, 0.2473, scale)
    #self.drive.tank_drive(1, 0.6, scale)
    #self.drive.tank_drive(1, 0.8124, scale)
    #self.drive.tank_drive(1, 0.9156, scale)
    #self.drive.tank_drive(1, 0.9572, scale)

    time.sleep(duration)
    drive.tank_drive(0, 0, scale)
    time.sleep(3)

def turnlefttest(drive, duration, scale):
    drive.tank_drive(0, 0, scale)
    time.sleep(duration)
    drive.tank_drive(0, 0.5, scale)
    #self.drive.tank_drive(0.2473, 1, scale)
    #self.drive.tank_drive(0.6, 1, scale)        
    #self.drive.tank_drive(0.8124, 1, scale)
    #self.drive.tank_drive(0.9156, 1, scale)        
    #self.drive.tank_drive(0.9572, 1, scale)
    time.sleep(duration)
    drive.tank_drive(0, 0, scale)
    time.sleep(3)

def straighttestparams(drive, duration, scale):
    drive.tank_drive(0, 0, scale)
    time.sleep(duration)
    drive.tank_drive(1, 1, scale)
    time.sleep(duration)
    drive.tank_drive(0, 0, scale)
    time.sleep(3)

def returntime():
    return time.time()
    

def turntest(drive):
    #turnrighttest and turnlefttest
    for y in range(10):
        scale = (y+1)/10
        for x in range(1, 5):
            turnrighttest(drive, x, scale)
            turnlefttest(drive, x, scale)

def straighttest(drive, duration, test_scale, turntime):
    turntime = 2 #tested value for how long it takes to turn 180
    #go straight and back test
    for x in range(1,5):
        straighttestparams(drive, duration, test_scale)
        turnrighttest(drive, turntime, test_scale)
        straighttestparams(drive, duration, test_scale)
        turnrighttest(drive, turntime, test_scale)

def straightspeed(drive, duration, test_scale, turntime):
    #go straight and back test, straight speed
    for x in range(10):
        scale = (x+1)/10
        straighttestparams(drive, duration, scale)
        turnrighttest(drive, turntime, test_scale)
        straighttestparams(drive, duration, scale)
        turnrighttest(drive, turntime, test_scale)

if __name__ == '__main__':
    main()
