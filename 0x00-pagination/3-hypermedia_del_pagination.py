#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a dictionary with hypermedia pagination information based on the start index (index).

        Args:
            index (int, optional): The 0-indexed start index of the page. Default is None.
            page_size (int, optional): The number of items per page. Default is 10.

        Returns:
            dict: A dictionary containing hypermedia pagination information.
        """
        indexed_dataset = self.indexed_dataset()
        total_items = len(indexed_dataset)

        assert isinstance(index, int) and 0 <= index < total_items, "Index is out of range."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."

        # Check if the requested index is still available in the dataset
        if index not in indexed_dataset:
            # Find the next available index
            next_index = index + 1
            while next_index < total_items and next_index not in indexed_dataset:
                next_index += 1

            # If no next index is available, return an empty page
            if next_index >= total_items:
                return {
                    "index": index,
                    "data": [],
                    "page_size": 0,
                    "next_index": None,
                }

            # Update the index to the next available index
            index = next_index

        data = [indexed_dataset[i] for i in range(index, min(index + page_size, total_items))]

        next_index = min(index + page_size, total_items) if index + page_size < total_items else None

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index,
        }
