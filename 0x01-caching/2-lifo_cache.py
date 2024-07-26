#!/usr/bin/python3
"""A caching system LIFO implementation"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """implements put and get methods"""
    def __init__(self) -> None:
        """BaseCaching Caching System"""
        super().__init__()
        self.last = ""

    def put(self, key, item):
        """puts a value"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.last))
                del (self.cache_data[self.last])
            self.last = key

    def get(self, key):
        """gets a value"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
