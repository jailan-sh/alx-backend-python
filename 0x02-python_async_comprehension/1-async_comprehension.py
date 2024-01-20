#!/usr/bin/env python3
"""
make Async Generator
"""
import asyncio
import random
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """
    collect 10 random numbers using an async comprehensing over async_generator
    return the 10 random numbers.
    """
    return [value async for value in async_generator()]
