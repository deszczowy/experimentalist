from Experimentalist.Core import Action
import numpy as np


class Revert(Action):

    def __init__(self) -> None:
        super().__init__("Revert")

    def process(self, audio: np.ndarray, sample_rate: float) -> np.ndarray:
        super().process(audio, sample_rate)
        return np.flip(audio)
