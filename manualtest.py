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
    
    
def turnrighttest(duration, scale):
    self.drive.tank_drive(0.5, 0, scale)
    #self.drive.tank_drive(1, 0.2473, scale)
    #self.drive.tank_drive(1, 0.6, scale)
    #self.drive.tank_drive(1, 0.8124, scale)
    #self.drive.tank_drive(1, 0.9156, scale)
    #self.drive.tank_drive(1, 0.9572, scale)

    time.sleep(duration)
    self.drive.tank_drive(0, 0, scale)
    time.sleep(3)

def turnlefttest(duration, scale):
    self.drive.tank_drive(0, 0.5, scale)
    #self.drive.tank_drive(0.2473, 1, scale)
    #self.drive.tank_drive(0.6, 1, scale)        
    #self.drive.tank_drive(0.8124, 1, scale)
    #self.drive.tank_drive(0.9156, 1, scale)        
    #self.drive.tank_drive(0.9572, 1, scale)
    time.sleep(duration)
    self.drive.tank_drive(0, 0, scale)
    time.sleep(3)

def straighttest(duration, scale):
    self.drive.tank-drive(1, 1, scale)
    time.sleep(duration)
    self.drive.tank_drive(0, 0, scale)
    time.sleep(3)


    

def manualtest():
    models = initialize()

    robot = Robot(*models)
    
    test_scale = 0.1

    #turnrighttest and turnlefttest
    for x in range(1, 5):
        robot.run(turnrighttest(x, test_scale))
        #robot.run(turnlefttest(x))

    
    #go straight and back test
    '''
    turntime = 2 #tested value for how long it takes to turn 180

    for x in range(1,5):
        robot.run(straighttest(duration, test_scale))
        robot.run(turnrighttest(turntime, test_scale))
        robot.run(straighttest(duration, test_scale))
    '''



if __name__ == "__manualtest__":
    manualtest()