from Experimentalist.Core import Audio, Action
import numpy as np


class Loop(Action):
    """
    Looping sound. Sound will be divided in half, then parts will overlap.
    """

    def __init__(self) -> None:
        super().__init__("Loop")
        self.peak = 0.5

    def process(self, audio: Audio) -> None:
        loop_point = int(audio.count * self.peak)
        part1 = audio.frames[:loop_point, :]
        part2 = audio.frames[-loop_point:, :]
        audio.frames = 0.5 * part1 + 0.5 * part2
