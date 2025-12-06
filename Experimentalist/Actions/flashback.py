from Experimentalist.Core import Action
from Experimentalist.Actions import Mix
import numpy as np
import random as r


class Flashback(Action):

    def __init__(self, excerpt_duration: float = 1.0, start: float = 0.0, target: float = 0.0, copy: bool = False, mix: bool = False) -> None:
        """
        Creates action for Flashback effect.

        Parameters
        ----------
        excerpt_duration : float
            Duration of flashbacked part. In seconds. Min: 0.2s Max: 4s
        start : float
            Point of time from which excerpt will be taken. In seconds.
        target : float
            Point of time in which excerpt will be placed.
        copy : bool
            Determines if excerpt will be copied or cut from its place.
        mix : bool
            Determines if excerpt will be mixed or inserted in target place.
        """
        super().__init__("Flashback")
        self.ed = np.clip(excerpt_duration, 0.2, 4.0)
        self.start = start
        self.target = target
        self.do_copy = copy
        self.do_mix = mix

    def process(self, audio: np.ndarray, sample_rate: float) -> np.ndarray:
        audio = super().process(audio, sample_rate)
        (excerpt, audio) = self._obtain_excerpt(audio, sample_rate)

        self.log.write("File sample rate = {0}Hz".format(sample_rate))
        self.log.write("File frames count = {0}".format(self.length))

        if self.do_mix:
            self.log.write("Mix")
            mixer = Mix(audio, self.target)
            audio = mixer.process(excerpt, sample_rate)
        else:
            self.log.write("Insert")
            target = np.round(self.target * sample_rate).astype(np.int64)
            audio = np.concatenate((audio[:target], excerpt, audio[target:]))

        return audio

    def _obtain_excerpt(self, audio: np.ndarray, sample_rate: float) -> (np.ndarray, np.ndarray):
        start = np.round(self.start * sample_rate).astype(np.int64)
        length = np.round(self.ed * sample_rate).astype(np.int64)

        self.log.write("Excerpt start index = {0}".format(start))
        self.log.write("Excerpt frames count = {0}".format(length))

        excerpt = audio[start : start + length]

        if self.do_copy is not True:
            audio = np.delete(audio, np.s_[start : start + length], axis=0)

        return (excerpt, audio)
