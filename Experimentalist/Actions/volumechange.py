from Experimentalist.Core import Action
import numpy as np


class VolumeChange(Action):

    def __init__(self, factor: float = 1.0) -> None:
        super().__init__("Volume")
        self.factor = np.clip(factor, 0.0, 2.0)

    def process(self, audio: np.ndarray, sample_rate: float) -> np.ndarray:
        audio[:, 0] *= self.factor
        audio[:, 1] *= self.factor
        return audio
