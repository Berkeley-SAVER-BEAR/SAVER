from . import Arduino

class SpeedController:

    def __init__(self, arduino: Arduino, port: int):
        self.arduino = arduino
        self.port = port

        self.thrustToPWM = {-10:1100, -9:1140, -8:1180, -7:1220, -6:1260, -5:1300, -4:1340, -3:1380, -2:1420, -1:1460, 
                            0:1500, 1:1540, 2:1580, 3:1620, 4:1660, 5:1700, 6:1740, 7:1780, 8:1820, 9:1860, 10:1900}

    def getPWM(self, level):
        return self.thrustToPWM[level]

    def set_speed(self, speed: float):
        """Runs the thruster at a specified speed between 1 (full speed forward) and -1 (full speed backward)"""
        self.arduino.send("{},{}".format(port, speed)) # TODO: convert speed to correct pwm values