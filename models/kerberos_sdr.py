
class KerberosSDR:

    def __init__(self, frequency=None):
        #want to write the value to desktop
        self.doa_fname = '/home/pi/Desktop/doa.txt'

    def getDOA(self):
        doa_file = open(self.doa_fname, 'r')
        return doa_file.read()
