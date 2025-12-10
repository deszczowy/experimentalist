from Experimentalist.Core import Audio, Action
import numpy as np


class VolumeChange(Action):

    """
    Changing sound volume by a given factor.
    """


    def __init__(self, factor: float = 1.0) -> None:
        """
        Parameters
        ----------

        factor : float
            Number from [0.2 .. 2.0] range. Default is 1.0, which indicates no volume change.
        """
        super().__init__("Volume")
        self.factor = np.clip(factor, 0.0, 2.0)

    def process(self, audio: Audio) -> None:
        print(audio)
        print(audio.channels)
        print(audio.frames)
        if audio.channels == 1:
            audio.frames[:] *= self.factor
        else:
            audio.frames[:, 0] *= self.factor
            audio.frames[:, 1] *= self.factor
