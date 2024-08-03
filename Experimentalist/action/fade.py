from numpy import clip

from Experimentalist.Core import Action
   
class Fade(Action):
    
    def __init__(self, peak_position: float = 0.5):
        super().__init__("Fade")
        self.peak = clip(peak_position, 0, 1)
        
    def process(self, audio, sample_rate):
        super().process(audio, sample_rate)
        
        peak_point = int(self.length * self.peak)

        if peak_point == 0:
            peak_point += 1
        if peak_point == self.length:
            peak_point -= 1

        coef1 = 1 / peak_point # fade in
        coef2 = 1 / (self.length - peak_point) # fade out
        
        for i in range(0, peak_point - 1):
            audio[i, 0] = audio[i, 0] * coef1 * i
            audio[i, 1] = audio[i, 1] * coef1 * i
           
        for i in range(peak_point, self.length):
            audio[i, 0] = audio[i, 0] * coef2 * (self.length - i)
            audio[i, 1] = audio[i, 1] * coef2 * (self.length - i)
        
        return audio