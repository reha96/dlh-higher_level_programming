# Python — Classes and Objects

A progressive study of Object-Oriented Programming in Python: class definition, encapsulation, properties, data validation, and data structures built from classes.

---

## Learning Objectives

| # | Concept |
|---|---------|
| 1 | What is OOP |
| 2 | "first-class everything" |
| 3 | What is a class |
| 4 | What is an object and an instance |
| 5 | What is the difference between a class and an object or instance |
| 6 | What is an attribute |
| 7 | What are and how to use public, protected, and private attributes |
| 8 | What is `self` |
| 9 | What is a method |
| 10 | What is the special `__init__` method and how to use it |
| 11 | What is Data Abstraction, Data Encapsulation, and Information Hiding |
| 12 | What is a property |
| 13 | What is the difference between an attribute and a property in Python |
| 14 | How to use getter and setter methods with `@property` |
| 15 | How to dynamically create arbitrary new attributes for existing instances |
| 16 | How to bind attributes to objects and classes |

---

## Task-by-Task Reference

Each task below highlights the **unique challenge** it posed and the **new technique** introduced to solve it — techniques from earlier tasks are not repeated. Use this as a quick revision guide.

---

### Task 0 — Empty Square Class (`0-square.py`)

**Challenge:** Define the simplest possible class — introducing the `class` keyword, module
and class documentation, and the `pass` placeholder.

**Approach:** Use `class Square:` with a docstring describing the class. The body contains
only `pass` since no attributes or methods are needed yet. Add a module-level docstring at
the top of the file.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `class ClassName:` | Define a new class |
| `"""module docstring"""` | Document the file/module at the top |
| `"""class docstring"""` | Document the class immediately after its definition |
| `pass` | Placeholder — satisfies Python's requirement that a block must contain at least one statement |

> **Key takeaway:** A class is a blueprint for creating objects. An empty class is valid
> Python and can still be instantiated. Docstrings (`"""..."""`) are the standard way to
> document modules, classes, and functions.

---

### Task 1 — Square with Private Size (`1-square.py`)

**Challenge:** Give the Square class an attribute that cannot be directly accessed from
outside — introducing the constructor, `self`, and private attributes.

**Approach:** Define `def __init__(self, size):` — the constructor. Inside, store
`self.__size = size`. The double-underscore prefix (`__`) triggers Python's **name
mangling**, making the attribute private (not truly hidden, but renamed to `_Square__size`).

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `def __init__(self, param):` | Constructor — called automatically when an object is created |
| `self` | Reference to the current instance — must be the first parameter of every method |
| `self.__size` | Private attribute — double underscore triggers name mangling for encapsulation |

> **Key takeaway:** `__init__` is Python's constructor. `self` refers to the instance being
> created. `__name` (double underscore) is Python's convention for private attributes —
> they're name-mangled to `_ClassName__name` to prevent accidental external access.

---

### Task 2 — Size Validation (`2-square.py`)

**Challenge:** Ensure the size attribute always holds a valid value — introducing input
validation in the constructor with type and value checks.

**Approach:** In `__init__`, check `type(size) is not int` and `raise TypeError("…")`.
Check `size < 0` and `raise ValueError("…")`. Only assign `self.__size = size` if both
checks pass. Use `size=0` as a default parameter value.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `type(value) is not int` | Type-check an argument before using it |
| `raise TypeError("message")` in constructor | Reject invalid input by raising an exception |
| `raise ValueError("message")` | Raise a different exception type for a different kind of invalidity |
| Default parameter `size=0` | Provide a fallback value when no argument is given |

> **Key takeaway:** Validation in the constructor guarantees an object is never created in an
> invalid state. `TypeError` and `ValueError` are the standard exceptions for bad arguments.

---

### Task 3 — Area Method (`3-square.py`)

**Challenge:** Give the Square the ability to compute its own area — introducing instance
methods and accessing private attributes from within the class.

**Approach:** Define `def area(self):` that returns `self.__size ** 2`. The method uses the
private attribute via `self.__size` (which works because the access is inside the class).
No parameters besides `self` — the data comes from the instance's own state.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `def method(self):` | Define an instance method — operates on `self`'s data |
| `self.__private_attr` in method | Access a private attribute from within its own class |
| `return self.__size ** 2` | Compute and return a value based on instance state |

