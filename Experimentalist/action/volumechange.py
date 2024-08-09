from Experimentalist.Core import Action
from numpy import clip


class VolumeChange(Action):

    def __init__(self, factor: float = 1.0):
        super().__init__("Volume")
        self.factor = clip(factor, 0.0, 2.0)

    def process(self, audio, sample_rate):
        audio[:, 0] *= self.factor
        audio[:, 1] *= self.factor
        return audio
