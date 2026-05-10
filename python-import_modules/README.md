# Python — Import & Modules

A progressive study of Python's import system, command-line arguments, module introspection, and the `if __name__ == "__main__"` pattern.

---

## Learning Objectives

| # | Concept |
|---|---------|
| 1 | How to import functions from another file |
| 2 | How to use imported functions |
| 3 | How to create a module |
| 4 | How to use the built-in function `dir()` |
| 5 | How to prevent code in your script from being executed when imported |
| 6 | How to use command-line arguments with `sys.argv` |
| 7 | How to use `*args` for variable-length function arguments |
| 8 | How to use `__import__()` for dynamic imports |
| 9 | How to use the `string` module for character constants |

---

## Task-by-Task Reference

Each task below highlights the **unique challenge** it posed and the **new technique** introduced to solve it — techniques from earlier tasks are not repeated. Use this as a quick revision guide.

---

### Task 0 — Import a Function (`0-add.py`)

**Challenge:** Use a function defined in a *different file* — introducing Python's import
system and the distinction between running vs. importing a script.

**Approach:** Use `from add_0 import add` to bring a single function into scope. Define a
`main()` wrapper function and guard its execution with `if __name__ == "__main__":` so the
code only runs when the file is executed directly, not when imported by another module.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `from module import name` | Import a specific function from another `.py` file |
| `if __name__ == "__main__":` | Guard — code only executes when run directly, not on import |
| `def main():` pattern | Convention for the entry point function |

> **Key takeaway:** `__name__` is a built-in variable. When a file is run directly, it equals
> `"__main__"`. When imported, it equals the module's name. The guard prevents imported code
> from auto-executing.

---

### Task 1 — Import Multiple Functions (`1-calculation.py`)

**Challenge:** Import several functions from a single module and call them all — introducing
comma-separated multi-import syntax.

**Approach:** Use `from calculator_1 import add, sub, mul, div` to import four functions in
one line. Call each with the same arguments and print the results with the operator symbol.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `from module import f1, f2, f3, f4` | Import multiple specific names from a module at once |

> **Key takeaway:** You can import as many names as you need from a module — just separate
> them with commas. This is cleaner than writing four separate `from … import` lines.

---

### Task 2 — Command-Line Arguments (`2-args.py`)

**Challenge:** Access and display arguments passed to the script from the command line —
introducing the `sys` module and the concept of program arguments.

**Approach:** `import sys` to access `sys.argv[1:]` (all arguments after the script name).
Define `main(*argv)` to accept variable-length arguments via `*` unpacking. Call
`main(*sys.argv[1:])` to pass arguments as positional parameters.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `import sys` | Access system-specific parameters and functions |
| `sys.argv` | List of command-line arguments (`sys.argv[0]` is the script name) |
| `*argv` in function signature | Accept a variable number of positional arguments as a tuple |
| `*sys.argv[1:]` at call site | Unpack a list into individual positional arguments |
| `len(argv)` | Count how many arguments were passed |

> **Key takeaway:** `sys.argv` is a list where index 0 is always the script filename.
> Everything from index 1 onward is actual user input. `*` unpacks lists into function arguments.

---

### Task 3 — Sum Arguments (`3-infinite_add.py`)

**Challenge:** Treat all command-line arguments as numbers and sum them — introducing
type conversion from string arguments to integers in a loop.

**Approach:** Use the same `main(*argv)` pattern from Task 2. Initialize `sum = 0`, loop
over `argv`, cast each to `int()`, and accumulate. Print the final sum.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `int(argv[i])` in a loop | Convert string arguments to integers for arithmetic |
| Accumulator pattern: `sum += value` | Build up a total across loop iterations |

> **Key takeaway:** Command-line arguments always arrive as strings. You must explicitly cast
> them to `int()` or `float()` before doing math.

---

### Task 4 — Discover Hidden Names (`4-hidden_discovery.py`)

**Challenge:** List only the *public* names defined in an imported module — filtering out
private/internal names — introducing module introspection with `dir()`.

**Approach:** `import hidden_4` then use `dir(hidden_4)` to get a list of all names in the
module's namespace. Filter by checking if the name starts with `_` (Python's convention for
private/hidden names) and print only public ones.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `dir(module)` | Introspection — list all names (functions, variables, classes) in a module |
| Name filtering: `name[0] != "_"` | Distinguish public vs. private names by Python's `_` prefix convention |

> **Key takeaway:** `dir()` is a powerful introspection tool. Names prefixed with `_` are
> conventionally "private" in Python (not truly hidden, but indicating internal use).

---

### Task 5 — Import a Variable (`5-variable_load.py`)

**Challenge:** Import and use a module-level *variable* (not a function) — showing that
imports work for data, not just code.

**Approach:** `from variable_load_5 import a` to bring the variable `a` into scope. Print
its value. The pattern is identical to importing a function — Python treats all module-level
names uniformly.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| Importing a variable (not a function) | Module-level names can be any object — strings, ints, lists, etc. |

