#!/usr/bin/env python3
import random
import asyncio


async def wait_random(max_delay: int=10) -> float:
    """returns a random delay between 0 and 10 secondsand eventually """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
