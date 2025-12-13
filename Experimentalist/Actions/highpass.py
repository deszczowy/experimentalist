from Experimentalist.Core import Audio, Action
import numpy as np
from pedalboard import HighpassFilter


class HighPass(Action):
    """
    High pass filter action.

    Parameters
    ----------

    cutoff_hz: float
        Filter will pass frequencies above this value. Default is 10kHz.

    """

    def __init__(self, cutoff_hz: float = 10000) -> None:
        super().__init__("High Pass")
        self.cutoff = cutoff_hz

    def process(self, audio: Audio) -> None:
        audio.frames = HighpassFilter(
            cutoff_frequency_hz=self.cutoff).process(audio.frames, audio.sample_rate)
