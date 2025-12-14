from Experimentalist.Core import Audio, Action
from Experimentalist.Actions import Mix, VolumeChange
import numpy as np


class Echo(Action):
    """
    Adding echo to audio.

    Parameters
    ----------
    repeat_interval : float
        Echo will repeat itself in this interval. Value in seconds, from a [0.1, 5.0] range. Default is 1.0 second.
    decay_rate : float
        This indicates how fast the echo will dissolve. Value from [0.1, 0.99] range. Lower the value the echo will stay longer. Default is 0.6.
    clip_to_original_length : bool
        If true, the sound will lengthen until the echo naturally fades away. Default is False, so sound will be cut.
    """

    def __init__(
            self,
            repeat_interval: float = 1.0,
            decay_rate: float = 0.6,
            clip_to_original_length: bool = False
            ) -> None:
        super().__init__("Echo")
        self.interval = np.clip(repeat_interval, 0.1, 5.0)
        self.decay = np.clip(decay_rate, 0.1, 0.99)
        self.clip = clip_to_original_length

    def process(self, audio: Audio) -> None:
        print(audio)
        copy = audio.copy()
        print(copy)
        mixer = Mix(audio, self.interval, self.clip)
        vol = VolumeChange(self.decay)
        iteration = 1

        while iteration < 5:
            vol.process(copy)
            mixer.process(copy)
            iteration += 1
            mixer.setOffset(iteration * self.interval)
