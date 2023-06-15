# fluent-python

## part1 data structures

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

## part5 metaprogramming

1. how to use `__getattr__`
2. how to write custom descriptor
