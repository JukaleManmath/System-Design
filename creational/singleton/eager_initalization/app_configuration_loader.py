"""
When your app starts, you want configuration (like API keys, DB creds, file paths) 
loaded once at startup and available everywhere.
"""

class Config:

    _instance = None

    def __init__(self):
        if Config._instance is not None:
            raise Exception("Use get_instance() instead.")
        self.settings = {
            "DB_URL": "postgres://localhost",
            "API_KEY": "secret123",
            "LOG_LEVEL": "DEBUG",
        }
        print("Configuration loaded.")

    @staticmethod
    def get_instance():
        return Config._instance

# Eagerly load config at import time
Config._instance = Config()