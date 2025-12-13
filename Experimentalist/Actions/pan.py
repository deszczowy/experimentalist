from Experimentalist.Core import Audio, Action
import numpy as np


class Pan(Action):
    """
    Panning sound.

    Parameters
    ----------
    balance : float
        Balance of pan, number from [0,1] range, where 0 means whole sound will be contained in left channel, and 1 means all sound will be in right channel.
        Default is 0.5 which means sound will spread evenly in both channels.
    """
    def __init__(self, balance: float = 0.5) -> None:
        # Balance: 0 (left) to 1 (right), with 0.5 being center
        self.balance = np.clip(balance, 0, 1)

    def process(self, audio: Audio) -> None:
        # Pan law adjustment: -3dB at center
        center_attenuation = np.sqrt(1/2)

        # Calculate gains for channels
        left_gain = np.cos(self.balance * np.pi / 2) * center_attenuation
        right_gain = np.sin(self.balance * np.pi / 2) * center_attenuation

        # Apply calculated gains to the audio channels
        audio.frames[:, 0] *= left_gain  # Apply gain to the left channel
        audio.frames[:, 1] *= right_gain  # Apply gain to the right channel
