#!/usr/bin/env python3

"""
module 0-basic_async_syntax
"""


import asyncio
import random

"""
import asyncio and random
"""


async def wait_random(max_delay: int = 10) -> float:
    """
    Coroutine that waits for a random delay between 0 and max_delay seconds
    and returns this delay.

    Args:
        max_delay (int): The maximum duration of the delay (default 10).

    Returns:
        float: The length of the delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
