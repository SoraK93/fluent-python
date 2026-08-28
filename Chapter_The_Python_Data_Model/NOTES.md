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
