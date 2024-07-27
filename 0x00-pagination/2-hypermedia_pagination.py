#!/usr/bin/env python3
"""
Server class with various ftns
"""
import csv
import math
from typing import List, Dict


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
        page_size with default value 10"""
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """takes two integer arguments page with default value 1 and
        page_size with default value 10, returns a dictionary containing
        the following key-value pairs:.
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        """
        # Verify that both arguments are integers greater than 0
        assert isinstance(page, int) and page > 0, (
            "Page should be an integer greater than 0."
        )
        assert isinstance(page_size, int) and page_size > 0, (
            "Page_size should be an integer greater than 0."
        )

        # Get the paginated data using the get_page method
        paginated_data = self.get_page(page, page_size)

        # Calculate total pages
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        # Calculate next and previous page numbers
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        # Create the dictionary with the required key-value pairs
        hyper_data = {
            "page_size": len(paginated_data),
            "page": page,
            "data": paginated_data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

        return hyper_data