> **Key takeaway:** When you `from module import name`, `name` can be a function, variable,
> class, or any object defined at the top level of that module. There's no syntactic difference.

---

### Task 6 — CLI Calculator (`100-my_calculator.py`)

**Challenge:** Build a command-line calculator that parses an operator symbol and dispatches
to the correct imported function — introducing argument validation, operator dispatch, and
error handling in a CLI tool.

**Approach:** Import `argv` directly from `sys`. Validate that exactly 3 arguments exist
(`<a> <operator> <b>`), printing a usage message if not. Cast `a` and `b` to `int`. Use
`if`/`elif` on the operator string to dispatch to `add`, `sub`, `mul`, or `div`. Raise
`ValueError` for unknown operators.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `from sys import argv` | Direct import of `argv` — no `sys.` prefix needed |
| CLI argument validation (`len(argv) != 3`) | Enforce correct usage before proceeding |
| Operator dispatch with `if`/`elif` | Route to the correct function based on a string |
| `raise ValueError()` | Explicitly signal an error condition to the caller |

> **Key takeaway:** Direct imports (`from X import Y`) let you use `Y` without the module
> prefix. `raise` is how you generate exceptions — it stops execution and propagates the error.

---

### Task 7 — Dynamic Import (`101-easy_print.py`)

**Challenge:** Import and use a module without a `from … import` or `import` statement —
introducing dynamic imports via the `__import__()` built-in function.

**Approach:** Call `__import__('sys').stdout.write("#pythoniscool\n")` — the `__import__()`
function returns the module object, then you chain attribute access (`.stdout`) and method
calls (`.write()`) directly on the result.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `__import__('module_name')` | Dynamic import — import a module whose name is a string (known at runtime) |
| Method chaining on import result | Access module attributes immediately without assigning to a variable |

> **Key takeaway:** `__import__()` is the function that backs the `import` statement. It's
> rarely used directly, but it enables importing modules whose names aren't known until runtime.

---

### Task 8 — Conditional Calculation (`102-magic_calculation.py`)

**Challenge:** Implement a function that imports helper functions from another module and
applies them conditionally with looping — showing how imports integrate with control flow.

**Approach:** `from magic_calculation_102 import add, sub`. Compare `a` and `b`: if `a < b`,
call `add` and then loop `range(4, 6)` to add 4 and 5 to the result. Otherwise, call `sub`
and return directly. The imports are used inside branching logic.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| Import + conditional + loop combination | Use imported functions inside `if`/`else` and `for` blocks |
| Accumulate across a `range()` loop | Repeatedly call an imported function with the running total |

> **Key takeaway:** Imports aren't just for top-level use — you can call imported functions
> anywhere: in loops, conditionals, or nested deeply in logic. They're first-class callables.

---

### Task 9 — String Module Constants (`103-fast_alphabet.py`)

**Challenge:** Print the uppercase alphabet without looping — introducing Python's `string`
module and its built-in character constants.

**Approach:** `import string` and print `string.ascii_uppercase` — a pre-defined string
constant containing `"ABCDEFGHIJKLMNOPQRSTUVWXYZ"`. No loops, no `chr()`, no ASCII math.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `import string` | Access character constants and string utilities |
| `string.ascii_uppercase` | Pre-defined uppercase alphabet constant |
| Module-level constants | Modules can expose data (strings, numbers) as well as functions |

> **Key takeaway:** The `string` module provides constants like `ascii_uppercase`,
> `ascii_lowercase`, `digits`, and `punctuation` — saving you from typing them manually.

---

## Technique Inventory

| Task | New technique summarized | Category |
|------|--------------------------|----------|
| 0 | `from X import Y`, `__name__ == "__main__"`, `main()` pattern | Modules |
| 1 | Multi-name import: `from X import f1, f2, f3` | Modules |
| 2 | `import sys`, `sys.argv`, `*argv` unpacking, `len()` | CLI & Scripting |
| 3 | `int()` casting in loop, accumulator `+=` pattern | CLI & Scripting |
| 4 | `dir()` introspection, name filtering by `_` prefix | Modules |
| 5 | Importing module-level variables (not just functions) | Modules |
| 6 | `from sys import argv`, operator dispatch, `raise ValueError()` | CLI & Scripting |
| 7 | `__import__()` dynamic import, method chaining | Modules |
| 8 | Imports inside conditionals and loops | Modules |
| 9 | `string` module, `string.ascii_uppercase` constant | Modules |

---

## Resources

- [6. Modules — Python Docs](https://docs.python.org/3/tutorial/modules.html)
- [The `sys` module — `sys.argv`](https://docs.python.org/3/library/sys.html)
- [Built-in Functions — `dir()`, `__import__()`](https://docs.python.org/3/library/functions.html)
- [The `string` module](https://docs.python.org/3/library/string.html)
- [`__main__` — Top-level code environment](https://docs.python.org/3/library/__main__.html)