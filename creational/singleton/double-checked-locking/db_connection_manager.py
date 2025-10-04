import psycopg2
import threading

class DBConnectionManager:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        if DBConnectionManager._instance is not None:
            raise Exception("Use get_instance() instead.")
        self.connection = psycopg2.connect(
            dbname="mydb", user="admin", password="pass", host="localhost"
        )
        print("DB connection created.")

    @staticmethod
    def get_instance():
        if DBConnectionManager._instance is None:
            with DBConnectionManager._lock:
                if DBConnectionManager._instance is None:
                    DBConnectionManager._instance = DBConnectionManager()
        return DBConnectionManager._instance
