from .arduino import Arduino
class SpeedController:

    def __init__(self, arduino: Arduino):
        self.arduino = arduino

    # gets and return the PWM based on inputs between -1 and 1
    MAX_FORWARD = 2.71
    MAX_BACKWARDS = 2.90


    def set_speed(self, speed1: float, speed2: float, scale):
        """Runs the thruster at a specified speed between 1 (full speed forward) and -1 (full speed backward)"""
        #self.arduino.send("{0}{1}".format(self.port, self.getPWM(speed)))
        self.arduino.send("{0}{1}{2}".format(round(self.getPWM(speed1, scale)), "|", round(self.getPWM(speed2, scale))))

    def getPWM(self, level, scale): # level is between -1 to 1 where < 0 means backwards and > 0 means forward.
        # Gets the PWM
        
        level *= scale

        if level < -1 or level > 1:
            return "Incorrect input"

        if level == 0:
            return 1500.00
        elif level > 0:
            return self.thrustToPWM(level * self.MAX_FORWARD) 
        elif level < 0:
            return self.thrustToPWM(level * self.MAX_BACKWARDS)
        
    def thrustToPWM(self, thrust):
        # fitted a polynomial to make it easy to map thrust to pwm
        if thrust > 0:
            return -32.289500442873752 * thrust ** 2 + 3.869011829925794 * thrust ** 3 + 162.816482640325944 * thrust + 1537.793648693580053
        else:
            thrust *= -1
            return 47.581695898375777 * thrust ** 2 + -7.292251741725251 * thrust ** 3 + -199.610465634680764 * thrust + 1460.832024027741454
