#! /usr/bin/python3

from concurrent import futures
from time import perf_counter
from math import sqrt
from operator import itemgetter

def is_prime(n: int):
    if n < 2:
        return (n, False)
    if n == 2:
        return (n, True)
    if n % 2 == 0:
        return (n, False)
    # divide iteration job into pieces
    root = int(sqrt(n)) + 1
    for i in range(3, root, 2):
        if n % i == 0:
            return (n, False)
    return (n, True)

def main():
    t0 = perf_counter()
    results = []
    with futures.ProcessPoolExecutor() as exec:
        jobs = []
        for n in NUMBERS:
            job = exec.submit(is_prime, n)
            jobs.append(job)
        for job in futures.as_completed(jobs):
            result = job.result()
            t1 = perf_counter()
            results.append(result)
            label = 'P' if result[1] else ' '
            print(f"{result[0]} {label} {t1 - t0:9.6}s")
    return results
    
def test_is_prime():
    results: list[tuple[int, bool]] = main()
    results.sort(key=itemgetter(0))
    assert results == PRIME_FIXTURE

PRIME_FIXTURE = [
    (2, True),
    (142702110479723, True),
    (299593572317531, True),
    (3333333333333301, True),
    (3333333333333333, False),
    (3333335652092209, False),
    (4444444444444423, True),
    (4444444444444444, False),
    (4444444488888889, False),
    (5555553133149889, False),
    (5555555555555503, True),
    (5555555555555555, False),
    (6666666666666666, False),
    (6666666666666719, True),
    (6666667141414921, False),
    (7777777536340681, False),
    (7777777777777753, True),
    (7777777777777777, False),
    (9999999999999917, True),
    (9999999999999999, False),
]

NUMBERS = [n for n, _ in PRIME_FIXTURE]

if __name__ == "__main__":
    main()
