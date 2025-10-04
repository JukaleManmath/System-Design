import datetime

class Logger:
    _instance = None

    def __init__(self):
        if Logger._instance is not None:
            raise Exception("user get_instance() instead")
    
        self.log_file = open("app.log", "a")
    
    @staticmethod
    def get_instance():
        if Logger._instance is None:
            Logger._instance = Logger()
        
        return Logger._instance

    def log(self, message):
        timestamp = datetime.datetime.now().isoformat()
        self.log_file.write(f"[{timestamp}] {message}\n")
        self.log_file.flush()
    
logger1 = Logger.get_instance()
logger1.log("Server started")

logger2 = Logger.get_instance()
logger2.log("User logged in")

print(logger1 is logger2)  # ✅ True
