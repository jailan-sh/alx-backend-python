#!/usr/bin/env python3
"""
a function task_wait_random that takes an integer max_delay
returns a asyncio.Task
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ returns a asyncio.Task"""
    delays = await asyncio.gather(*(task_wait_random(max_delay)
                                    for _ in range(n)))
    return sorted(delays)
