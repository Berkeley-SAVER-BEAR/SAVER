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
    drive.tank_drive(0.5, 0, scale)
    #self.drive.tank_drive(1, 0.2473, scale)
    #self.drive.tank_drive(1, 0.6, scale)
    #self.drive.tank_drive(1, 0.8124, scale)
    #self.drive.tank_drive(1, 0.9156, scale)
    #self.drive.tank_drive(1, 0.9572, scale)

    time.sleep(duration)
    drive.tank_drive(0, 0, scale)
    time.sleep(3)

def turnlefttest(duration, scale):
    drive.tank_drive(0, 0.5, scale)
    #self.drive.tank_drive(0.2473, 1, scale)
    #self.drive.tank_drive(0.6, 1, scale)        
    #self.drive.tank_drive(0.8124, 1, scale)
    #self.drive.tank_drive(0.9156, 1, scale)        
    #self.drive.tank_drive(0.9572, 1, scale)
    time.sleep(duration)
    drive.tank_drive(0, 0, scale)
    time.sleep(3)

def straighttest(duration, scale):
    drive.tank-drive(1, 1, scale)
    time.sleep(duration)
    drive.tank_drive(0, 0, scale)
    time.sleep(3)

def returntime():
    return time.time

    

def manualtest():
    models = initialize()

    robot = Robot(*models)
    
    test_scale = 0.1

    #turnrighttest and turnlefttest
    for y in range(10):
        scale = (y+1)/10
        for x in range(1, 5):
            robot.run(turnrighttest(x, scale))
            robot.run(turnlefttest(x, scale))

    turntime = 2 #tested value for how long it takes to turn 180

    #go straight and back test
    '''
    for x in range(1,5):
        robot.run(straighttest(duration, test_scale))
        robot.run(turnrighttest(turntime, test_scale))
        robot.run(straighttest(duration, test_scale))
    '''

    #go straight and back test, straight speed
    '''
    for x in range(10):
        scale = (x+1)/10
        robot.run(straighttest(3, scale))
        robot.run(turnrighttest(turntime, test_scale))
        robot.run(straighttest(3, scale))
    '''

    




if __name__ == "__main__":
    manualtest()
