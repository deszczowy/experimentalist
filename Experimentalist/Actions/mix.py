from Experimentalist.Core import Audio, Action
import numpy as np


class Mix(Action):
    """
    Mixing. Action is initialized with base sound in which other sound layers can be mixed.

    Parameters
    ----------

    base_audio : Audio
        Base sound layer for mixing.

    offset : float
        Another layer can be mixed starting from every moment of a base sound. Value in seconds. Default is 0.0 which is a base sound beginning.

    clip : bool
        Indicates if mixed sound sholud be clip to the base sound length. Default is False, so the mixed sound will always be fully heard.
    """

    def __init__(
            self,
            base_audio: Audio,
            offset: float = 0.0,
            clip: bool = False
            ) -> None:
        super().__init__("Mix")
        self.base = base_audio
        self.setOffset(offset)
        self.clip = clip

    def process(self, audio: Audio) -> None:
        """
        Mixing process. Provided audio will be mixed into base_audio layer.
        """

        # Offset is provided in seconds, so we need the exact number of frames to be skiped.
        offset_cnt = int(self.offset * self.base.sample_rate)

        # No clipping means we have to extend base sound if needed
        if self.clip is False:

            # Computing the last frame of mixed sound
            new_length = offset_cnt + audio.count  # in frames

            if new_length > self.base.count:
                # If mixed sound ends after the base level resize base level
                self.base.resize(new_length)

        # Clipping means that mixed sound should be shortend if needed
        if self.clip is True:
            new_length = min(audio.count, self.base.count - offset_cnt)
            if new_length < audio.count:
                audio.resize(new_length)

        # Actual mixing
        for i in range(0, audio.count):
            self.base.frames[i + offset_cnt] = self.base.frames[i + offset_cnt] + 0.5 * audio.frames[i] # todo : coeficient? low volume? check

    def result(self) -> Audio:
        return self.base

    def setOffset(self, value: float) -> None:
        val = value
        if value < 0.0:
            val = 0.0
        if value > self.base.duration:
            val = self.base.duration

        self.offset = val
