from Experimentalist.Workers import Looper, Drone


class Container:

    @staticmethod
    def Header() -> None:
        return "============== Experiment: "

    @staticmethod
    def LoopClean(file: str, id: int, outputPath: str) -> None:
        print(f"{Container.Header()} LoopClean for {file}")
        Looper(file).apply(id, outputPath)

    @staticmethod
    def LoopLong(file: str, id: int, outputPath: str) -> None:
        print(f"{Container.Header()} LoopLong for {file}")
        Looper(file, 20).apply(id, outputPath)

    @staticmethod
    def LoopDrone(file: str, id: int, outputPath: str) -> None:
        Drone(file, maxDuration=20, factor=0.8).apply(id, outputPath)
