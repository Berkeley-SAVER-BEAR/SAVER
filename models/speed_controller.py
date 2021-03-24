from .arduino import Arduino
class SpeedController:

    def __init__(self, arduino: Arduino, port: int):
        self.arduino = arduino
        self.port = port

    # gets and return the PWM based on inputs between -1 and 1
    MAX_FORWARD = 2.71
    MAX_BACKWARDS = 2.90


    def getPWM(self, level): # level is between -1 to 1 where < 0 means backwards and > 0 means forward.
        # Gets the PWM
        if level < -1 or level > 1:
            return "Incorrect input"

        if level == 0:
            return 1500
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
