from Experimentalist.Core import Audio, Action
import numpy as np


class Fade(Action):

    def __init__(self, peak_position: float = 0.5) -> None:
        super().__init__("Fade")
        self.peak = np.clip(peak_position, 0, 1)

    def process(self, audio: Audio) -> None:
        peak_point = int(audio.count * self.peak)

        if peak_point == 0:
            peak_point += 1
        if peak_point == audio.count:
            peak_point -= 1

        coef1 = 1 / peak_point  # fade in
        coef2 = 1 / (audio.count - peak_point)  # fade out

        for i in range(0, peak_point - 1):
            audio.frames[i, 0] = audio.frames[i, 0] * coef1 * i
            audio.frames[i, 1] = audio.frames[i, 1] * coef1 * i

        for i in range(peak_point, audio.count):
            audio.frames[i, 0] = audio.frames[i, 0] * coef2 * (audio.count - i)
            audio.frames[i, 1] = audio.frames[i, 1] * coef2 * (audio.count - i)
