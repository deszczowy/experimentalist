from Experimentalist.Core import Action
import numpy as np
from pedalboard import Reverb as pbrev


class Reverb(Action):

    def __init__(self, room_size: float = 0.5, dry_wet: float = 0.5, space: float = 0.5) -> None:
        super().__init__("Reverb")
        self.room_size = np.clip(room_size, 0.0, 1.0)
        self.wet = np.clip(dry_wet, 0.0, 1.0)
        self.dry = 1.0 - self.wet
        self.space = np.clip(space, 0.0, 1.0)

    def process(self, audio: np.ndarray, sample_rate: float) -> np.ndarray:
        super().process(audio, sample_rate)
        audio = pbrev(
            room_size=self.room_size,
            damping=0.5,
            wet_level=self.wet,
            dry_level=self.dry,
            width=self.space,
            freeze_mode=0.0).process(audio, sample_rate)
        return audio
