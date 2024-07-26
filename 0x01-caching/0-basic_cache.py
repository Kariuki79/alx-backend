#!/usr/bin/python3
"""A caching system that inherits from BaseCaching"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """implements put and get methods"""
    def __init__(self) -> None:
        """BaseCaching Caching System"""
        super().__init__()

    def put(self, key, item):
        """puts a value"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """gets a value"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
