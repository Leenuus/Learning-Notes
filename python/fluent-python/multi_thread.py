from itertools import cycle
from threading import Event, Thread
from time import sleep

def spin(msg: str, done: Event):
    character = "\\|/-"
    length = 0
    for c in cycle(character):
        status = f"\r{c} {msg}"
        length = len(status)
        print(status, end='', flush=True)
        if done.wait(0.1):
            break
    # We need to clear the screen here
    # After loop, 1st \r sets the buffer cursor to the start of line. print blanks to clear previous string, and then one more \r brings the cursor back to line start
    blanks = ' ' * length
    print(f"\r{blanks}\r", end='')

def slow() -> int:
    """do something slow"""
    sleep(3)
    return 42

def supervisor():
    """wrap spin with a task"""
    done = Event()
    task = Thread(target=spin, args=('do something slow', done))
    task.start()
    result = slow()
    done.set()
    task.join()
    return result

def main():
    result = supervisor()
    print(result)

if __name__ == '__main__':
    main()

