import os
from glob import glob

from Experimentalist.Core import Log

class Processor:
    
    def __init__(self, directory):
        self.log = Log("Processor")
        self.experiments = []
        self.counter = 0
        self._setupDirectories(directory)
        self._loadSources()
        self._logProcessorState()

    def perform(self):
        for f in self.filesToProcess:
            for experiment in self.experiments:
                self.counter += 1
                experiment(f, self.counter, self.target)

    def connect(self, experiment):
        self.log.write(f"Connecting {experiment.__name__}")
        self.experiments.append(experiment)

    def _setupDirectories(self, path):
        self.source = os.path.join(path, "")
        if not os.path.exists(path):
            raise Exception("Source directory does not exists.")

        self.target = os.path.join(self.source, "results")
        self._forceDirectory(self.target)

    def _forceDirectory(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def _loadSources(self):
        self.filesToProcess = glob(f"{self.source}*.wav")
    
    def _logProcessorState(self):
        self.log.write(f"Sources path: {self.source}")
        self.log.write(f"Results path: {self.target}")
        self.log.write(f"Found {len(self.filesToProcess)} sources")

