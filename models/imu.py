# Need to enable i2c slowdown on Raspberry Pi device tree overlay
# import board
# import busio
# import adafruit_bno055 as IMU


# class Imu:

#     def __init__(self):
#         i2c = busio.I2C(board.SCL, board.SDA)
#         self.sensor = IMU.BNO055_I2C(i2c)

#     def get_acceleration(self):
#         """Return 3-tuple of X, Y, Z axis accelerometer values in m/s^2."""
#         return self.sensor.acceleration

#     def get_gyro(self):
#         """"Returns 3-tuple of X, Y, Z axis gyroscope values in rad/s."""
#         return self.sensor.gyro

#     def get_euler_angles(self):
#         """Returns 3-tuple of orientation Euler angle values."""
#         return self.sensor.euler

#     def get_quaternion(self):
#         """Returns 4-tuple of orientation quaternion values."""
#         return self.sensor.quaternion

#     def get_linear_acceleration(self):
#         """Returns 3-tuple of X, Y, Z linear acceleration values (without effect of gravity) in m/s^2."""
#         return self.sensor.linear_acceleration

#     def get_gravity(self):
#         """Returns 3-tuple of X, Y, Z gravity acceleration values (without the effect of linear acceleration)
#         in m/s^2."""
#         return self.sensor.gravity
