#!/usr/bin/env python3

"""
LFUCache Class

This class inherits from BaseCaching and implements a caching system using the Least Frequently Used (LFU) algorithm.
"""

from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """
    LFUCache Class

    This class inherits from BaseCaching and implements a caching system using the Least Frequently Used (LFU) algorithm.
    """

    def __init__(self):
        # Call the constructor of the parent class
        super().__init__()
        # Dictionary to store the frequency of each key
        self.frequency_data = {}

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

            # Increase the frequency of the key by 1
            self.frequency_data[key] = self.frequency_data.get(key, 0) + 1

            # Check if the number of items in the cache exceeds the maximum limit
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Find the least frequency used key(s)
                min_frequency = min(self.frequency_data.values())
                least_frequent_keys = [key for key, freq in self.frequency_data.items() if freq == min_frequency]

                # If there is only one key with the least frequency, discard it
                if len(least_frequent_keys) == 1:
                    lfu_key = least_frequent_keys[0]
                    del self.cache_data[lfu_key]
                    del self.frequency_data[lfu_key]
                    print("DISCARD: {}".format(lfu_key))
                else:
                    # If there are multiple keys with the same least frequency, apply LRU to break the tie
                    # Retrieve the least recently used key from the cache
                    lru_key = least_frequent_keys.pop(0)
                    for key in least_frequent_keys:
                        if self.frequency_data[key] < self.frequency_data[lru_key]:
                            lru_key = key

                    del self.cache_data[lru_key]
                    del self.frequency_data[lru_key]
                    print("DISCARD: {}".format(lru_key))

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
                # Increase the frequency of the key by 1
                self.frequency_data[key] = self.frequency_data.get(key, 0) + 1
            return item
        return None
