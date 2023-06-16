from re import L
from time import perf_counter
from multiprocessing import queues, Process, SimpleQueue, cpu_count
from typing import NamedTuple
from math import sqrt

class Result(NamedTuple):
    n: int
    is_prime: bool
    time: float

JobQueue = queues.SimpleQueue[int]
ResultQueue = queues.SimpleQueue[Result]

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    root = sqrt(n)
    for i in range(3, int(root) + 1, 2):
        if n % i == 0:
            return False
    return True

def check(n: int) -> Result:
    start = perf_counter()
    res = is_prime(n)
    return Result(n, res, perf_counter() - start)

def worker(jobs: JobQueue, results: ResultQueue):
    while n 
