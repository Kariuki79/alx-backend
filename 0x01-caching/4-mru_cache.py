#!/usr/bin/python3
"""A caching system MRU implementation"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """implements put and get methods"""
    def __init__(self) -> None:
        """BaseCaching Caching System"""
        super().__init__()
        self.__keys = []

    def put(self, key, item):
        """puts a value"""
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.__keys:
            discard = self.__keys.pop()
            del self.cache_data[discard]
            print('DISCARD: {}'.format(discard))
        if key and item:
            if key not in self.__keys:
                self.__keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """gets a value"""
        if key is None or self.cache_data.get(key) is None:
            return None
        self.__keys.remove(key)
        self.__keys.append(key)
        return self.cache_data.get(key)
