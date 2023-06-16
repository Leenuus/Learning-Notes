"""navie coroutine"""

import asyncio
from asyncio.exceptions import CancelledError
from itertools import cycle
import time
from math import sqrt

async def spin(msg: str):
    character = "\\|/-"
    length = 0
    for c in cycle(character):
        status = f"\r{c} {msg}"
        length = len(status)
        print(status, end='', flush=True)
        try:
            await asyncio.sleep(0.1)
        except CancelledError:
            break
    blanks = ' ' * length
    print(f"\r{blanks}\r", end='')

async def slow():
    """do something slow"""
    # time.sleep() block this thread, the control never yield back to event loop, so no spin displayed using time.sleep
    # time.sleep(3)
    # same result for is_prime
    # result = is_prime(5000_111_000_222_021)
    result = await asyncio.sleep(3)
    return result

def is_prime(a: int) -> bool:
    """a blocking cpu-intensive task"""
    if a < 2:
        return False
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    s = sqrt(a)
    for i in range(3, int(s) + 1, 2):
        if a % i == 0:
            return False
    return True

async def supervisor():
    """wrap spin with a task"""
    # register a task, return task handle, the task start
    task = asyncio.create_task(spin("do slow thing"))
    # keep polling result
    result = await slow()
    # raise CancelledError in the task
    task.cancel()
    return result

def main():
    """main entry"""
    # start event loop
    result = asyncio.run(supervisor())
    print(result)

if __name__ == '__main__':
    main()

