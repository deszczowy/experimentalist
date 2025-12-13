from Experimentalist.Core import Audio, Action
import librosa
import numpy as np


class Stretch(Action):
    """
    Stretching sound.

    Parameters
    ----------

    factor : float
        Indicates a direction and level of stretch. Is a number from [0.51, 2.0] range, where 2.0 means doubling up, and 0.51 is doubling down of sound speed. Delfault is 0.7.
    """

    def __init__(self, factor: float = 0.7) -> None:
        super().__init__("Stretch")
        self.factor = np.clip(factor, 0.51, 2)
        self._computeFactor()

    def process(self, audio: Audio) -> None:

        # We are using Librosa for this one, and Librosa has different approach
        # to storing audio data
        signal = audio.frames.T
        channels = []

        for channel in signal:
            resampled = librosa.resample(
                channel,
                orig_sr=audio.sample_rate,
                target_sr=int(audio.sample_rate * self.factor))
            channels.append(resampled)
        new_audio = np.array(channels)

        # Back on track
        audio.frames = new_audio.T

    def _computeFactor(self) -> None:
        if self.factor < 1:
            self.factor = ((-2) * self.factor) + 3
        else:
            self.factor = ((-0.5 * self.factor) + 1.5)
        self.log.write(f"Multiplier {self.factor}")
