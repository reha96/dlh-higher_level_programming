# Python — More Classes and Objects

A progressive study of advanced OOP concepts: dunder methods, class variables, static methods, class methods, and the object lifecycle.

---

## Learning Objectives

| # | Concept |
|---|---------|
| 1 | What are the special `__str__` and `__repr__` methods and how to use them |
| 2 | What is the difference between `__str__` and `__repr__` |
| 3 | What is a class attribute |
| 4 | What is the difference between an object attribute and a class attribute |
| 5 | What is a class method |
| 6 | What is a static method |
| 7 | How to dynamically create arbitrary new attributes for existing instances |
| 8 | How to bind attributes to objects and classes |
| 9 | What is and what does `__dict__` contain for a class and an instance |
| 10 | What is the special `__del__` method and how to use it |
| 11 | How does Python find the attributes of an object or class |

---

## Task-by-Task Reference

Each task below highlights the **unique challenge** it posed and the **new technique** introduced to solve it — techniques from earlier tasks are not repeated. Use this as a quick revision guide.

---

### Task 0 — Empty Rectangle Class (`0-rectangle.py`)

**Challenge:** Establish a new class hierarchy — the Rectangle — that will be progressively
enhanced across all subsequent tasks. Same pattern as the empty Square, but for a new type.

**Approach:** Define `class Rectangle:` with docstrings and `pass`. This is the starting
point for 9 more tasks that build layer by layer on the Rectangle blueprint.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| (Review) `class`, `"""docstring"""`, `pass` | Same foundational OOP patterns, applied to a new class |

> **Key takeaway:** Starting with an empty class is a deliberate design choice — it
> establishes the class name and lets you add features incrementally across tasks.

---

### Task 1 — Rectangle with Width and Height (`1-rectangle.py`)

**Challenge:** Manage TWO private attributes (width and height) with independent validation —
introducing multi-attribute classes and separate getter/setter pairs for each.

**Approach:** Define `__init__(self, width=0, height=0)` with separate `isinstance` and
value checks for each attribute. Create `@property` + `@width.setter` and `@property` +
`@height.setter` pairs — four decorators total, each with its own validation logic.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| Multiple private attributes (`__width`, `__height`) | A class can encapsulate more than one piece of data |
| Multiple property pairs | Each private attribute gets its own getter/setter independently |
| Separate validation per attribute | Each attribute validates its own type and value constraints |

> **Key takeaway:** Each private attribute deserves its own `@property` pair. The validation
> is duplicated in both the constructor and the setter because attributes can be set at
> creation time OR later via the property.

---

### Task 2 — Area and Perimeter (`2-rectangle.py`)

**Challenge:** Compute the rectangle's area and perimeter, handling the edge case where
either dimension is zero — introducing geometric methods and zero-value guards.

**Approach:** `area()` returns `width * height`. `perimeter()` checks if either dimension
is 0 and returns `0` (not `2*(0+5) = 10`), otherwise `2 * (width + height)`. Both methods
use only `self` — all data comes from the instance's own state.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `perimeter()` edge case: return `0` if `width == 0 or height == 0` | Detect degenerate (zero-area) rectangles |
| Geometric formula in a method | Encapsulate domain-specific math inside the class |

> **Key takeaway:** A zero-width or zero-height rectangle has a perimeter of 0, not
> `2*(0 + height)`. Always consider edge cases where standard formulas break down.

---

### Task 3 — String Representation (`3-rectangle.py`)

**Challenge:** Make `print(rect)` visually render the rectangle with `#` characters —
introducing Python's `__str__` dunder method.

**Approach:** Define `def __str__(self):`. If either dimension is 0, return `""`. Otherwise,
build a list of characters: append `#` for width, append `\n` for newlines between rows,
join with `"".join(out)`, and trim the trailing newline with `out[:-1]`.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `def __str__(self):` | Dunder method — called by `print(obj)` and `str(obj)` |
| List building + `"".join()` | Efficiently construct a multi-line string from pieces |
| `out[:-1]` trim | Remove the trailing newline from the final result |

> **Key takeaway:** `__str__` should return a human-readable string. It's called implicitly
> by `print()` and `str()`. Always return a string — never `print()` inside `__str__`.