> **Key takeaway:** Methods are functions defined inside a class. They always take `self` as
> the first parameter and can freely access private attributes of the same instance.

---

### Task 4 — Property Getter and Setter (`4-square.py`)

**Challenge:** Provide controlled access to the private `__size` attribute from outside the
class — introducing Python's `@property` decorator for getters and setters.

**Approach:** Decorate `def size(self):` with `@property` (the getter) and `def size(self, value):`
with `@size.setter` (the setter). The getter simply returns `self.__size`. The setter
repeats the validation from the constructor. Now `square.size` works like a regular attribute
access but runs the getter/setter code.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `@property` | Turn a method into a read-only attribute-like accessor (getter) |
| `@name.setter` | Define a setter for the property — called on `obj.name = value` |
| Property pattern | Encapsulate a private attribute behind getter/setter methods |

> **Key takeaway:** `@property` lets you replace `get_size()`/`set_size()` with natural
> `obj.size` syntax while still running validation and logic on every access. This is
> Python's idiomatic encapsulation.

---

### Task 5 — Print the Square (`5-square.py`)

**Challenge:** Visually render the square using `#` characters — introducing methods that
produce formatted output and conditionally handle edge cases (size 0).

**Approach:** Define `def my_print(self):`. If `self.size == 0`, print a blank line.
Otherwise, use nested `for` loops: outer loop for rows (`range(self.size)`), inner loop for
columns (`range(self.size)`). Print `#` without newline via `end=""`, then print a newline
after each row.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| Nested `for` loops for 2D output | Render a grid: rows × columns |
| `print("#", end="")` + `print("")` | Build a line character by character, then end the row |
| Edge case: `if self.size == 0` | Handle the zero-size case by printing only a newline |

> **Key takeaway:** Printing a 2D shape requires nested loops — one for rows, one for columns.
> The `end=""` trick prints characters side-by-side; a bare `print("")` ends the line.

---

### Task 6 — Position and Offset (`6-square.py`)

**Challenge:** Add a position tuple that controls where the square prints on screen —
introducing tuple validation, the `all()` function, and offset-based printing.

**Approach:** Add a `position` property with getter and setter. The setter validates: must be
a tuple, length 2, both elements positive integers — using `isinstance()`, `len()`, and
`all(isinstance(p, int) and p >= 0 for p in position)`. In `my_print()`, print blank lines
for vertical offset and prepend spaces for horizontal offset using `" " * n`.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `isinstance(obj, tuple)` | Check if an object is of a specific type (preferred over `type()`) |
| `all(condition for item in iterable)` | Check that all elements satisfy a condition |
| Generator expression `(p >= 0 for p in position)` | Inline iteration for `all()` — no list creation needed |
| `" " * n` string repetition for offset | Print `n` spaces for horizontal positioning |
| Multi-property class (size + position) | Manage two independent encapsulated attributes |

> **Key takeaway:** `isinstance()` is more flexible than `type() is` because it supports
> inheritance. `all()` with a generator expression is a clean way to validate every element.
> String repetition (`" " * n`) is a concise way to create padding.

---

### Task 7 — Singly Linked List (`100-singly_linked_list.py`)

**Challenge:** Build a complete singly linked list data structure from scratch using classes —
introducing node-based data structures, sorted insertion, and custom string representation.

**Approach:** Define a `Node` class with `data` (validated integer) and `next_node` (must be
Node or None) properties. Define a `SinglyLinkedList` class with a private `__head`. Implement
`sorted_insert(value)` that walks the list to find the correct position, handling insertion
at head, middle, and end. Override `__str__` to traverse the list and return `"\n".join(values)`.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| Node class with property-validated `next_node` | Validate that `next_node` is either a Node instance or None |
| `isinstance(value, Node)` type check | Ensure linked references are of the correct class |
| Private `__head` in container class | Hide the list's internal structure from external access |
| Linked list traversal (`while current is not None`) | Walk node-by-node through a linked structure |
| `sorted_insert()` algorithm | Insert a value while maintaining sorted order |
| `__str__()` method | Define how the object is printed — `print(sll)` calls `__str__` |
| `"\n".join(list_of_strings)` | Join collected values with newlines for multi-line output |

