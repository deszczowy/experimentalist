from Experimentalist.Core import Audio, Action
import numpy as np
from pedalboard import LowpassFilter


class LowPass(Action):
    """
    Low pass filter action.

    Parameters
    ----------

    cutoff_hz: float
        Filter will pass frequencies below this value. Default is 100Hz.

    """
    def __init__(self, cutoff_hz: float = 100) -> None:
        super().__init__("Low Pass")
        self.cutoff = cutoff_hz

    def process(self, audio: Audio) -> None:
        audio.frames = LowpassFilter(
            cutoff_frequency_hz=self.cutoff).process(audio.frames, audio.sample_rate)
