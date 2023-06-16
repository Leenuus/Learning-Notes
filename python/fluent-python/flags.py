#! /usr/bin/python3
from time import perf_counter
from pathlib import Path
from typing import Callable
from concurrent import futures

import httpx

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()  # <2>

BASE_URL = 'https://www.fluentpython.com/data/flags'  # <3>
DEST_DIR = Path('downloaded')                         # <4>

def save_image(filename: str, image: bytes):
    """easy path operation for Path"""
    (DEST_DIR/filename).write_bytes(image)

def download_flag(flag_name: str):
    url = f"{BASE_URL}/{flag_name}/{flag_name}.gif".lower()
    resp = httpx.get(url, follow_redirects=True, timeout=4.1)
    # raise exception when status is not 2xx
    resp.raise_for_status()
    return resp.content

def download_one(flag_name: str):
    try:
        image = download_flag(flag_name)
        save_image(f"{flag_name}.gif", image)
    except Exception as e:
        print(f"\ndownload {flag_name} fails, {e}")
    print(flag_name, end=' ', flush=True)

def download_many_sequential(flags: list[str] = POP20_CC) -> int:
    i = 0
    for flag in flags:
        download_one(flag)
    return i

def download_many_thread_pool(flags: list[str] = POP20_CC) -> int:
    with futures.ThreadPoolExecutor() as executor:
        res = executor.map(download_one, flags)
    return len(list(res))

def download_many_thread_future(flags: list[str] = POP20_CC) -> int:
    todo = []
    i = 0
    with futures.ThreadPoolExecutor() as executor:
        for flag in flags:
            future = executor.submit(download_one, flag)
            todo.append(future)
        for _ in futures.as_completed(todo):
            i += 1
    return i

def main(downloader: Callable[[list[str]], int]) -> None:  # <13>
    DEST_DIR.mkdir(exist_ok=True)                          # <14>
    t0 = perf_counter()                               # <15>
    count = downloader(POP20_CC)
    elapsed = perf_counter() - t0
    print(f'\n{count} downloads in {elapsed:.2f}s')

if __name__ == '__main__':
    # main(download_many_sequential)
    # main(download_many_thread_pool)
    main(download_many_thread_future)