---

### Task 4 — Repr Representation (`4-rectangle.py`)

**Challenge:** Provide a representation that can recreate the object — introducing `__repr__`
and distinguishing it from `__str__`.

**Approach:** Define `def __repr__(self):` that returns `f"Rectangle({self.__width}, {self.__height})"`.
This string is valid Python code that, if passed to `eval()`, would recreate an equal Rectangle.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `def __repr__(self):` | Dunder method — called by `repr(obj)` and in interactive interpreter |
| `f"ClassName({attr1}, {attr2})"` | Standard `__repr__` format — looks like the constructor call |

> **Key takeaway:** `__str__` is for users (readable), `__repr__` is for developers
> (unambiguous, ideally `eval()`-able). If `__str__` is not defined, Python falls back to
> `__repr__` — but not vice versa.

---

### Task 5 — Destructor (`5-rectangle.py`)

**Challenge:** Execute cleanup code when a Rectangle instance is garbage-collected —
introducing the `__del__` dunder method and the object lifecycle.

**Approach:** Define `def __del__(self):` that prints `"Bye rectangle..."`. Python calls
this method automatically when the object's reference count reaches zero and it's about
to be destroyed.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `def __del__(self):` | Destructor — called when the object is about to be garbage-collected |

> **Key takeaway:** `__del__` is not a true destructor like in C++ — it's called by the
> garbage collector, and the timing is not guaranteed. Use it for cleanup like closing
> files or releasing resources. Avoid relying on it for critical logic.

---

### Task 6 — Class Variable: Instance Counter (`6-rectangle.py`)

**Challenge:** Track how many Rectangle instances currently exist — introducing class
variables (shared across all instances) and the pattern of incrementing/decrementing them.

**Approach:** Define `number_of_instances = 0` at the class level (outside any method).
In `__init__`, increment with `Rectangle.number_of_instances += 1`. In `__del__`, decrement
with `Rectangle.number_of_instances -= 1`. Access always uses `ClassName.var`, not `self.var`.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| Class variable (defined outside methods) | A single value shared by all instances of the class |
| `ClassName.var` access | Explicitly reference a class variable — distinct from `self.var` |
| `+= 1` in `__init__`, `-= 1` in `__del__` | Track instance count across the lifecycle |

> **Key takeaway:** Class variables belong to the class, not to instances. Changing
> `ClassName.var` affects all instances. Instance variables (set via `self`) are unique
> to each object. Use `ClassName.var` for clarity when dealing with class-level data.

---

### Task 7 — Customizable Print Symbol (`7-rectangle.py`)

**Challenge:** Let users change the character used to render the rectangle — introducing
a configurable class variable that affects instance behavior.

**Approach:** Define `print_symbol = "#"` as a class variable. In `__str__`, replace the
hardcoded `"#"` with `"{}".format(self.print_symbol) * self.__width`. Users can now do
`Rectangle.print_symbol = "X"` to change the symbol for all instances.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| Class variable as configurable option | Change behavior globally by reassigning a class variable |
| `self.print_symbol` access | An instance can read a class variable through `self` (falls back to class) |
| `"{}".format(symbol) * width` | Repeat a configurable character for the rectangle's width |

> **Key takeaway:** When you access `self.var`, Python first looks for an instance attribute,
> then falls back to the class attribute. This means class variables can serve as defaults
> that instances can optionally override.

---

### Task 8 — Static Method (`8-rectangle.py`)

**Challenge:** Add a comparison method that doesn't depend on a specific instance —
introducing `@staticmethod` and its distinction from regular methods.

**Approach:** Decorate `def bigger_or_equal(rect_1, rect_2):` with `@staticmethod`. The
method takes two Rectangle arguments, validates both with `isinstance`, compares their
`area()`, and returns the larger (or `rect_1` if equal). No `self` parameter — it's called
as `Rectangle.bigger_or_equal(r1, r2)`.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `@staticmethod` | Define a method that doesn't receive `self` or `cls` — a plain function in the class namespace |
| No `self` parameter | Static methods operate on explicit arguments, not on instance data |
| `ClassName.static_method()` call | Call a static method via the class (or an instance) |

