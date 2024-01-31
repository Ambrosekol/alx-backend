#!/usr/bin/env python3

"""
Create a class BasicCache that inherits from
BaseCaching and is a caching system:
"""


from baseclass import BaseCaching


class BasicCache(BaseCaching):
    """
    You must use self.cache_data - dictionary from the
    parent class BaseCaching
    This caching system doesn't have limit
    def put(self, key, item):
    Must assign to the dictionary self.cache_data the item
    value for the key key.
        If key or item is None, this method should not do anything.
    def get(self, key):
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn't exist in self.cache_data,
        return None.
    """

    def put(self, key, item):
        """put into cache"""
        if key is None:
            return
        if item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """get item in cache"""
        val = None
        if key is not None:
            val = self.cache_data.get(key)
        return val
