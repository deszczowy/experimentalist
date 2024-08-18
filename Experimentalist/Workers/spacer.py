from Experimentalist.Core import Worker
from Experimentalist.Actions import HighPass, LowPass, Copy, DynamicPan, Mix, Reverb


class Spacer(Worker):

    def __init__(self, filePath: str) -> None:
        super().__init__(filePath, "Test")

    def process(self) -> None:
        self.audio = Reverb(room_size=1.0, dry_wet=1.0).process(self.audio, self.sample_rate)

        copy1 = Copy().process(self.audio, self.sample_rate)
        copy2 = Copy().process(self.audio, self.sample_rate)

        copy1 = HighPass().process(copy1, self.sample_rate)
        copy1 = DynamicPan(phase=10.0, starting_left=True).process(copy1, self.sample_rate)
        copy2 = LowPass().process(copy2, self.sample_rate)
        copy2 = DynamicPan(phase=10.0, starting_left=False).process(copy2, self.sample_rate)

        mixer = Mix(base_audio=copy1, offset_seconds=0.0, clip=True)
        mixer.process(copy2, self.sample_rate)

        self.audio = mixer.result()
        super().process()
