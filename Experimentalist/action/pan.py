from numpy import clip, sqrt, sin, cos, pi

from Experimentalist.Core import Action

class Pan(Action):

    def __init__(self, balance=0.5):  # Balance: 0 (left) to 1 (right), with 0.5 being center
        self.balance = clip(balance, 0, 1)

    def process(self, audio, sample_rate):
        # Pan law adjustment: -3dB at center
        center_attenuation = sqrt(1/2)
        
        # Calculate gains for L and R channels using a cosine and sine law for smooth panning
        left_gain = cos(self.balance * pi / 2) * center_attenuation
        right_gain = sin(self.balance * pi / 2) * center_attenuation
        
        # Apply calculated gains to the audio channels
        audio[:, 0] *= left_gain  # Apply gain to the left channel
        audio[:, 1] *= right_gain  # Apply gain to the right channel
        return audio