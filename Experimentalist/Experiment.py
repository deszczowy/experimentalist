from Experimentalist.Workers import Looper, Drone

class Container:
    
    @staticmethod
    def Header():
        return "============== Experiment: "

    @staticmethod
    def LoopClean(file, id, outputPath):
        print(f"{Container.Header()} LoopClean for {file}")
        Looper(file).apply(id, outputPath)
    
    @staticmethod
    def LoopLong(file, id, outputPath):
        print(f"{Container.Header()} LoopLong for {file}")
        Looper(file, 20).apply(id, outputPath)

    @staticmethod
    def LoopDrone(file, id, outputPath):
        Drone(file, maxDuration=20, factor=0.8).apply(id, outputPath)