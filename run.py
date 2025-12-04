from Experimentalist.Core import Processor, Arguments
from Experimentalist.Experiment import Container

# Arguments parser. You can use it, but don't have to.
a = Arguments()

# Main part: a processor. Here a command line argument value is provided with sources path.
p = Processor(a.sources())

## Example of custom code
from Experimentalist.Core import Worker
from Experimentalist.Actions import Loop
from pedalboard import Reverb
import soundfile as sf
import os

## Simple worker
class Reverber(Worker):

    def __init__(self, filePath):
        super().__init__(filePath, "Reverber")

    def process(self):
        self.audio = Reverb(room_size=1, damping=0).process(self.audio, self.sample_rate)

## Method which invokes worker
def reverbed(file, id, outputPath):
    Reverber(file).apply(id, outputPath, True) # result will be played, for testing.
##

# Now some experiments will be connected to the chain of works. Each one of it will
# be invoked on every file from sources path.
p.connect(Container.LoopClean)
p.connect(Container.LoopLong)
p.connect(Container.LoopDrone)
p.connect(Container.SpaceFull)
p.connect(Container.SpaceLoop)
p.connect(reverbed)

# Sit back and wait for the results
p.perform()
