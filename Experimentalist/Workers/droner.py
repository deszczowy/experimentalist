from Experimentalist.Actions import Fade, Loop, Stretch
from Experimentalist.Core import Worker


class Droner(Worker):

    def __init__(
            self,
            filePath: str,
            factor: float = 0.9,
            maxDuration: float = 10
            ) -> None:
        super().__init__(filePath, "Drone")
        self.maxDuration = maxDuration
        self.factor = factor

    def process(self) -> None:
        while True:
            self.audio = Stretch(self.factor).process(
                self.audio,
                self.sample_rate)
            self.audio = Fade().process(self.audio, self.sample_rate)
            self.audio = Loop().process(self.audio, self.sample_rate)
            super().process()
            self.log.write(f"Loop length {self.length}")

            if self.length < self.maxDuration:
                break
