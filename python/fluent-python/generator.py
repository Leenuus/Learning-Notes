"""practice of chapter generator"""

def tree(cls , level=0):
    """a generator yield all subclass of a class"""
    yield cls.__name__, level
    for sub in cls.__subclasses__():
        yield from tree(sub, level + 1)

def display(cls):
    for cls, level in tree(cls, 0):
        indent = '  ' * level 
        print(f"{indent}{cls}")

if __name__ == "__main__":
    display(BaseException)
