#!/usr/bin/python3
"""A caching system LFU implementation"""

from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """Implements put and get methods with LFU eviction policy"""

    def __init__(self) -> None:
        """Initialize the LFUCache"""
        super().__init__()
        self.item_frequency = {}
        self.frequency_lists = {}
        self.min_freq = 0

    def update_frequency(self, key):
        """Update the frequency of an item"""
        if key in self.item_frequency:
            freq = self.item_frequency[key]
            self.frequency_lists[freq].remove(key)
            if not self.frequency_lists[freq]:
                del self.frequency_lists[freq]
                if self.min_freq == freq:
                    self.min_freq += 1
            self.item_frequency[key] = freq + 1
            if freq + 1 not in self.frequency_lists:
                self.frequency_lists[freq + 1] = set()
            self.frequency_lists[freq + 1].add(key)
        else:
            self.item_frequency[key] = 1
            if 1 not in self.frequency_lists:
                self.frequency_lists[1] = set()
            self.frequency_lists[1].add(key)
            self.min_freq = 1

    def get_least_frequent(self):
        """Get the least frequent item from the cache"""
        if not self.frequency_lists:
            return None
        least_freq = self.min_freq
        if least_freq not in self.frequency_lists or not self.frequency_lists[least_freq]:
            return None
        item_to_discard = self.frequency_lists[least_freq].pop()
        if not self.frequency_lists[least_freq]:
            del self.frequency_lists[least_freq]
        return item_to_discard

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.update_frequency(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                item_to_discard = self.get_least_frequent()
                if item_to_discard is not None:
                    del self.cache_data[item_to_discard]
                    del self.item_frequency[item_to_discard]
                    print("DISCARD:", item_to_discard)
            self.cache_data[key] = item
            self.update_frequency(key)

    def get(self, key):
        """Retrieve an item from the cache"""
        if key is None or key not in self.cache_data:
            return None

        self.update_frequency(key)
        return self.cache_data[key]
