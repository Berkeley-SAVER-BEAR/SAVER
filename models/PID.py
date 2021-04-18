from .arduino import Arduino
import . from imu

thisImu = Imu()

# set dt to loop time.
# D means derivative. xD means velocity. xDD means acceleration.

dt = 0.1
t = 0
x = 0
y = 0
z = 0
xD = 0
yD = 0
zD = 0
xDD = 0
yDD = 0
zDD = 0
xDDCorr = 0
yDDCorr = 0
zDDCorr = 0

class SpeedController:


    #Tracks velocity and implements PID control given desired velocity
        
    def getThrust(self, desiredVelocity):

        #loop this every dt seconds

        acelVector = get_acceleration(self)
        t = t + dt

        # when time is less than 2 seconds, make sure drone is steady to correct for sensor biases.
        if t < 2:
            x = 0
            y = 0
            z = 0
            xD = 0
            yD = 0
            zD = 0
            #change this to average bias
            xDDCorr = acelVector[0]
            yDDCorr = acelVector[1]
            zDDCorr = acelVector[2]
            return 0
        else:
            xDD = acelVector[0] - xDDCorr
            yDD = acelVector[1] - yDDCorr
            zDD = acelVector[2] - zDDCorr

            xD = xD + xDD * dt
            yD = yD + yDD * dt
            zD = zD + zDD * dt

            velocityError = desiredVelocity - currentVelocity
            lastVelocityError = totalVelocityError
            totalVelocityError = totalVelocityError + velocityError * dt
            slopeVelocityError = (lastVelocityError - velocityError)/dt

            x = x + xD * dt
            y = y + yD * dt
            z = z + zD * dt

            # PID controls, first part is P, second is I, last is D
            # Need to optomize constants for PID controls based on tests. 

            outputThrust = 1000 * (desiredVelocity - currentVelocity) + 200 * totalVelocityError + 300 * slopeVelocityError
            return outputThrust

def thrustToPWM(self, thrust):
    PWM = 0
    if thrust > 0:
        PWM = -32.289500442873752 * thrust ** 2 + 3.869011829925794 * thrust ** 3 + 162.816482640325944 * thrust + 1537.793648693580053
    elif thrust <= 0:
        PWM 47.581695898375777 * thrust ** 2 + -7.292251741725251 * thrust ** 3 + -199.610465634680764 * thrust + 1460.832024027741454

    if PWM < 1820 and PWN > 1100:
        return PWM
    else:
        return 1500
