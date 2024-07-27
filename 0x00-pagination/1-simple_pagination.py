#!/usr/bin/env python3
"""
Server class with various ftns
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    ftn takes in two ints and returns atuple
    """
    start_index: int = (page - 1) * page_size
    end_index: int = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """takes two integer arguments page with default value 1 and
        page_size with default value 10."""
        # Verify that both arguments are integers greater than 0
        assert isinstance(page, int) and page > 0, (
            "Page should be an integer greater than 0."
        )
        assert isinstance(page_size, int) and page_size > 0, (
            "Page_size should be an integer greater than 0."
        )

        # Calculate the start and end indexes using index_range function
        start_index, end_index = index_range(page, page_size)

        # Return the appropriate page of the dataset
        return self.dataset()[start_index:end_index]
