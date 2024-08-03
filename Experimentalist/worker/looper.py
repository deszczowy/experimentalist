from Experimentalist.Actions import Fade, Loop
from Experimentalist.Core import Worker

class Looper(Worker):

    def __init__(self, filePath, maxDuration : float = 10):
        super().__init__(filePath, "Looper")
        self.maxDuration = maxDuration
        
    def process(self):

        if self.length > self.maxDuration:
            while True:
                self.audio = Fade().process(self.audio, self.sample_rate)
                self.audio = Loop().process(self.audio, self.sample_rate)
                super().process()
            
                if self.length < self.maxDuration:
                    break
        
