#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""


import csv
import math
from typing import List, Dict


class Server:
    """
    Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary with the following pagination details:
        - index: the current start index of the return page.
        - next_index: the next index to query with.
        - page_size: the current page size.
        - data: the actual page of the dataset.
        """

        assert isinstance(index, int) and index >= 0, (
            "Index must be a non-negative integer."
        )
        assert 0 <= index < len(self.__dataset), "Index out of range."

        data = []
        next_index = index
        while len(data) < page_size:
            if next_index in self.__indexed_dataset:
                data.append(self.__indexed_dataset[next_index])
            next_index += 1

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index if next_index < len(self.__dataset)
            else None
        }
