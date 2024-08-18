from Experimentalist.Core import Action
import numpy as np
from pedalboard import LowpassFilter


class LowPass(Action):

    def __init__(self, cutoff_hz: float = 100) -> None:
        super().__init__("Low Pass")
        self.cutoff = cutoff_hz

    def process(self, audio: np.ndarray, sample_rate: float) -> np.ndarray:
        audio = LowpassFilter(
            cutoff_frequency_hz=self.cutoff).process(audio, sample_rate)
        super().process(audio, sample_rate)
        return audio
