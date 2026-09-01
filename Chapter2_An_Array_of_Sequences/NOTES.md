![Python Logo](https://www.python.org/static/img/python-logo.png)

Since, Python inherits from ABC the uniform handling of sequences. Strings, lists, byte sequences, arrays, XML elements and database results they all share a rich set of common operations like iteration, slicing, sorting, and concatenation.

Understanding all this will help us save time and prevents from reinventing the wheel.

## Overview of Built-In Sequences

The standard library offers a rich selection of sequence types implemented in C:

1. _Container Sequences_: Can hold items of different types, including nested containers. Some examples: `list`, `tuple`, and `collections.deque`.
   _Example: `(9.46, 'cat', [2.08, 4.29])`_
2. _Flat Sequences_: Hold items of one simple type. Some examples: `str`, `bytes`, and `array.arrray`. It is more compact, but they are limited to holding primitive machine values like bytes, integers, and floats.
   _Example: `array('d', [9.46, 2.08, 4.29])`_

<p align="center">
  <img src="./Ref-Image/simplified_memory_diagrams.jpeg" alt="Simplified Memory Diagram">
  <i><small>A container sequence holds references to the objects it contains, which may be of any type.<br>A flat sequence stores the value of its contents in its own memory space, not as distinct Python objects.</small></i>
</p>

3. _Mutable Sequences_: For example, `list`, `bytearray`, `array.array` and `collections.deque`.
4. _Immutable sequences_: Fot example, `typle`, `str`, and `bytes`.

> [!IMPORTANT]
> - Mutable sequences inherit all methods from immutable sequences, and implement several additional methods.
> - Common traits: mutable versus immutable, container versus flat.

<p align="center">
  <img src="./Ref-Image/simplified_UML_class_diagram.jpeg" alt="Simplified Memory Diagram">
  <i><small>A container sequence holds references to the objects it contains, which may be of any type.<br>A flat sequence stores the value of its contents in its own memory space, not as distinct Python objects.</small></i>
</p>

Every Python object in memory has a header with metadata. The simplest Python object, a float, has a value field and two metadata fields:

- `ob_refcnt`: the objet's reference count
- `ob_type`: a pointer to the object's type
- `ob_fval`: a C double holding the value of the float

## List Comprehensions and Generator Expressions
A quick way to build a sequence is using a list comprehension (if the target is a list) or a generator expression (for ther kinds of sequence).

Python programmers refer to list comprehensions as `listcomps`, generator expressions as `genexps`.

#### List comprehensions and Readability [[Example](./examples/listcomp.py)]
A `for` loop may be used to do lots of different things: scanning a sequence to count or pick items, computing aggregates (sums, averages), or any number of other tasks.

#### Local Scope Within Comprehensions and Generator Expressions [[Example](./examples/listcomp_scope.py)]
In Python 3, list comprehensions, generator expressions, and their siblings set and dict comprehensions, have a  local scope to hold the variables assigned in the for clause.
However, variables assigned with the "Walrus Operator" := remain accessible after those comprehensions or expressions return -- unlike local variables in a function.

> [!IMPORTANT]
> Walrus expression (:=) works when you're assigning and checking in the same expression
> ```python
> # Walrus expression doesn't work in this type of situation
> count = 0
> for item in my_list:
>     if item == x:
>         count += 1
> ```
> ```python
> # Here variable is assigned and checked in the same expression.
> if count:= my_list.count(x):
>     count += 1
> ```

#### Listcomps Versus map and filter [[Example](./examples/listcomp_map_filter.py)]
Listcomps are a one-trick pony: they build lists.

> [!NOTE]
> To generate data for other sequence types, a genexp is the way to go

#### Cartesian Products [[Example](./examples/cartesian_product.py)]
Listcomps can build lists from the Cartesian product of two or more iterables. The items that make up the Cartesian product are tuples made from items from every input iterable.

#### Generator Expressions [[Example](./examples/genexp.py)]
A genexp saves memory because it yields items one by one using the iterator protocol instead of building a while list just to feed another constructor.
> Uses the same syntax as listcomps, but are enclosed in parentheses rather than brackets.

## Tuples Are Not Just Immutable Lists
Tuples can be used as immutable lists and also as records with no field names.

#### Tuples as Records
