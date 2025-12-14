from Experimentalist.Core import Audio, Action
from Experimentalist.Actions import Mix
import numpy as np
import random as r


class Flashback(Action):

    def __init__(self, excerpt_duration: float = 1.0, start: float = 0.0, target: float = 0.0, cut: bool = False, mix: bool = False) -> None:
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
        cut : bool
            Determines if excerpt will be cut or copied from its place.
        mix : bool
            Determines if excerpt will be mixed or inserted in target place.
        """
        super().__init__("Flashback")
        self.ed = np.clip(excerpt_duration, 0.2, 4.0)
        self.start = start
        self.target = target
        self.do_cut = cut
        self.do_mix = mix

    def process(self, audio: Audio) -> None:

        excerpt = audio.get_excerpt(self.start, self.ed, self.do_cut)

        if self.do_mix:
            self.log.write("Mix")
            mixer = Mix(audio, self.target)
            audio = mixer.process(excerpt)
        else:
            self.log.write("Insert")
            target = np.round(self.target * audio.sample_rate).astype(np.int64)
            audio.frames = np.concatenate((audio.frames[:target], excerpt.frames, audio.frames[target:]))
