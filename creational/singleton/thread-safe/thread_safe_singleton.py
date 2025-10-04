"""
THREAD-SAFE SINGLETON (Lazy + Safe for Multi-Threading)

WHAT:
- Ensures that only one instance of the class is created,
  even when multiple threads access it concurrently.
- Uses a lock to prevent race conditions during first initialization.

WHY:
- Prevents duplicate object creation in multi-threaded environments.
- Ideal for shared resources (e.g., loggers, database connections).

WHEN TO USE:
- In concurrent or server-based systems where multiple threads may
  access shared resources simultaneously (e.g., backend APIs, workers).

KEY IDEA:
- Uses `threading.Lock()` around the instance creation section.
- Guarantees one instance, created safely and lazily.
"""


import threading

class ThreadSafeSingleton:

    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        if ThreadSafeSingleton._instance is not None:
            raise Exception("use get_instance() instead.")
    
    @staticmethod
    def get_instance():
        with ThreadSafeSingleton._lock:
            if ThreadSafeSingleton._instance is None:
                ThreadSafeSingleton._instance = ThreadSafeSingleton()
        return ThreadSafeSingleton._instance


