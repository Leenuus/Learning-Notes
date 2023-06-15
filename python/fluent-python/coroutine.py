from typing import NamedTuple

class Result(NamedTuple):
    count: int
    avg: float

class Stop:
    pass

def average(verbose: bool = False):
    total = 0
    count = 0
    avg = 0
    while True:
        term = yield
        if verbose:
            print(f"Received: {term}")
            print(f"Accumulated: {total}")
        if isinstance(term, Stop):
            break
        total += term
        count += 1
        avg = total / count
    return Result(count, avg)
        
