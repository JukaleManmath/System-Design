"""
🔒 DOUBLE-CHECKED LOCKING SINGLETON (Thread-Safe, Lazy)

WHAT:
- A lazy-loaded Singleton that checks twice before creating an instance.
- Uses a lock only during the first initialization for thread safety.

WHY:
- Prevents multiple threads from creating separate instances.
- Avoids performance overhead by locking only once when needed.

WHEN TO USE:
- In multi-threaded systems where object creation is expensive
  (e.g., database connections, logging systems, API clients).

KEY IDEA:
- First check (_instance is None) → avoids locking once initialized.
- Second check inside lock → ensures only one thread creates the object.
"""

import threading

class DoubleCheckedSingleton:

    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        if DoubleCheckedSingleton._instance is not None:
            raise Exception("use get_instance() instead")
    
    @staticmethod
    def get_instance():
        if DoubleCheckedSingleton._instance is None:    # first check
            with DoubleCheckedSingleton._lock:          # lock acquired
                if DoubleCheckedSingleton._instance is None:    # second check
                    DoubleCheckedSingleton._instance = DoubleCheckedSingleton()
        return DoubleCheckedSingleton._instance
