from Experimentalist.Core import Log
import os
from glob import glob
from collections.abc import Callable


class Processor:

    def __init__(self, directory: str) -> None:
        self.log = Log("Processor")
        self.experiments = []
        self.counter = 0
        self._setupDirectories(directory)
        self._loadSources()
        self._logProcessorState()

    def perform(self) -> None:
        for f in self.filesToProcess:
            for experiment in self.experiments:
                self.counter += 1
                experiment(f, self.counter, self.target)

    def connect(self, experiment: Callable[[str, int, str], None]) -> None:
        self.log.write(f"Connecting {experiment.__name__}")
        self.experiments.append(experiment)

    def _setupDirectories(self, path: str) -> None:
        self.source = os.path.join(path, "")
        if not os.path.exists(path):
            raise Exception("Source directory does not exists.")

        self.target = os.path.join(self.source, "results")
        self._forceDirectory(self.target)

    def _forceDirectory(self, path: str) -> None:
        if not os.path.exists(path):
            os.makedirs(path)

    def _loadSources(self) -> None:
        self.filesToProcess = glob(f"{self.source}*.wav")

    def _logProcessorState(self) -> None:
        self.log.write(f"Sources path: {self.source}")
        self.log.write(f"Results path: {self.target}")
        self.log.write(f"Found {len(self.filesToProcess)} sources")
