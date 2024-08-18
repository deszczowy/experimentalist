from Experimentalist.Core import Log
from pedalboard import Limiter
import os
import soundfile as sf


class Worker:

    def __init__(self, filePath: str, workerName: str) -> None:
        self.log = Log(workerName)
        self.path = filePath
        self._read()
        self.computeLength()
        self.log.write(f"Data prepared from {filePath}")

    def process(self) -> None:
        self.normalize()
        self.computeLength()

    def computeLength(self) -> None:
        self.length = len(self.audio) / self.sample_rate  # length in seconds

    def normalize(self) -> None:
        self.audio = Limiter(threshold_db=-5.0).process(
            self.audio,
            self.sample_rate
        )

    def apply(self, runId: int, outputPath: str, play: bool = False) -> None:
        self._nameOutputFile(outputPath, runId)
        self.process()
        self._save()
        if play is True:
            self._play()

    def _read(self) -> None:
        self.audio, self.sample_rate = sf.read(self.path)

    def _nameOutputFile(self, outputPath: str, runId: int) -> None:
        name, extension = os.path.splitext(os.path.basename(self.path))
        self.output = os.path.join(outputPath, "")
        self.output = f"{self.output}{name}-{runId}{extension}"

    def _save(self) -> None:
        with sf.SoundFile(
            self.output,
            'w',
            samplerate=self.sample_rate,
            channels=len(self.audio.shape)
        ) as f:
            f.write(self.audio)

    def _play(self) -> None:
        from playsound import playsound
        playsound(self.output)
