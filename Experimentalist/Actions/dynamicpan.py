from Experimentalist.Core import Audio, Action
import numpy as np


class DynamicPan(Action):
    """
    After this action sound in stereo audio will go from one channel to another and back in given time interval.
    """

    def __init__(self, phase: float = 1.0, starting_left: bool = True) -> None:
        """
        Parameters
        ----------

        phase : float
            Interval in which  sound will circulate between channels. In seconds. Default 1.0s.
        starting_left : bool
            Indicates if sound starts from left channel. By default it starts from right one.
        """
        super().__init__("Dynamic Pan")
        self.phase = np.clip(phase, 0.1, 10.0)
        self.first_left = starting_left

    def process(self, audio: Audio) -> None:
        frames_count = int(self.phase * audio.sample_rate)

        points = np.linspace(0, 2 * np.pi, frames_count)
        left = self._one(points)
        right = self._two(points)

        channels = audio.frames.T
        if self.first_left is True:
            channels[0] = self._apply(channels[0], left)
            channels[1] = self._apply(channels[1], right)
        else:
            channels[0] = self._apply(channels[0], right)
            channels[1] = self._apply(channels[1], left)

        audio.frames = channels.T

    def _one(self, x: float) -> float:
        return (np.sin(x) + 1) / 2

    def _two(self, x: float) -> float:
        return (np.sin(x + np.pi) + 1) / 2

    def _apply(self, arr: np.ndarray, coefs: np.ndarray) -> np.ndarray:
        values = []
        i = 0
        length = len(coefs)

        for x in arr:

            if i == length:
                i = 0

            values.append(x * coefs[i])
            i += 1
        return values
