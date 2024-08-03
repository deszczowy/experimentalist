class Log:
    
    def __init__(self, loggerName):
        self.tag = loggerName
    
    def write(self, message):
        print(f"{self.tag}: {message}")