"""
LAZY INITIALIZATION SINGLETON (Non-Thread-Safe)

WHAT:
- Creates the Singleton instance only when it’s first requested.
- Does not use any locking mechanism → not thread-safe.

WHY:
- Saves resources by delaying object creation until actually needed.
- Suitable for single-threaded applications or lightweight scripts.

WHEN TO USE:
- In simple programs or utilities where concurrency is not a concern
  (e.g., single-threaded apps, config readers, data parsers).

KEY IDEA:
- Instance is created inside get_instance() only on first call.
- Subsequent calls return the same stored instance.
"""

class LazySingleton:

    _instance = None

    def __init__(self):
        if LazySingleton._instance is not None:
            raise Exception("use get_instance() instead")

    @staticmethod 
    def get_instance():
        if LazySingleton._instance is None:
            LazySingleton._instance = LazySingleton()
        return LazySingleton._instance

    # A Singleton ensures that only one object of a class can exist throughout the program.
    # So even if we try to create it multiple times, all references point to the same instance.
    # Because the instance is created only when needed, i.e., when get_instance() is called for the first time — not before.
    # This is called lazy initialization.

    # Singleton pattern actually shines — when you want only one instance of a resource across your application 
    # (for example: database connection, configuration loader, logger, cache manager, etc.).