import numpy as np
import soundfile as sf
from pedalboard import Limiter

class Audio:
    """
    This class represents audio record and contains all informations related to sound.

    Fields
    ------
    frames : numpy.nbarray
        Contains table of samples. First axis is a progression of time, second contains samples values for channels.
    sample_rate : int
        Sound sample rate. Default is 44.1kHz
    channels : int
        Contains count of channels in sound (i.e. 2 for stereo). Default is 2.
    path : str
        If audio was loaded from file, here will be a path to this file. Default is `None`
    length : int
        Represents count of samples in sound. Does not update automaticly after `frames` change, you have to call `update_parameters` for this.
    duration : float
        Sound duration in seconds, computed over frames and sample_rate. Does not update automaticly after `frames` change, you have to call `update_parameters` for this.
    """

    def __init__(self, path: str = None) -> None:
        self._initialize()
        if path is not None:
            self.load(path)

    def load(self, path : str) -> None:
        self.frames, self.sample_rate = sf.read(path)

        self._compute_duration()
        self._compute_channels()
        self._compute_length()

        if len(self.frames) > 0:
            self.path = path

    def update_parameters(self) -> None:
        self._compute_duration()
        self._compute_length()

    def normalize(self) -> None:
        """
        Normalizes signal to -5.0db.
        """
        self.frames = Limiter(threshold_db=-5.0).process(
            self.frames,
            self.sample_rate
        )

    def resize(self, new_size: int) -> None:
        self.frames.resize((new_size, self.channels), refcheck=False)
        self.count = new_size

    def copy(self) -> 'Audio':
        """
        Makes a hard copy of self.
        """
        new_audio = Audio()
        new_audio.frames = np.ndarray.copy(self.frames)
        new_audio.sample_rate = self.sample_rate
        new_audio.path = self.path
        new_audio.channels = self.channels
        new_audio.update_parameters()
        return new_audio

    # Private methods

    def _initialize(self) -> None:
        self.path = ""
        self.channels = 2
        self.duration = 0.001
        self.sample_rate = 44100
        self.count = int(self.duration * self.sample_rate)
        self.frames = np.zeros((self.count, self.channels), dtype='float32')

    def _compute_duration(self) -> None:
        self.duration = len(self.frames) / self.sample_rate  # length in seconds

    def _compute_channels(self) -> None:
        if self.frames.ndim == 1:
            self.channels = 1
        else:
            self.channels = self.frames.shape[1]

    def _compute_length(self) -> None:
        self.count = len(self.frames)


