import smbus 

class Arduino:

    def __init__(self):
        # Slave Addresses for Arduinos 
        self.SlaveAddress = "fill with arduino address" # I2C Address of Arduino

        # Create the I2C bus 
        self.I2Cbus = smbus.SMBus(1) 

    def sendToESC(self, bytesToSend):

        self.I2Cbus.write_i2c_block_data(self.SlaveAddress, "Fill register address", bytesToSend)
