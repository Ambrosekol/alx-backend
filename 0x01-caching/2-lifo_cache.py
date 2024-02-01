#!/usr/bin/env python3
"""
Create a class LIFOCache that inherits from BaseCaching and
is a caching system:
"""


import base_caching


class LIFOCache(base_caching.BaseCaching):
    """
    You must use self.cache_data - dictionary from the parent
    class BaseCaching
    You can overload def __init__(self): but don't forget to call
    the parent init: super().__init__()
    """
    def put(self, key, item):
        """Register a key if !empty and checks if > MAX_ITEMS"""
        if key is not None and item is not None:
            self.cache_data.update(key=item)
            keys = [val for val in self.cache_data.keys()]
            if len(keys) > self.MAX_ITEMS:
                self.cache_data.pop(keys.pop())
                print("DISCARD: {}".format(keys.pop()))

    def get(self, key):
        """return a specific key else none"""
        return self.cache_data.get(key, None)
