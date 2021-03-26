from robot import Robot
from models import Arduino, Drive, KerberosSDR, SpeedController
from constants import *
import time

class ManualTest:
    def __init__(self, drive: Drive, radio: KerberosSDR, arduino: Arduino):
        self.arduino = Arduino()
        self.thrusters = SpeedController(arduino)
        self.drive = Drive(thrusters)
        #imu = Imu()
        self.radio = KerberosSDR()

        models = initialize()
        self.robot = Robot(*models)   
        self.test_scale = 0.1
    
        
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

    def returntime():
        return time.time

        

    def turntest():
        #turnrighttest and turnlefttest
        for y in range(10):
            scale = (y+1)/10
            for x in range(1, 5):
                self.robot.run(turnrighttest(x, scale))
                self.robot.run(turnlefttest(x, scale))

    def straighttest():
        turntime = 2 #tested value for how long it takes to turn 180
        #go straight and back test
        for x in range(1,5):
            self.robot.run(straighttest(duration, test_scale))
            self.robot.run(turnrighttest(turntime, test_scale))
            self.robot.run(straighttest(duration, test_scale))

    def straightspeed():
        #go straight and back test, straight speed
        for x in range(10):
            scale = (x+1)/10
            self.robot.run(straighttest(3, scale))
            self.robot.run(turnrighttest(turntime, test_scale))
            self.robot.run(straighttest(3, scale))
