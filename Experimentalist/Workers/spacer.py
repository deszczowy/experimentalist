from Experimentalist.Core import Worker
from Experimentalist.Actions import HighPass, LowPass, DynamicPan, Mix, Reverb, Fade, Loop


class Spacer(Worker):

    def __init__(self, filePath: str) -> None:
        super().__init__(filePath, "Spacer")

    def process(self) -> None:
        self.audio = Reverb(room_size=1.0, dry_wet=1.0).process(self.audio, self.sample_rate)

        copy1 = self.audio.copy()
        copy2 = self.audio.copy()

        copy1 = HighPass().process(copy1, self.sample_rate)
        copy1 = DynamicPan(phase=10.0, starting_left=True).process(copy1, self.sample_rate)
        copy2 = LowPass().process(copy2, self.sample_rate)
        copy2 = DynamicPan(phase=10.0, starting_left=False).process(copy2, self.sample_rate)

        mixer = Mix(base_audio=copy1, offset_seconds=0.0, clip=True)
        mixer.process(copy2, self.sample_rate)

        self.audio = mixer.result()
        super().process()

class SpacerLoop(Spacer):

    def __init__(self, filePath: str) -> None:
        super().__init__(filePath)

    def process(self) -> None:
        super().process()

        maxDuration = 10
        if self.length > maxDuration:
            while True:
                self.audio = Fade().process(self.audio, self.sample_rate)
                self.audio = Loop().process(self.audio, self.sample_rate)

                self.normalize()
                self.computeLength()

                if self.length < maxDuration:
                    break

