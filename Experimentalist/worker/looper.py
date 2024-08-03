import soundfile as sf
import os

from pedalboard import Limiter
from Experimentalist.Actions import Fade, Loop

class Looper:

    def __init__(self, filePath, maxDuration : float = 10):
        self.path = filePath
        self.maxDuration = maxDuration
        self._read()
        self._computeLength()

    def _read(self):
        self.audio, self.sample_rate = sf.read(self.path)

    def _process(self):
        self.audio = Fade().process(self.audio, self.sample_rate)
        self.audio = Loop().process(self.audio, self.sample_rate)
        self.audio = Limiter(threshold_db=-5.0).process(self.audio, self.sample_rate)
        self._computeLength()
        
    def _computeLength(self):
        self.length = len(self.audio) / self.sample_rate # length in seconds
        print(self.length)
    
    def _nameOutputFile(self, outputPath, runId):
        name, extension = os.path.splitext(self.path)
        self.output = os.path.join(outputPath, "")
        self.output = f"{self.output}{name}-{runId}{extension}"
    
    def _save(self):
        with sf.SoundFile(
            self.output,
            'w',
            samplerate = self.sample_rate,
            channels = len(self.audio.shape)
        ) as f:
            f.write(self.audio)

    def apply(self, runId, outputPath):
        self._nameOutputFile(outputPath, runId)

        if self.length > self.maxDuration:
            while True:
                self._process()
            
                if self.length < self.maxDuration:
                    break
        self._save()