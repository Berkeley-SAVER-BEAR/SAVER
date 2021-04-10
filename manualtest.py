from robot import Robot
from models import Arduino, Drive, KerberosSDR, SpeedController
from constants import *
import time

TEST_SCALE = 0.7
DURATION = 1
TURNTIME = 2


#class LogTest():
#
#    def __init__(self, test_name, initial_data=None):
#        self.filename = test_name + time.time()
#        self.add(initial_data)
#
#    def add(self, string):
#        file = open("log/" + self.filename, 'a')
#        file.write(string + "\n")
#        file.close()
#
#    def print(self):
#        file = open("log/" + self.filename, 'r')
#        print(file.read())
#
#
#EULER_SPIN_LOG = LogTest(
#    "euler",
#    "Testing to find which value of the tuple represents spin in the x-y plane")


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

    def turn_right_test(self, duration=DURATION, scale=TEST_SCALE):
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

    def turn_left_test(self, duration=DURATION, scale=TEST_SCALE):
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

    def turn_test(self):
        #turn_right_test() and turn_left_test()
        for y in range(10):
            scale = (y+1)/10
            for x in range(1, 5):
                self.turnrighttest(x, scale)
                self.turnlefttest(x, scale)

    def straight_test_params(self, duration=DURATION, scale=TEST_SCALE):
        self.drive.tank_drive(0, 0, scale)
        time.sleep(duration)
        val = int(scale*10)
        for i in range(val):
            x = i / 10
            self.drive.tank_drive(1,1,x)
            time.sleep(duration)
        #self.drive.tank_drive(1, 1, scale-0.2)
        #time.sleep(duration)
        #self.drive.tank_drive(1, 1, scale-0.1)
        #time.sleep(duration)
        #self.drive.tank_drive(1, 1, scale)
        #time.sleep(duration)
        #self.drive.tank_drive(0, 0, scale)
        #time.sleep(3)

    def return_time(self):
        return time.time()

    def stop(self):
        for i in range(8):
            self.drive.tank_drive(0, 0, 0)

    def reverse(self, duration=DURATION, scale=TEST_SCALE):
        self.drive.tank_drive(0, 0, scale)
        time.sleep(duration)
        val = int(scale*10)
        for i in range(val):
            x = i / 10
            self.drive.tank_drive(1,-1,x)
            time.sleep(duration)

    def straight_test(self):
        # turntime = 2 #tested value for how long it takes to turn 180
        # go straight and back test
        for x in range(1, 5):
            self.straight_test_params(DURATION, TEST_SCALE)
            self.turn_right_test(TURNTIME, TEST_SCALE)
            self.straight_test_params(DURATION, TEST_SCALE)
            self.turn_right_test(TURNTIME, TEST_SCALE)

    def straight_speed(self):
        # go straight and back test, straight speed
        for x in range(10):
            scale = (x+1)/10
            self.straight_test_params(DURATION, scale)
            self.turn_right_test(TURNTIME, TEST_SCALE)
            self.straight_test_params(DURATION, scale)
            self.turn_right_test(TURNTIME, TEST_SCALE)

    def dead_spin_test(self,
                       direction="left",
                       duration=10,
                       iteration=1,
                       speed=0,
                       func=None,
                       func_interval=0.2):
        STOP_DURATION = 5

        self.drive.tank_drive(0, 0, TEST_SCALE)
        time.sleep(STOP_DURATION)

        for i in range(iteration):
            self.drive.tank_drive(0.5, 0, TEST_SCALE)
            for t in range(duration / func_interval):
                func()
                time.sleep(func_interval)
            self.drive.tank_drive(0, 0, TEST_SCALE)
            time.sleep(STOP_DURATION)

    def euler_angle_test(self, iteration=1, func_interval=0.2):
        dead_spin_test(iteration=iteration, func_interval=func_interval)

    def dump_euler_angles(self):
        imu = Imu()
        EULER_SPIN_LOG.add(str(imu.get_euler_angles()))
