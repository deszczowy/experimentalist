from Experimentalist.Core import Audio, Log
import numpy as np


class Action:

    def __init__(self, withName: str) -> None:
        self.log = Log(withName)

    def process(self, audio: Audio) -> None:
        pass
