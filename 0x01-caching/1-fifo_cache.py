#!/usr/bin/env python3

"""
Create a class FIFOCache that inherits from
BaseCaching and is a caching system:
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    You must use self.cache_data - dictionary from the
    parent class BaseCaching
    You can overload def __init__(self): but don't forget to
    call the parent init: super().__init__()
    def put(self, key, item):
        Must assign to the dictionary self.cache_data the item
        value for the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher
        that BaseCaching.MAX_ITEMS:
        you must discard the first item put in cache (FIFO algorithm)
        you must print DISCARD: with the key discarded and
        following by a new line
    def get(self, key):
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn't exist in
        self.cache_data, return None.
    """

    def put(self, key, item):
        """Register a key if !empty and checks if > MAX_ITEMS"""
        if key is not None and item is not None:
            self.cache_data.update({key: item})
            if self.cache_data.items().__len__() > self.MAX_ITEMS:
                keys = [val for val in self.cache_data.keys()]
                self.cache_data.pop(keys[0])
                print("DISCARD: {}".format(keys[0]))

    def get(self, key):
        """return a specific key else none"""
        return self.cache_data.get(key, None)
