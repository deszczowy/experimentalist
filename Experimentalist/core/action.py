from numpy import ndarray

from Experimentalist.Core import Log

class Action:
    
    def __init__(self, withName):
        self.length = 0
        self.log = Log(withName)
    
    def process(self, audio, sample_rate):
        self.length = len(audio[:, 0])
        return audio