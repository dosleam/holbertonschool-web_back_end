#!/usr/bin/env python3
"""
Module that contains the coroutine async_comprehension.
This coroutine collects 10 random numbers from async_generator
using an asynchronous list comprehension.
"""


from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:

    """
    Coroutine that collects 10 random numbers from async_generator
    using an async comprehension and returns them as a list.

    Returns:
        List[float]: A list of 10 random floating-point numbers.
    """
    return [number async for number in async_generator()]
