from Experimentalist.Actions import Fade, Loop, Stretch
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
        
class Drone(Worker):

    def __init__(self, filePath, factor : float = 0.9, maxDuration : float = 10):
        super().__init__(filePath, "Drone")
        self.maxDuration = maxDuration
        self.factor = factor

    def process(self):
        while True:
            self.audio = Stretch(self.factor).process(self.audio, self.sample_rate)
            self.audio = Fade().process(self.audio, self.sample_rate)
            self.audio = Loop().process(self.audio, self.sample_rate)
            super().process()
            self.log.write(f"Loop length {self.length}")

            if self.length < self.maxDuration:
                break