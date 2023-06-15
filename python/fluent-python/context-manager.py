"""a simple self-made context-manager class"""
from contextlib import AbstractContextManager
import contextlib
import sys
from types import TracebackType

def test():
    ...

class Manager(AbstractContextManager):

    def __enter__(self):
        print("enter context manager")

    def __exit__(self, exc_type, exc_value, traceback):
        print("exit from context manager")


class Mirror(AbstractContextManager):

    def __enter__(self):
        self.write = sys.stdout.write
        sys.stdout.write = self.reverse
        return 'something'

    def reverse(self, text: str):
        return self.write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.write
        return True

@contextlib.contextmanager
def mirror():
    origin_writer = sys.stdout.write
    sys.stdout.write = lambda s: origin_writer(s[::-1])
    yield "CBA"
    sys.stdout.write = origin_writer

@mirror()
def also_work_as_decorator():
    print("also_work_as_decorator")

if __name__ == "__main__":
    with Manager():
        print("inside the context manager")

    with mirror() as enter_return:
        print("hello")
        print("see you")

    print(enter_return)

    also_work_as_decorator()
