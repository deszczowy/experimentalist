from Experimentalist.Actions import Echo
from Experimentalist.Core import Worker


class Echoer(Worker):

    def __init__(self, filePath: str) -> None:
        super().__init__(filePath, "Echoer")

    def process(self) -> None:
        self.audio = Echo().process(self.audio, self.sample_rate)
