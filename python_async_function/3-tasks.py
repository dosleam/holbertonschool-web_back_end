#!/usr/bin/env python3

"""
module 3-tasks
"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

"""
import asyncio and wait_random
"""


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio task to run the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay for the wait_random function.

    Returns:
        asyncio.Task: An asyncio task that executes wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))
