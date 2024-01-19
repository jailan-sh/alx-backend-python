#!/usr/bin/env python3
import random
import asyncio
from . import wait_random


async def wait_n(n, max_delay):
    """returns a random delay between 0 and 10 secondsand eventually """
    
