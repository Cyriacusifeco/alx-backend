#!/usr/bin/env python3

"""
LRUCache Class

This class inherits from BaseCaching and implements a
caching system using the Least Recently Used (LRU) algorithm.
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache Class

    This class inherits from BaseCaching and implements a
    caching system using the Least Recently Used (LRU) algorithm.
    """

    def __init__(self):
        # Call the constructor of the parent class
        super().__init__()
        # List to store the order of keys in LRU fashion
        self.lru_list = []

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

            # Check if the key is already in the LRU list
            if key in self.lru_list:
                # If it is, remove it from its current position
                self.lru_list.remove(key)

            # Update the LRU list with the most
            # recently used key (move it to the end)
            self.lru_list.append(key)

            # Check if the number of items in the
            # cache exceeds the maximum limit
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                if self.lru_list:
                    # Retrieve the least recently used item (LRU)
                    # from the beginning of the list
                    lru_key = self.lru_list.pop(0)
                    # Remove the LRU item from the cache
                    del self.cache_data[lru_key]
                    print("DISCARD: {}".format(lru_key))
                else:
                    # If the LRU list is empty, skip the eviction step
                    print("LRU list is empty. Unable to evict LRU item.")

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
                # Update the LRU list with the most recently
                # used key (move it to the end)
                self.lru_list.remove(key)
                self.lru_list.append(key)
            return item
        return None
