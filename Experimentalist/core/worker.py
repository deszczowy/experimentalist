import os
import soundfile as sf

from pedalboard import Limiter

from Experimentalist.Core import Log

class Worker:

    def __init__(self, filePath, workerName):
        self.log = Log(workerName)
        self.path = filePath
        self._read()
        self.computeLength()
        self.log.write(f"Data prepared from {filePath}")
    
    def process(self):
        self.normalize()
        self.computeLength()

    def computeLength(self):
        self.length = len(self.audio) / self.sample_rate # length in seconds
    
    def normalize(self):
        self.audio = Limiter(threshold_db=-5.0).process(self.audio, self.sample_rate)

    def apply(self, runId, outputPath, play=False):
        self._nameOutputFile(outputPath, runId)
        self.process()
        self._save()
        if play == True:
            self._play()

    def _read(self):
        self.audio, self.sample_rate = sf.read(self.path)

    def _nameOutputFile(self, outputPath, runId):        
        name, extension = os.path.splitext(os.path.basename(self.path))
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

    def _play(self):
        from playsound import playsound
        playsound(self.output)