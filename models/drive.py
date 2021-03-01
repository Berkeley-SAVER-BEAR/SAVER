from . import SpeedController

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
        left /= scale_factor
        right /= scale_factor

        self.tank_drive(left, right)