from Experimentalist.Core import Action
import numpy as np


class Mix(Action):

    def __init__(
            self,
            base_audio: np.ndarray,
            offset_seconds: float,
            clip: bool = False
            ) -> None:
        super().__init__("Mix")
        self.base = base_audio
        self.base_length = len(base_audio)
        self.setOffset(offset_seconds)
        self.clip = clip

    def process(self, audio: np.ndarray, sample_rate: float) -> np.ndarray:
        super().process(audio, sample_rate)
        offset = int(self.offset * sample_rate)

        if self.clip is False:
            new_length = offset + self.length  # in frames

            if new_length > self.base_length:
                extra = new_length - self.base_length
                for i in range(0, extra):
                    # silence! to separate action
                    self.base.resize((new_length, 2), refcheck=False)
                self.base_length = len(self.base)

        if self.clip is True:
            self.length = min(self.length, self.base_length - offset)

        for i in range(0, self.length):
            self.base[i + offset] = self.base[i + offset] + 0.5 * audio[i]

        return self.base

    def result(self) -> np.ndarray:
        return self.base

    def setOffset(self, value: float) -> None:
        self.offset = value
