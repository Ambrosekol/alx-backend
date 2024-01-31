#!/usr/bin/env python3

"""
Create a class BasicCache that inherits from
BaseCaching and is a caching system:
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    You must use self.cache_data - dictionary from the
    parent class BaseCaching
    This caching system doesn't have limit
    """

    def put(self, key, item):
        """put into cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get item in cache"""
        return self.cache_data.get(key, None)
