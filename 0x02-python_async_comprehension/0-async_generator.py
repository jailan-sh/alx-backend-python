#!/usr/bin/env python3
"""
make Async Generator
"""
import asyncio
import random


async def async_generator() -> int:
    """
    return await list between 0-10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
