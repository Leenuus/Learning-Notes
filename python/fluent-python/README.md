# fluent-python

## part1 data structures

### primitive compound data structures

1. match case syntax, `int() float() str()` runtime type cheking
2. dict usage: dict comprehesion; `__missing__` method for fallback; inherit `collections.UserDict` to build custom dict type; use `typing.MappingProxyType` to build immutable mapping; `keys()` and `values()` return a view of mapping, views are iterable and don't support subscript, when the dict update, the view update too.
3. trick to reserve order and filter duplicated of a list: `dict.from_keys(l).keys()`
4. set and frozenset, the former is mutable, and the latter is immutable; how to use set comprehension; set typing `{...}`; empty set `set()` and set literal eg. `{1, 2, 3}`; subset relationship `s1 >= s2` means s2 is a subset of s1, without `=` means proper subset(真子集)

### bytes and str

1. `bytes('str', encoding='utf8')`
2. difference between slice of bytes, still bytes; and index of bytes, a byte, a integer smaller than 256
3. use `unicodedata.normalize` to normalize different form of same string, always normalize string into `NFC` composed type before saving(default from keyboard drivesr)

### data class builder

1. `__annotation__` in dataclass and NamedTuple holds the type of a field, which you can get using `inspect.get_annotation(MyClass)` and `typing.get_type_hints(Myclass)`
2. make class on the fly(in runtime), use `namedtuple` and `dataclasses.make_dataclass` functions

## part2 functions as object

1. how to write custom decorator, both class-based and function-based; how to write decorator receiving arguments
2. some tools from functools, such as wrapper
3. design pattern such as adapter pattern implemented with functions
4. use cases of decorator: enhance a function, add feature to a function, dynamic plugin register over different modules
5. `nonlocal` keyword helps build javascript-like "stateful function"
6. position-only arguments, before `/`; keyword-only arguments after `*`

## part3 class and protocols

1. subclass `Protocol` to help typing checker
2. when to use `__slot__`
3. representation: `__str__`, `__repr__`(import reprlib for hep), `__format__(self, format_arg)`; how to use `format()`, f-str, `s.format(data)`
4. immutable type, hash, eq
5. sequence method, `__getitem__`, `__setitem__`; how to support slice(tuple slice syntax: separated by comma in the brackets), in numpy, tuple slice is used to return multiple slice at a time
6. support match-case syntax by `__match_args__`
7. a faster `__eq__` with iterator adapter zip and len built-in

## part4 control flow

1. itertools usage, drop_while, cycle, count
2. generator(classic), use `.send` to build a generator, use generator to build a context manager
3. use asyncio. how to start a event loop, how to register a task
4. use thread for io-bound tasks; use process for cpu-bound tasks. use Event to send a signal to a thread instance, handle this exception inside thread; 
5. use executor to spawn thread and process, `concurrent.futures` module

## part5 metaprogramming

1. how to use `__getattr__`
2. how to write custom descriptor

### meta class

no done yet
