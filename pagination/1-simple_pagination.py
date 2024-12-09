#!/usr/bin/env Python3

"""
Simple pagination
"""


import csv
import math
from typing import List


def index_range(page, page_size) -> tuple:
    """
    Returns a tuple containing the start and end index for pagination.

    Parameters:
    page (int): The page number (1-indexed).
    page_size (int): The number of items per page.

    Returns:
    tuple: A tuple containing the start index and end index.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)

class Server:
    """
    Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """

        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a tuple of size two
        containing a start index and an end index
        """

        assert type(page) is int \
            and type(page_size) is int
        assert page > 0 and page_size > 0

        start = (page - 1) * page_size
        end = page * page_size

        return self.dataset()[start:end]
