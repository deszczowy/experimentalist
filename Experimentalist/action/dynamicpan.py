from Experimentalist.Core import Action
import numpy as np

class DynamicPan(Action):

    def __init__(self, phase : float = 1.0):
        super().__init__("Dynamic Pan")
        self.phase = np.clip(phase, 0.1, 10.0)
    
    def process(self, audio, sample_rate):
        super().process(audio, sample_rate)
        frames = int(self.phase * sample_rate)

        points = np.linspace(0, 2 * np.pi, frames)
        left = self._one(points)
        right = self._two(points)

        channels = audio.T
        channels[0] = self._apply(channels[0], left)
        channels[1] = self._apply(channels[1], right)
        return channels.T

    def _one(self, x):
        return (np.sin(x) + 1) / 2

    def _two(self, x):
        return (np.sin(x + np.pi) + 1) / 2

    def _apply(self, arr, coefs):
        values = []
        i = 0
        length = len(coefs)

        for x in arr:

            if i == length:
                i = 0
            
            values.append(x * coefs[i])
            i += 1
        return values