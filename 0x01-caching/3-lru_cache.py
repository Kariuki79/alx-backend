#!/usr/bin/python3
"""A caching system LRU implementation"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """implements put and get methods"""
    def __init__(self) -> None:
        """BaseCaching Caching System"""
        super().__init__()
        self.list = []

    def put(self, key, item):
        """puts a value"""
        if key and item:
            self.cache_data[key] = item
            if key not in self.list:
                self.list.append(key)
            else:
                if self.list[-1] != key:
                    self.list.remove(key)
                    self.list.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.list[0]))
                del (self.cache_data[self.list[0]])
                self.list.pop(0)

    def get(self, key):
        """gets a value"""
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.list:
            if self.list[-1] != key:
                self.list.remove(key)
                self.list.append(key)

        return self.cache_data.get(key)
