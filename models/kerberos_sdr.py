from random import randrange
from time import time

class KerberosSDR:

    # For testing
    latest_DOA_timestamp = None
    
    # Cache last DOA value
    latest_DOA = None

    ##########################################################
    # PRIVATE VARIABLES AND FUNCTIONS
    ##########################################################

    # TODO: Determine if default should be scan() or 121.5 ... leaving at 136 for testing
    def __init__(self, frequency=None):

        # 108 MHz: For Testing - This is the closest lower-bound legal frequency found in transceivers.
        if(frequency == 108 or frequency == "test_lower"):
            self._set_frequency(108)

        # 108 MHz: For Testing - This is the closest upper-bound legal frequency found in transceivers.
        elif(frequency == 136 or frequency == "test_upper"):
            self._set_frequency(136)

        # 121.5 MHz: International Aeronautical Emergency Frequency.
        elif(frequency == 121.5 or frequency == "IAEF"):
            self._set_frequency(121.5)

        # 156.8 MHz: International Maritime Distress, Calling and Safety Frequency.
        elif(frequency == 156.8 or frequency == "IMD"):
            self._set_frequency(243)

        # 243.0 MHz: NATO Combined Distress and Emergency Frequency.
        elif(frequency == 243 or frequency == "NATO"):
            self._set_frequency(243)

        # 406.0 MHz: Emergency Position Indicating Locator Beacon (EPIRB).
        elif(frequency == 406 or frequency == "EPIRB"):
            self._set_frequency(406)

        # Else Scan For Known Frequency
        else:
            self._set_frequency(self._scan_for_frequency())

    
    def _set_frequency(self, frequency):
        # TODO: Load a settings file
        pass

    
    def _scan_for_frequency(self):
        # TODO: Load settings files one by one, calibrate, and check for DOA hit. Return best fit frequency if found.
        return 136

    
    ##########################################################
    # PUBLIC FUNCTION(S)
    ##########################################################

    def get_DOA(self, type="random"):
        """Primary and possibly only public function for this class. 
        
        Returns the calculated 'Direction of Arrival' of our anticipated signal. 
        This return value will be an integer indicating degrees in relation to current direction of travel ranging between 0 and 359.
        
        As of now, we believe this number will update approximateley once every second, but this could change. Therefore, we will ensure that excessive polling via this does not hinder performance as we will simply return cached values when applicable.

        Additionally, you will be able to use the optional parameter to return real or dummy data.

        NOTE: Until this note is removed, this function will only return dummy data. Currently, it is simply random dummy data by default.
        """

        # For testing, mimic 1 second buffer between DOA changes by returning cached value until at least a second lapses
        if(int(time()) == self.latest_DOA_timestamp):
            return self.latest_DOA
        
        # Set latest timestamp to current seconds in UNIX time
        self.latest_DOA_timestamp = int(time())

        # TODO: Return something more useful with alternate parameters
        if(True or type == "random"):
            self.latest_DOA = randrange(0,360,1)
            return self.latest_DOA

    

    


    