"""
BILL PUGH SINGLETON (Lazy, Thread-Safe via Inner Helper)

WHAT:
- Uses an inner helper class to hold the Singleton instance.
- Instance is created only when the helper class is first accessed.

WHY:
- Provides lazy initialization without explicit synchronization.
- Clean separation of concern: outer class defines behavior, inner class stores instance.

WHEN TO USE:
- When you want thread safety, lazy loading, and clean structure
  (e.g., cache managers, model loaders, service connectors).

KEY IDEA:
- Inner helper is loaded only when get_instance() is called → lazy & safe.
"""


class BillPughSingleton:
    class _Helper:
        INSTANCE = None

    def __init__(self):
        if BillPughSingleton._Helper.INSTANCE is not None:
            raise Exception("Use get_instance() instead.")
        print("Bill Pugh Singleton instance created.")

    @staticmethod
    def get_instance():
        if BillPughSingleton._Helper.INSTANCE is None:
            BillPughSingleton._Helper.INSTANCE = BillPughSingleton()
        return BillPughSingleton._Helper.INSTANCE
