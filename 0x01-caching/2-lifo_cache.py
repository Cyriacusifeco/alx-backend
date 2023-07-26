#!/usr/bin/env python3

"""
LIFOCache Class

This class inherits from BaseCaching and implements a
caching system using the Last-In-First-Out (LIFO) algorithm.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache Class

    This class inherits from BaseCaching and implements a
    caching system using the Last-In-First-Out (LIFO) algorithm.
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

            # Check if the number of items in the
            # cache exceeds the maximum limit
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Retrieve the last item (LIFO) that was put in the cache
                last_key = list(self.cache_data.keys())[-2]
                # Remove the last item from the cache
                del self.cache_data[last_key]
                print("DISCARD: {}".format(last_key))

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
