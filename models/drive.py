from . import SpeedController
import math

class Drive:
    def __init__(self, left_thruster: SpeedController, right_thruster: SpeedController):
        self.left_thruster = left_thruster
        self.right_thruster = right_thruster

    def tank_drive(self, left: float, right: float):
        self.left_thruster.set_speed(left)
        self.right_thruster.set_speed(right)

    def arcade_drive(self, forward: float, turn: float):
        """
        Control robot by forward speed and turn speed, both -1 to 1. 
        Positive turn for clockwise, negative for counterclockwise
        """
        left = forward + turn
        right = forward - turn

        # normalize values to 1 if too big
        scale_factor = max(1, abs(left), abs(right))
        left = round(left/scale_factor , 4)
        right = round(right/scale_factor, 4)

        self.tank_drive(left, right)

    def calculate_speeds (self):
        degree = (round(KerberosSDR.get_DOA(), 4) + 45) %360 - 180
        #if degree <= 5 or degree <= 355:
            #self.tankdrive(1,1)
        if degree <= 90 or degree >= 270:
            angle = round(math.radians(degree), 4)
            forward = round(2 * math.cos(angle), 4)
            turn = round(math.sin(angle) / 2, 4)
            self.arcade_drive(forward, turn)
        elif degree <= 180:
            self.tank_drive(1, -1)        #maybe 1, 0; depends on boat behavior
        else:
            self.tank_drive(-1, 1)

       
        #arduino send: ??