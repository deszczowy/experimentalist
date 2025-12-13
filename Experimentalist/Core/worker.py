from Experimentalist.Core import Audio, Log
import os
import soundfile as sf


class Worker:

    def __init__(self, filePath: str, workerName: str) -> None:
        self.log = Log(workerName)
        self.audio = Audio(filePath)
        self.log.write(f"Data prepared from {filePath}")

    def process(self) -> None:
        self.audio.normalize()
        self.audio.update_parameters()

    def apply(self, runId: int, outputPath: str, play: bool = False) -> None:
        self._nameOutputFile(outputPath, runId)
        self.process()
        self._save()
        if play is True:
            self._play()

    def _nameOutputFile(self, outputPath: str, runId: int) -> None:
        name, extension = os.path.splitext(os.path.basename(self.audio.path))
        self.output = os.path.join(outputPath, "")
        self.output = f"{self.output}{name}-{runId}{extension}"

    def _save(self) -> None:
        with sf.SoundFile(
            self.output,
            'w',
            samplerate=self.audio.sample_rate,
            channels=self.audio.channels
        ) as f:
            f.write(self.audio.frames)

    def _play(self) -> None:
        from playsound import playsound
        self.log.write(f"Playing {self.output}")
        playsound(self.output)
