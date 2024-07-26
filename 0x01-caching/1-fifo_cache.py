#!/usr/bin/python3
"""
Basic FIFO cache implementation
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """BaseCaching FIFO Caching System"""

    def __init__(self) -> None:
        """Init function"""
        super().__init__()

    def put(self, key, item):
        """Put function"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first = list(self.cache_data.keys())[0]
                print("DISCARD: {}".format(first))
                del (self.cache_data[first])

    def get(self, key):
        """Get function"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
