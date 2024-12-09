#!/usr/bin/env python3

"""
Module that contains the coroutine async_generator.
This coroutine generates random numbers asynchronously.
"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> Generator[float, None]:

    """
    Coroutine that generates 10 random numbers between 0 and 10.
    It waits asynchronously for 1 second between each generation.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
