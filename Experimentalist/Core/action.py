from Experimentalist.Core import Audio, Log
import numpy as np


class Action:
    """
    Base class for actions invoked on sound.

    Parameters
    ----------
    withName : str
        This is an action name, which will appear in log file and prints.
    """
    def __init__(self, withName: str) -> None:
        self.log = Log(withName)

    def process(self, audio: Audio) -> None:
        pass
