from Experimentalist.Core import Action
import librosa
import numpy as np


class Stretch(Action):

    def __init__(self, factor: float = 0.7) -> None:
        super().__init__("Stretch")
        self.factor = np.clip(factor, 0.51, 2)
        self._computeFactor()

    def process(self, audio: np.ndarray, sample_rate: float) -> np.ndarray:
        super().process(audio, sample_rate)

        # We are using Librosa for this one, and Librosa has different approach
        # to storing audio data
        signal = audio.T
        channels = []

        for channel in signal:
            resampled = librosa.resample(
                channel,
                orig_sr=sample_rate,
                target_sr=int(sample_rate * self.factor))
            channels.append(resampled)
        new_audio = np.array(channels)

        # Back on track
        audio = new_audio.T
        return audio

    def _computeFactor(self) -> None:
        if self.factor < 1:
            self.factor = ((-2) * self.factor) + 3
        else:
            self.factor = ((-0.5 * self.factor) + 1.5)
        self.log.write(f"Multiplier {self.factor}")
