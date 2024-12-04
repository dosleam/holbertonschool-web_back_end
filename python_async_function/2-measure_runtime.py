#!/usr/bin/env python3

"""
module 2-measure_runtime
"""


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n

"""
import time asyncio and wait_n
"""


def measure_time(n: int, max_delay: int) -> float:
    """

    Args:
        n (int): argument passed to wait_n
        max_delay (int): argument passed to wait_n

    Returns:
        float: average time
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
