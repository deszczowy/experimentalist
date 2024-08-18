from Experimentalist.Core import Log
import numpy as np


class Action:

    def __init__(self, withName: str) -> None:
        self.length = 0
        self.log = Log(withName)

    def process(self, audio: np.ndarray, sample_rate: float) -> np.ndarray:
        self.length = len(audio[:, 0])
        return audio
