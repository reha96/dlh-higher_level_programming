# DLH — Higher-Level Programming

A structured curriculum in Python programming — from printing strings to object-oriented design, data structures, exception handling, file I/O, and serialization.

---

## Directory Structure

```
dlh-higher_level_programming/
├── python-hello_world/                  # Printing, strings, formatting
│   ├── 2-print.py through 9-easter_egg.py
│   └── README.md
├── python-if_else_loops_functions/      # Control flow, loops, functions, ASCII
│   ├── 0-positive_or_negative.py through 12-fizzbuzz.py
│   ├── 100-print_tebahpla.py, 101-remove_char_at.py
│   └── README.md
├── python-import_modules/               # Import system, sys.argv, module introspection
│   ├── 0-add.py through 5-variable_load.py
│   ├── 100-my_calculator.py through 103-fast_alphabet.py
│   └── README.md
├── python-data_structures/              # Lists, tuples, sequence operations
│   ├── 0-print_list_integer.py through 12-switch.py
│   └── README.md
├── python-more_data_structures/         # Sets, dictionaries, lambda, map, filter
│   ├── 0-square_matrix_simple.py through 12-roman_to_int.py
│   ├── 100-weight_average.py through 102-complex_delete.py
│   └── README.md
├── python-exceptions/                   # try/except/finally, raise, stderr
│   ├── 0-safe_print_list.py through 6-raise_exception_msg.py
│   ├── 100-safe_print_integer_err.py through 102-magic_calculation.py
│   └── README.md
├── python-classes/                      # OOP: classes, objects, properties, validation
│   ├── 0-square.py through 6-square.py
│   ├── 100-singly_linked_list.py through 102-square.py
│   └── README.md
├── python-more_classes/                 # Dunder methods, class/static methods, lifecycle
│   ├── 0-rectangle.py through 9-rectangle.py
│   └── README.md
├── python-input_output/                 # File I/O, JSON, context managers
│   ├── 0-read_file.py through 12-pascal_triangle.py
│   └── README.md
├── python-serialization/                # Pickle, CSV, JSON, XML marshaling
│   ├── task_00_basic_serialization.py through task_03_xml.py
│   └── README.md
└── README.md
```

---

## Quick Reference

| # | Module | Topics | Tasks |
|---|--------|--------|-------|
| 1 | [Hello World](python-hello_world/) | `print()`, f-strings, format specifiers, string slicing, `import` | 8 |
| 2 | [If/Else, Loops, Functions](python-if_else_loops_functions/) | `if`/`elif`/`else`, `for`/`while`, `range()`, `ord()`/`chr()`, `def`, operators | 15 |
| 3 | [Import & Modules](python-import_modules/) | `from X import Y`, `sys.argv`, `*args`, `__name__`, `dir()`, `__import__()` | 10 |
| 4 | [Data Structures: Lists, Tuples](python-data_structures/) | List iteration, indexing, mutation, tuples, matrix traversal, `del` | 13 |
| 5 | [More Data Structures](python-more_data_structures/) | Sets, dictionaries, `map()`/`lambda`/`filter`, sorting with `key`, Roman numerals | 16 |
| 6 | [Exceptions](python-exceptions/) | `try`/`except`/`finally`, `raise`, `stderr`, safe functions, exception chaining | 10 |
| 7 | [Classes & Objects](python-classes/) | `class`, `__init__`, `self`, `@property`, encapsulation, linked lists, comparison dunders | 10 |
| 8 | [More Classes](python-more_classes/) | `__str__`/`__repr__`/`__del__`, class/static methods, `@classmethod`, `__dict__` | 11 |
| 9 | [Input/Output](python-input_output/) | `with open()`, `read()`/`write()`/`append`, `json.dumps()`/`json.loads()`, Pascal's triangle | 13 |
| 10 | [Serialization](python-serialization/) | `json.dump()`/`json.load()`, `pickle`, `csv.DictReader`, `xml.etree.ElementTree` | 4 |

---

## Learning Progression

```
Hello World ──→ If/Else/Loops ──→ Import/Modules ──→ Data Structures (Lists/Tuples)
                                                          │
                                                          ▼
                                              More Data Structures (Sets/Dicts)
                                                          │
                                                          ▼
                                                  Exceptions (try/except)
                                                          │
                                                          ▼
                                              Classes & Objects (OOP Basics)
                                                          │
                                                          ▼
                                              More Classes (Dunder, Static, Class Methods)
                                                          │
                                                          ▼
                                              Input/Output (Files + JSON)
                                                          │
                                                          ▼
                                              Serialization (Pickle, CSV, XML)
```

### Track Summary

1. **Foundations** (Hello World → Import/Modules): Basic syntax, control flow, functions, the import system
2. **Data Manipulation** (Data Structures → More Data Structures): Lists, tuples, sets, dictionaries, functional programming
3. **Robustness** (Exceptions): Error handling, safe functions, stderr
4. **OOP** (Classes → More Classes): Encapsulation, properties, dunder methods, class hierarchies
5. **Persistence** (I/O → Serialization): Files, JSON, Pickle, CSV, XML — data in and out of Python

---

## Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Python Tutorial — Classes](https://docs.python.org/3/tutorial/classes.html)
- [Python Tutorial — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Python Tutorial — Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)
- [Python Data Model — Dunder Methods](https://docs.python.org/3/reference/datamodel.html)
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [Pickle — Python object serialization](https://docs.python.org/3/library/pickle.html)
