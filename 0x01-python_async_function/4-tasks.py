#!/usr/bin/env python3
"""
a function task_wait_random that takes an integer max_delay
returns a asyncio.Task
"""
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n, max_delay):
    """ returns a asyncio.Task"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
