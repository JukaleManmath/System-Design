"""
Central Cache Manager
Imagining having a cache (like Redis or in-memory) that should be shared app-wide.
You don’t want it loaded until it’s actually used (lazy initialization).
"""


import time

class CacheManager:
    class _Helper:
        INSTANCE = None

    def __init__(self):
        if CacheManager._Helper.INSTANCE is not None:
            raise Exception("Use get_instance() instead.")
        print("Connecting to Redis cache...")
        time.sleep(1)
        self.cache = {"status": "connected"}

    @staticmethod
    def get_instance():
        if CacheManager._Helper.INSTANCE is None:
            CacheManager._Helper.INSTANCE = CacheManager()
        return CacheManager._Helper.INSTANCE