> **Key takeaway:** Static methods are utility functions that logically belong to the class
> but don't need instance or class data. They're called on the class, not on instances.

---

### Task 9 — Class Method: Factory (`9-rectangle.py`)

**Challenge:** Create an alternative constructor that returns a special kind of Rectangle
(a square) — introducing `@classmethod` and the factory pattern.

**Approach:** Decorate `def square(cls, size=0):` with `@classmethod`. The method receives
`cls` (the class itself) instead of `self`. It returns `Rectangle(size, size)` — a rectangle
with equal width and height. Called as `Rectangle.square(5)`.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `@classmethod` | Define a method that receives the class (`cls`) as its first argument |
| `cls` parameter | Reference to the class — used to create instances or access class variables |
| Factory method pattern | Alternative constructor that returns a pre-configured instance |
| `return cls(arg, arg)` | Create and return an instance from within a class method |

> **Key takeaway:** Class methods are for operations on the class itself — like alternative
> constructors. `cls` is the class (e.g., `Rectangle`), so `cls(5, 5)` creates a new instance.
> This pattern lets you provide multiple ways to create objects.

---

### Task 10 — Blog: Class and Instance Attributes

**Challenge:** Articulate the full mental model of class vs. instance attributes — including
creation, differences, `__dict__` mechanics, and Pythonic best practices — in a published
blog post with examples and a diagram.

**Approach:** Write a comprehensive post covering: class attributes (defined in the class
body, shared across all instances), instance attributes (bound to `self` in `__init__`,
unique per object), the Pythonic way using `__init__` and class-level constants, the
`__dict__` attribute as the storage mechanism, and Python's MRO-based lookup fallback
from instance to class. Include code examples and an explanatory diagram.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| Class attribute definition in class body | Shared mutable/non-mutable state across all instances |
| Instance attribute via `self.attr` in `__init__` | Per-object state, unique to each instance |
| `obj.__dict__` and `ClassName.__dict__` | Inspect the attribute storage dictionary for instances and classes |
| Python attribute lookup: instance → class → base classes | Understand the MRO-based fallback chain |

> **Key takeaway:** Class attributes are shared; instance attributes are unique. Python stores
> both in `__dict__` dictionaries and looks up attributes via instance-first MRO fallback.
> The Pythonic way: define class-level defaults/constants in the class body, instance-specific
> state in `__init__` via `self`.

---

## Technique Inventory

| Task | New technique summarized | Category |
|------|--------------------------|----------|
| 0 | Review: empty class, docstrings, `pass` | OOP Basics |
| 1 | Multiple private attributes, separate property pairs per attribute | Properties |
| 2 | `perimeter()` formula, zero-dimension edge case return 0 | Methods |
| 3 | `__str__` dunder, list building + `"".join()`, `out[:-1]` trim | Dunder Methods |
| 4 | `__repr__` dunder, `eval()`-compatible format string | Dunder Methods |
| 5 | `__del__` destructor, garbage collection lifecycle | Lifecycle |
| 6 | Class variable, `ClassName.var` access, `+=`/`-=` lifecycle tracking | Class Attributes |
| 7 | Configurable class variable, `self.var` fallback, `"{}".format()` repetition | Class Attributes |
| 8 | `@staticmethod`, no `self`/`cls`, `isinstance` parameter validation | Static Methods |
| 9 | `@classmethod`, `cls` parameter, factory method pattern | Class Methods |
| 10 | Class vs. instance attributes, `__dict__` mechanics, MRO lookup fallback | Attributes & Internals |

---

## Resources

- [9. Classes — Python Docs](https://docs.python.org/3/tutorial/classes.html)
- [Data model — `__str__`, `__repr__`, `__del__`](https://docs.python.org/3/reference/datamodel.html#basic-customization)
- [Class and Static Methods — Real Python](https://realpython.com/instance-class-and-static-methods-demystified/)
- [Python Class Attributes — Overview](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables)
- [Factory Method Pattern — Python](https://realpython.com/factory-method-python/)
- [Python `__dict__` and Attribute Lookup](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy)
- [Class and Instance Attributes — Real Python](https://realpython.com/python3-object-oriented-programming/#class-and-instance-attributes)