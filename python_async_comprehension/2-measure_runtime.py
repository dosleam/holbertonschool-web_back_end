#!/usr/bin/env python3

"""
Module that contains the coroutine measure_runtime.
This coroutine measures the runtime of executing async_comprehension
four times in parallel using asyncio.gather.
"""


import asyncio
import time
from typing import List


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:

    """
    Coroutine that measures the total runtime of running async_comprehension
    four times in parallel using asyncio.gather.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()

    return end_time - start_time
