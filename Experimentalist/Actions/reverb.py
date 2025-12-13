from Experimentalist.Core import Audio, Action
import numpy as np
from pedalboard import Reverb as pbrev


class Reverb(Action):
    """
    Reverb action.

    Parameters
    ----------

    room_size : float
        Number from a [0, 1] range, where 0 is a small room, and 1.0 is cathedral. Default value is 0.5.

    dry_wet : float
        "Wettness" indicator. Number from [0.0, 1.0] range, where 0.0 means original sound will be fully heard over reverb effect, and 1.0 means that reverb will fully tak over the scene. Default is 0.5.

    space : float
        Number from [0.0, 1.0] range which indicates vastnes of spatial effect. Default is 0.5.
    """

    def __init__(self, room_size: float = 0.5, dry_wet: float = 0.5, space: float = 0.5) -> None:
        super().__init__("Reverb")
        self.room_size = np.clip(room_size, 0.0, 1.0)
        self.wet = np.clip(dry_wet, 0.0, 1.0)
        self.dry = 1.0 - self.wet
        self.space = np.clip(space, 0.0, 1.0)

    def process(self, audio: Audio) -> None:
        audio.frames = pbrev(
            room_size=self.room_size,
            damping=0.5,
            wet_level=self.wet,
            dry_level=self.dry,
            width=self.space,
            freeze_mode=0.0).process(audio.frames, audio.sample_rate)
