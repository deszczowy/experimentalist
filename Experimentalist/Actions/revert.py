from Experimentalist.Core import Audio, Action
import numpy as np


class Revert(Action):
    """
    Simple revert action.
    """

    def __init__(self) -> None:
        super().__init__("Revert")

    def process(self, audio: Audio) -> None:
        audio.frames = np.flip(audio.frames)
