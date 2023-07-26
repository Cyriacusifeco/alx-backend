#!/usr/bin/env python3

"""
BasicCache Class

This class inherits from BaseCaching and implements a
basic caching mechanism using a dictionary.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache Class

    This class inherits from BaseCaching and implements a
    basic caching mechanism using a dictionary.
    """

    def __init__(self):
        # Call the constructor of the parent class
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key to associate with the item.
            item: The item to be stored in the cache.

        Returns:
            None
        """
        if key is not None and item is not None:
            # Add the item to the cache dictionary
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value associated with the given key if found, otherwise None.
        """
        if key is not None:
            # Try to get the item from the cache
            return self.cache_data.get(key, None)
        return None
