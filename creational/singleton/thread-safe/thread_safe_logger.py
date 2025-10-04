import threading
import time

class ThreadSafeLogger:
    _instance = None
    _lock = threading.Lock()  # shared lock for all threads

    def __init__(self, filename):
        if ThreadSafeLogger._instance is not None:
            raise Exception("Use get_instance() instead of creating directly.")
        self.filename = filename
        with open(self.filename, "a") as f:
            f.write("=== Log started ===\n")

    @staticmethod
    def get_instance(filename="app.log"):
        with ThreadSafeLogger._lock:
            if ThreadSafeLogger._instance is None:
                ThreadSafeLogger._instance = ThreadSafeLogger(filename)
        return ThreadSafeLogger._instance

    def log(self, message):
        """Write a message to the log file."""
        with open(self.filename, "a") as f:
            f.write(f"[{threading.current_thread().name}] {message}\n")


if __name__ == "__main__":
    def worker(task_id):
        logger = ThreadSafeLogger.get_instance()
        for i in range(3):
            logger.log(f"Task {task_id} - Step {i}")
            time.sleep(0.1)

    threads = []
    for i in range(5):  # 5 worker threads
        t = threading.Thread(target=worker, args=(i,), name=f"Worker-{i}")
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


