from Experimentalist.Core import Action
import numpy as np


class Copy(Action):

    def __init__(self) -> None:
        super().__init__("Copy")

    def process(self, audio: np.ndarray, sample_rate: float) -> np.ndarray:
        return np.ndarray.copy(audio)
