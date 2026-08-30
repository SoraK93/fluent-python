![Python Logo](https://www.python.org/static/img/python-logo.png)
# Data Model

## How Special Methods Are Used
Special methods are meant to be called by Python interpreter, and not by you. Like you don't write `object.__len__()`, instead you write `len(my_object)`, and if my_object is an instance of a user-defined class, then Python calls the `__len__` method you implemented.

The interpreter takes a shortcut when built-in types like list, str, bytearray, or extensions like numpy array are used. Pythons variable type collection written in C called `PyVarObject`, which has an `ob_size` field holding the number of items in the collection.  
This is the reason, why calling `len()` retrieves the value so fast.

> [!IMPORTANT]
> Special method call is implicit. Notmally, your code should not have many direct calls to special methods. Unless I am doingg a lot of metaprogramming, I should be implementing special methods more often than invokingg them explicitly.  
If I need to invoke a special method, it is usually better to call the related built-in function (e.g., len, iter, str, etc.).

## Emulating Numeric Types
This <u>[example](./two-dimensional-vector-class/vector2d.py)</u> implements two operators: + and *, to show basic usage of `__add__` and `__mul__`. In both cases, the methods create and return a new instance of Ventor, and do not modify either operand--`self` or `other` are merely read.

This is the expected behavior of **Infix operator**: to create new objects and not touch their operands.

## String Representation
The `__repr__` special method is called by the repr built-in to get the string representation of the object for inspection. Without a custom `__repr__`, Python's console would display a Vector instance `<Vector object at 0x10e100070>`.
```Python
"""
f-string in our `__repr__` uses `!r` to get the 
standard representation of the attributes to be displayed.
"""
def __repr__(self):
    return f'Vector({self.x!r}, {self.y!r})'
```
The string returned by `__repr__` should be unambiguous and, if possible, match the source code necessary to re-create the represented object.

> [!NOTE]
> `__str__` is called by the `str()` built-in and implicitly used by the print function. It should return a string suitable for display to end users.
Soemtimes string returned by `__repr__` is user-friendly, this makes `__str__` implementation unnecessary. Because implementation inherited from the object class calls `__repr__` as a fallback.
[What is the difference between `__str__` and `__repr__` in Python?](https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr/1436756#1436756)

## Boolean Value of a Custom Type
To determine whether a value x is *truthy* or *falsy*, Python applies `bool(x)`, which returns either `True` or `False`. Such expressions can be used on controlling statement like `if` or `while`, or as operands to `and`, `or` and `not`. Basically, `bool(x)` calls `x.__bool__()` and uses the result.

> <small>**DEFAULT BEHAVIOUR:** If `__bool__` is not implemented, Python tries to invoke `x.__len__()`, and if that returns zero, bool returns `False`. Otherwise bool returns `True`.</small>

The explicit conversion to bool is needed because `__bool__` must return a Boolean, and or returns either operand as is: `x or y` evaluates to x if that is truthy, otherwise the result is y, whatever that is.

## Collection API  
The Collection ABC unifies the three essential interfaces that every collection should implement:
- `Iterable` to support `for`, unpacking and other forms of iteration
- `Sized` to supprt the `len` built-in function
- `Container` to support the `in` operator

Three very important specializations of `Collection` are:
- `Sequence`, formatizing the interface of built-ins like `list` and `str`
- `Mapping`, implemented by `dict`, `collections.defaultdict`, etc.
- `Set, the interface of the `set` and `frozenset` built-in types
> <small>Sequence are reversible, because it supports arbitrary ordering of their contents, while mappings and sets do not.</small>

<p align="center">
  <img src="./Ref-Image/WhatsApp%20Image%202026-08-29%20at%2018.17.18.jpeg" alt="UML class diagram">
  <i><small>All the classes in the diagram are ABCs--abstract base classes.</small></i>
</p>

> [!NOTE]
> Augmented assignments are shortcuts combining an infix operator with variable assignment, e.g., a += b

## Why len Is Not a Method
`len` is not called as a method bacause it gets special treatment as part of the Python Data Model, just like `abs`. `len(x)` runes very last when x is an instance of a built-in type. No method call is called for the built-in objects of CPython: the length is simply read from the field in a C struct.

> [!TIP]
> 1. Practicality beats purity.
> 2. Special cases aren't special enough to break the rules.

## Summary

By implementing special methods, your objects can behave like the built-in types, enabling the expressive coding style the community considers Pythonic.

Python offers a rich selection of numeric types, from the built-ins to `decimal.Decimal` and `fractions.Fraction`, all supporting infix arithmentic operators. The NumPy data science libraries support infix operators with matrices and tensors.