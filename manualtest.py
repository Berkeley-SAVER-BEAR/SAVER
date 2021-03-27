from robot import Robot
from models import Arduino, Drive, KerberosSDR, SpeedController
from constants import *
import time

TEST_SCALE = 0.1
DURATION = 3
TURNTIME = 2

class ManualTest:
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
        #drive, radio, arduino = initialize()
        #robot = Robot(drive, radio, arduino)
        #test_scale = 0.1
        #duration = 3
        #turntime = 2

        #for i in range(8):
        #    self.drive.tank_drive(0, 0, test_scale)

        #uncomment depending on what test we want

        #turnrighttest(duration, test_scale)
        #turnlefttest(duration, test_scale)
        #straighttestparams(duration, test_scale)
        #turntest()
        #straighttest(duration, test_scale, turntime)
        #straightspeed(duration, test_scale, turntime)
        
        # for timing purposes
        #t = returntime()
        #print(time.asctime(time.localtime(t)))

    def turnrighttest(self, duration=DURATION, scale=TEST_SCALE):
        self.drive.tank_drive(0, 0, scale)
        time.sleep(duration)
        self.drive.tank_drive(0.5, 0, scale)
        #self.drive.tank_drive(1, 0.2473, scale)
        #self.drive.tank_drive(1, 0.6, scale)
        #self.drive.tank_drive(1, 0.8124, scale)
        #self.drive.tank_drive(1, 0.9156, scale)
        #self.drive.tank_drive(1, 0.9572, scale)

        time.sleep(duration)
        self.drive.tank_drive(0, 0, scale)
        time.sleep(3)

    def turnlefttest(self, duration=DURATION, scale=TEST_SCALE):
        self.drive.tank_drive(0, 0, scale)
        time.sleep(duration)
        self.drive.tank_drive(0, 0.5, scale)
        #self.drive.tank_drive(0.2473, 1, scale)
        #self.drive.tank_drive(0.6, 1, scale)        
        #self.drive.tank_drive(0.8124, 1, scale)
        #self.drive.tank_drive(0.9156, 1, scale)        
        #self.drive.tank_drive(0.9572, 1, scale)
        time.sleep(duration)
        self.drive.tank_drive(0, 0, scale)
        time.sleep(3)

    def straighttestparams(self, duration=DURATION, scale=TEST_SCALE):
        self.drive.tank_drive(0, 0, scale)
        time.sleep(duration)
        self.drive.tank_drive(1, 1, scale)
        time.sleep(duration)
        self.drive.tank_drive(0, 0, scale)
        time.sleep(3)

    def returntime(self):
        return time.time()

    def stop(self):
        for i in range(8):
            self.drive.tank_drive(0, 0, 0)

    def turntest(self):
        #turnrighttest and turnlefttest
        for y in range(10):
            scale = (y+1)/10
            for x in range(1, 5):
                self.turnrighttest(x, scale)
                self.turnlefttest(x, scale)

    def straighttest(self):
        #turntime = 2 #tested value for how long it takes to turn 180
        #go straight and back test
        for x in range(1,5):
            self.straighttestparams(DURATION, TEST_SCALE)
            self.turnrighttest(TURNTIME, TEST_SCALE)
            self.straighttestparams(DURATION, TEST_SCALE)
            self.turnrighttest(TURNTIME, TEST_SCALE)

    def straightspeed(self):
        #go straight and back test, straight speed
        for x in range(10):
            scale = (x+1)/10
            self.straighttestparams(DURATION, scale)
            self.turnrighttest(TURNTIME, TEST_SCALE)
            self.straighttestparams(DURATION, scale)
            self.turnrighttest(TURNTIME, TEST_SCALE)

#if __name__ == '__main__':
#    main()
