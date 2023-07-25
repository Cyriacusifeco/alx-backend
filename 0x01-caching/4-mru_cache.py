#!/usr/bin/env python3

"""
MRUCache Class

This class inherits from BaseCaching and implements a caching system using the Most Recently Used (MRU) algorithm.
"""

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """
    MRUCache Class

    This class inherits from BaseCaching and implements a caching system using the Most Recently Used (MRU) algorithm.
    """

    def __init__(self):
        # Call the constructor of the parent class
        super().__init__()
        # List to store the order of keys in MRU fashion
        self.mru_list = []

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

            # Check if the key is already in the MRU list
            if key in self.mru_list:
                # If it is, remove it from its current position
                self.mru_list.remove(key)

            # Check if the number of items in the cache exceeds the maximum limit
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                if self.mru_list:
                    # Retrieve the most recently used item (MRU) from the end of the list
                    mru_key = self.mru_list.pop()
                    # Remove the MRU item from the cache
                    del self.cache_data[mru_key]
                    print("DISCARD: {}".format(mru_key))

            # Update the MRU list with the most recently used key (move it to the end)
            self.mru_list.append(key)

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
            item = self.cache_data.get(key, None)
            if item is not None:
                # Update the MRU list with the most recently used key (move it to the end)
                self.mru_list.remove(key)
                self.mru_list.append(key)
            return item
        return None
