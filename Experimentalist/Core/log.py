class Log:

    def __init__(self, loggerName: str) -> None:
        self.tag = loggerName

    def write(self, message: str) -> None:
        print(f"{self.tag}: {message}")
