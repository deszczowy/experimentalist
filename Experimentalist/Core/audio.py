import numpy as np
import soundfile as sf

class Audio:

    def __init__(self, path: str = None) -> None:
        self._initialize()
        if path is not None:
            self.load(path)

    def load(self, path : str) -> None:
        self.frames, self.sample_rate = sf.read(path)

        self._compute_duration()
        self._compute_channels()

        if len(self.frames) > 0:
            self.path = path

    def update_parameters(self) -> None:
        self._compute_duration()

    def _initialize(self) -> None:
        self.path = ""
        self.channels = 2
        self.duration = 0.001
        self.sample_rate = 44100
        self.frames = np.zeros((int(self.duration * self.sample_rate), self.channels), dtype='float32')

    def _compute_duration(self) -> None:
        self.duration = len(self.frames) / self.sample_rate  # length in seconds

    def _compute_channels(self) -> None:
        if self.frames.ndim == 1:
            self.channels = 1
        else:
            self.channels = self.frames.shape[1]


