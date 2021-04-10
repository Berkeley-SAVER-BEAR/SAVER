from .arduino import Arduino
from .imu import Imu


class SpeedController:

    def __init__(self, arduino: Arduino):
        self.arduino = arduino
        self.thisImu = Imu()

        # set dt to loop time.
        # D means derivative. xD means velocity. xDD means acceleration.

        self.dt = 0.1
        self.t = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.xD = 0
        self.yD = 0
        self.zD = 0
        self.xDD = 0
        self.yDD = 0
        self.zDD = 0
        self.xDDCorr = 0
        self.yDDCorr = 0
        self.zDDCorr = 0

        self.MAX_FORWARD = 2.71
        self.MAX_BACKWARDS = 2.90

        self.MAX_SPEED_FORWARD = 1 #???
        self.MAX_SPEED_BACKWARDS = 1 #??

        #???
        self.totalVelocityError = 0


    #calling thrusttoPwm: pass in level * forward/backward
    def set_speed(self, speed1: float, speed2: float, scale):
        """Runs the thruster at a specified speed between 1 (full speed forward) and -1 (full speed backward)"""
        thrust1, thrust2 = 0, 0
        if speed1 > 0:
            velocity1 = speed1 * scale * self.MAX_SPEED_FORWARD
        else:
            velocity1 = speed1 * scale *self.MAX_SPEED_BACKWARDS
        if speed1 > 0:
            velocity2 = speed2 * scale * self.MAX_SPEED_FORWARD
        else:
            velocity2 = speed2 * scale *self.MAX_SPEED_BACKWARDS
        thrust1 = self.getThrust(velocity1)
        thrust2 = self.getThrust(velocity2)
        self.arduino.send("{0}{1}{2}".format(round(self.thrustToPWM(thrust1)), "|", round(self.thrustToPWM(thrust2))))

    def set_speed2(self, desiredVelocity: float):
        
        thrust1 = self.getThrust(desiredVelocity)
        thrust2 = self.getThrust(desiredVelocity)
        self.arduino.send("{0}{1}{2}".format(round(self.thrustToPWM(thrust1)), "|", round(self.thrustToPWM(thrust2))))

    #Tracks velocity and implements PID control given desired velocity

    def getThrust(self, desiredVelocity):

        #loop this every dt seconds

        acelVector = self.thisImu.get_acceleration()
        self.t = self.t + self.dt

        # when time is less than 2 seconds, make sure drone is steady to correct for sensor biases.
        if self.t < 2:
            self.x = 0
            self.y = 0
            self.z = 0
            self.xD = 0
            self.yD = 0
            self.zD = 0
            #change this to average bias
            self.xDDCorr = acelVector[0]
            self.yDDCorr = acelVector[1]
            self.zDDCorr = acelVector[2]
            self.totalVelocityError = 0
            return 0
        else:
            dt = self.dt
            t = self.t
            x = self.x
            y = self.y
            z = self.z
            xD = self.xD
            yD = self.yD
            zD = self.zD
            xDD = self.xDD
            yDD = self.yDD
            zDD = self.zDD
            xDDCorr = self.xDDCorr
            yDDCorr = self.yDDCorr
            zDDCorr = self.zDDCorr
            totalVelocityError = self.totalVelocityError

            xDD = acelVector[0] - xDDCorr
            yDD = acelVector[1] - yDDCorr
            zDD = acelVector[2] - zDDCorr

            xD = xD + xDD * dt
            yD = yD + yDD * dt
            zD = zD + zDD * dt


            #currentVelocity is undefined
            #velocityError = desiredVelocity - currentVelocity

            currentVelocity = yD
            velocityError = desiredVelocity - currentVelocity

            #should this be below totalvelocityerror?
            self.lastVelocityError = self.totalVelocityError 
            self.totalVelocityError = self.totalVelocityError + velocityError * dt

            slopeVelocityError = (self.lastVelocityError - velocityError)/dt

            x = x + xD * dt
            y = y + yD * dt
            z = z + zD * dt

            # PID controls, first part is P, second is I, last is D
            # Need to optomize constants for PID controls based on tests.

            self.dt = dt
            self.t = t
            self.x = x
            self.y = y
            self.z = z
            self.xD = xD
            self.yD = yD
            self.zD = zD
            self.xDD = xDD
            self.yDD = yDD
            self.zDD = zDD
            self.xDDCorr = xDDCorr
            self.yDDCorr = yDDCorr
            self.zDDCorr = zDDCorr
            self.totalVelocityError = totalVelocityError

            outputThrust = 1000 * (desiredVelocity - currentVelocity) + 200 * totalVelocityError + 300 * slopeVelocityError
            return outputThrust

    def thrustToPWM(self, thrust):
        PWM = 0
        if thrust > 0:
            PWM = -32.289500442873752 * thrust ** 2 + 3.869011829925794 * thrust ** 3 + 162.816482640325944 * thrust + 1537.793648693580053
        else:
            if thrust <= 0: #should this be < rather than <=??
                PWM = 47.581695898375777 * thrust ** 2 + -7.292251741725251 * thrust ** 3 + -199.610465634680764 * thrust + 1460.832024027741454

        if PWM < 1820 and PWM > 1100:
            return PWM
        else:
            print(PWM)
            return 1500
