from Experimentalist.Core import Audio, Action
from Experimentalist.Actions import Mix, VolumeChange
import numpy as np


class Echo(Action):

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
        super().process(audio)

        copy = audio.copy()
        mixer = Mix(audio, self.interval, self.clip)
        vol = VolumeChange(self.decay)
        iteration = 1

        while iteration < 5:
            copy = vol.process(copy)
            mixer.process(copy)
            iteration += 1
            mixer.setOffset(iteration * self.interval)

        _ = mixer.result()
