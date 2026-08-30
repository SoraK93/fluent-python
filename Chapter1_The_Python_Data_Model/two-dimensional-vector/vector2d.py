"""
A simplistic class demonstrating some special methods

It is simplistic for didatic reasons. It lacks proper error handling, especially in the ``__add__`` and ``__mul__`` methods.

Addition::
>>> v1 = Vector(2,4)
>>> v2 = Vector(2,1)
>>>  v1 + v2
Vector(4,5)

Absolute value::
>>> v = Vector(3,4)
>>> abs(v)
5.0

Scalar multiplication::
>>> v * 3
Vector(9, 12)
>>> abs(v * 3)
15.0

This example implements two operators: + and *, to show basic usage of __add__ and __mul__. In both cases, the methods create and return a new instance of Ventor, and do not modify either operand--`self` or `other` are merely read.

This is the expected behavior of infix operator: to create new objects and not touch their operands.
"""

import math

class Vector:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        # 
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(2, 3)
# This print shows a readable output instead of <Vector object at 0x10e100070> because of __repr__ implementation inside the Vector class.
print(v1) 