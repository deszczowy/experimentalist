from Experimentalist.Core import Action

class Loop:
    def __init__(self):
        self.peak = 0.5
        
    def process(self, audio, sample_rate):
        length = len(audio[:, 0])
        loop_point = int(length * self.peak)
        part1 = audio[:loop_point, :]
        part2 = audio[-loop_point:, :]
        audio = 0.5 * part1 + 0.5 * part2
        return audio