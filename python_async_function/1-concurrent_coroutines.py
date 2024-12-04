#!/usr/bin/env python3

"""
module 1-concurrent_coroutines
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

"""
import asyncio, List and t0 module
"""


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes wait_random n times with a given max_delay,
    and returns a list of deadlines sorted in ascending order.

    Args:
        n (int): Number of wait_random executions
        max_delay (int): Maximum delay for each call to wait_random.

    Returns:
        List[float]: List of deadlines sorted in ascending order.
    """
    delays = []

    # Lancer n tâches concurrentes
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Attendre que chaque tâche se termine et insérer chaque délai dans l'ordre
    for finished_task in asyncio.as_completed(tasks):
        delay = await finished_task

        # Insertion dans la liste tout en maintenant l'ordre croissant
        inserted = False
        for i in range(len(delays)):
            if delay < delays[i]:
                delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            delays.append(delay)

    return delays
