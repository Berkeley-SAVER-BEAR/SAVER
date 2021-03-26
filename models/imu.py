# Need to enable i2c slowdown on Raspberry Pi device tree overlay
from board import *
import busio
import adafruit_bno055 as IMU

#step 1. Setup imu and get readings going.
#Step 2. Find initial orientations, and set that equal to 0
#Step 3. Integeration: Position x,y,z, Velocity x,y,z Accleration x,y,z
#Step 4. Integration: Euler Angles. Theta, Theta Dot, Theta DoubleDot (x,y,z)
#Step 5. Calibration, fraction of input

class Imu:
    def __init__(self):
        i2c = busio.I2C(SCL,SDA)
        self.sensor = IMU.BNO055_I2C(i2c)

    def get_acceleration(self):
        """Return 3-tuple of X, Y, Z axis accelerometer values in m/s^2."""
        return self.sensor.acceleration

    def get_gyro(self):
        """"Returns 3-tuple of X, Y, Z axis gyroscope values in rad/s."""
        return self.sensor.gyro

    def get_euler_angles(self):
        """Returns 3-tuple of orientation Euler angle values."""
        return self.sensor.euler

    def get_quaternion(self):
        """Returns 4-tuple of orientation quaternion values."""
        return self.sensor.quaternion

    def get_linear_acceleration(self):
        """Returns 3-tuple of X, Y, Z linear acceleration values (without effect of gravity) in m/s^2."""
        return self.sensor.linear_acceleration

    def get_gravity(self):
        """Returns 3-tuple of X, Y, Z gravity acceleration values (without the effect of linear acceleration)
        in m/s^2."""
        return self.sensor.gravity

