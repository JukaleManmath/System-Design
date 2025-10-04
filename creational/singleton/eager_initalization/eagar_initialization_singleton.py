"""
⚡ EAGER INITIALIZATION SINGLETON (Thread-Safe, Non-Lazy)

WHAT:
- The Singleton instance is created immediately when the class is loaded.
- No synchronization or locking is required.

WHY:
- Thread-safe by design since the instance exists before any thread uses it.
- Simple and reliable — no race conditions possible.

WHEN TO USE:
- When the instance is lightweight and always needed throughout the app
  (e.g., configuration loader, constants manager, global settings).

KEY IDEA:
- Instance created eagerly at load time → zero runtime overhead later.
- Might waste resources if never used.
"""

class EagerSingleton:

    _instance = None

    def __init__(self):
        if EagerSingleton._instance is not None:
            raise Exception("use get_instance() instead")
        print("Eager Singleton Initialized")
    
    @staticmethod
    def get_instance():
        return EagerSingleton._instance

# Instance created eagerly when class is loaded
EagerSingleton._instance = EagerSingleton()