> **Key takeaway:** A linked list is built from Node objects that each hold data and a
> reference to the next node. `__str__` gives your class a human-readable string representation.
> Traversal (`while current`) is the fundamental operation for all linked list algorithms.

---

### Task 8 — Square with Position (`101-square.py`)

**Challenge:** Enhance the Square class with a `position` attribute — a tuple of two positive
integers that controls where the square is printed on screen — introducing tuple validation
and multi-property classes.

**Approach:** Add a `position` property with getter and setter. The setter validates that
`position` is a tuple of exactly 2 positive integers using `isinstance()`, `len()`, and
`all()` with a generator. The `my_print()` method uses `position[1]` for vertical offset
(number of blank lines) and `position[0]` for horizontal offset (spaces before `#`).
Overload `__str__` to produce the same visual output as a string.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| Tuple validation with `isinstance()`, `len()`, `all()` | Validate compound position data in one check |
| `position[1]` vertical offset | Print blank lines before the square |
| `position[0]` horizontal padding | `" " * pos[0]` shifts each row right |
| `__str__` for visual output | Return the same printed representation as a string |

> **Key takeaway:** The `position` tuple encapsulates 2D spatial information. Tuple
> validation ensures both dimensions are valid positive integers. `__str__` and `my_print()`
> produce identical visuals — one as a return value, the other as side-effect output.

---

### Task 9 — Square Comparison Operators (`102-square.py`)

**Challenge:** Make Square instances comparable by area using Python's rich comparison
operators — introducing the full set of dunder comparison methods.

**Approach:** Implement all six comparison dunders: `__lt__` (<), `__le__` (<=), `__eq__` (==),
`__ne__` (!=), `__gt__` (>), `__ge__` (>=). Each compares `self.area()` against `other.area()`.
Only define `size` (no position needed here), focusing purely on comparison semantics.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `__lt__(self, other)` | Less-than comparison — `square1 < square2` |
| `__le__(self, other)` | Less-than-or-equal — `square1 <= square2` |
| `__eq__(self, other)` | Equality — `square1 == square2` |
| `__ne__(self, other)` | Not-equal — `square1 != square2` |
| `__gt__(self, other)` | Greater-than — `square1 > square2` |
| `__ge__(self, other)` | Greater-than-or-equal — `square1 >= square2` |
| Comparison by computed property | Compare `self.area()` methods, not raw attributes |

> **Key takeaway:** Python's rich comparison dunders (`__lt__`, `__eq__`, etc.) let your
> objects work with `==`, `<`, `>`, and sorting. Define all six for consistency — Python
> can infer some from others, but explicit is better. Comparing by area rather than size
> demonstrates indirection: equality is based on a computed value.

---

## Technique Inventory

| Task | New technique summarized | Category |
|------|--------------------------|----------|
| 0 | `class`, docstrings, `pass` | OOP Basics |
| 1 | `__init__`, `self`, `__` private attributes | OOP Basics |
| 2 | Type/value validation in constructor, `raise` exceptions | OOP Basics |
| 3 | Instance method, `self.__attr` access, computed return | OOP Methods |
| 4 | `@property` getter, `@name.setter`, encapsulation pattern | Properties |
| 5 | Nested loops for 2D output, `end=""` printing, edge case handling | OOP Methods |
| 6 | `isinstance()`, `all()` generator, `len()` for tuple, `" " * n` offset | Validation & Data |
| 7 | Node class, linked list traversal, `sorted_insert`, `__str__`, `"\n".join()` | Data Structures |
| 8 | Tuple position, vertical/horizontal offset, `__str__` for visual output | OOP & Position |
| 9 | Rich comparison dunders (`__lt__`–`__ge__`), compare by `area()` | OOP & Comparison |

---

## Resources

- [9. Classes — Python Docs](https://docs.python.org/3/tutorial/classes.html)
- [Built-in Functions — `isinstance()`, `all()`](https://docs.python.org/3/library/functions.html)
- [The `@property` decorator](https://docs.python.org/3/library/functions.html#property)
- [Private Variables — Python Docs](https://docs.python.org/3/tutorial/classes.html#private-variables)
- [Rich Comparison Methods — Python Data Model](https://docs.python.org/3/reference/datamodel.html#object.__lt__)
- [Data model — `__str__` and `__init__`](https://docs.python.org/3/reference/datamodel.html)