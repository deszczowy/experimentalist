from Experimentalist.Core import Action
import numpy as np


class Loop(Action):

    def __init__(self) -> None:
        super().__init__("Loop")
        self.peak = 0.5

    def process(self, audio: np.ndarray, sample_rate: float) -> np.ndarray:
        super().process(audio, sample_rate)
        loop_point = int(self.length * self.peak)
        part1 = audio[:loop_point, :]
        part2 = audio[-loop_point:, :]
        audio = 0.5 * part1 + 0.5 * part2
        return audio
