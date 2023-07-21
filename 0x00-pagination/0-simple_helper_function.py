#!/usr/bin/env python3
""" Helper function module """


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end indexes for a given page and page_size.

    Args:
        page (int): The 1-indexed page number.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and end index for the given page.
    """
    if page < 1 or page_size < 1:
        raise ValueError("Page and page_size must be positive integers.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
