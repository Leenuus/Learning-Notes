from typing import NamedTuple

class Result(NamedTuple):
    count: int
    avg: float

class Stop:
    pass

def average(verbose: bool = False):
    """classic coroutine in generator flavor"""
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
        
if __name__ == "__main__":
    co = average()
    # the first argument to send must be None
    # or use next(co)
    co.send(None)
    co.send(10)
    co.send(20)
    co.send(30)
    # send Stop signal to stop iteration, raise a StopIteration with field named after value holding the return value
    try:
        co.send(Stop())
    except StopIteration as exc:
        result = exc.value
        print(result)


