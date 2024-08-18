from Experimentalist.Core import Action
import numpy as np


class Pan(Action):

    def __init__(self, balance: float = 0.5) -> None:
        # Balance: 0 (left) to 1 (right), with 0.5 being center
        self.balance = np.clip(balance, 0, 1)

    def process(self, audio: np.ndarray, sample_rate: float) -> np.ndarray:
        # Pan law adjustment: -3dB at center
        center_attenuation = np.sqrt(1/2)

        # Calculate gains for channels
        left_gain = np.cos(self.balance * np.pi / 2) * center_attenuation
        right_gain = np.sin(self.balance * np.pi / 2) * center_attenuation

        # Apply calculated gains to the audio channels
        audio[:, 0] *= left_gain  # Apply gain to the left channel
        audio[:, 1] *= right_gain  # Apply gain to the right channel
        return audio
