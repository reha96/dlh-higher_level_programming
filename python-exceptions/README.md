# Python — Exceptions

A progressive study of error handling in Python: `try`/`except`/`finally`, raising exceptions, writing to stderr, and building resilient functions.

---

## Learning Objectives

| # | Concept |
|---|---------|
| 1 | Why Python programming is awesome |
| 2 | What's the difference between errors and exceptions |
| 3 | What are exceptions and how to use them |
| 4 | When do we need to use exceptions |
| 5 | How to correctly handle an exception |
| 6 | What's the purpose of catching exceptions |
| 7 | How to raise a built-in exception |
| 8 | When do we need to implement a clean-up action after an exception |
| 9 | How to write to standard error (`stderr`) |

---

## Task-by-Task Reference

Each task below highlights the **unique challenge** it posed and the **new technique** introduced to solve it — techniques from earlier tasks are not repeated. Use this as a quick revision guide.

---

### Task 0 — Safe Print List (`0-safe_print_list.py`)

**Challenge:** Print elements from a list up to a requested count, even if the list is
shorter than requested — introducing Python's exception handling mechanism.

**Approach:** Wrap the printing loop in `try:`. Catch `IndexError` (raised when accessing
beyond the list bounds) with `except (IndexError):` and simply `pass`. Use `finally:` to
always print a newline and return the count of successfully printed elements.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `try:` / `except (IndexError):` | Catch a specific exception — IndexError when index is out of range |
| `finally:` block | Code that always runs, whether an exception occurred or not |
| `return` inside `finally` | Return a value after cleanup — `finally` runs even if there's a `return` elsewhere |

> **Key takeaway:** `try`/`except` lets you handle errors gracefully instead of crashing.
> `finally` is for cleanup that must happen no matter what (closing files, returning results).

---

### Task 1 — Safe Print Integer (`1-safe_print_integer.py`)

**Challenge:** Attempt to format and print a value as an integer — catching ANY exception
if the value isn't compatible — introducing broad exception handling and boolean success/failure returns.

**Approach:** Use `try:` with `"{:d}".format(value)` (which only works for integers).
Catch all exceptions with a bare `except:` and return `False`. On success, return `True`.
The function never crashes — it always returns a boolean indicating success.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| Bare `except:` (no exception type) | Catch absolutely any exception — broadest possible handler |
| `"{:d}".format(value)` | Format spec `:d` — only accepts integers, raises TypeError/ValueError otherwise |
| Boolean success/failure return | Pattern: return `True` on success, `False` on any error |

> **Key takeaway:** A bare `except:` catches everything including `KeyboardInterrupt` and
> `SystemExit` — use it sparingly. Prefer specific exception types when possible.

---

### Task 2 — Safe Print Only Integers (`2-safe_print_list_integers.py`)

**Challenge:** Print only the integer elements from a list, skipping non-integers and
handling out-of-bounds access — introducing type-checking inside exception handlers and
catching multiple exception types.

**Approach:** Loop up to `x`, and inside `try:`, use `type(my_list[i]) is int` to check
the type. If it matches, print it. Catch both `TypeError` (wrong type) and `IndexError`
(out of range) with a tuple `except (TypeError, IndexError):` and `pass`.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `except (TypeError, IndexError):` | Catch multiple exception types in a single `except` clause |
| `type(value) is int` inside `try` | Type-check elements before operating on them |

> **Key takeaway:** You can catch multiple exception types by grouping them in a tuple.
> The first matching type triggers the handler. Each exception is independent.

---

### Task 3 — Safe Division (`3-safe_print_division.py`)

**Challenge:** Safely divide two numbers, handling division-by-zero, and always print the
result — introducing specific exception catching and fallback values.

**Approach:** Try `a / b` inside `try:`. Catch `ZeroDivisionError` and set the result to
`None`. In `finally:`, always print the result and return it — ensuring the function never
fails silently.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `except ZeroDivisionError:` | Catch division by zero specifically |
| `None` as fallback value | Use `None` to signal "no valid result" when an error occurs |

> **Key takeaway:** Division by zero raises `ZeroDivisionError`, not a general exception.
> Catching it specifically lets you distinguish it from other errors and provide a meaningful fallback.

---

### Task 4 — List Division (`4-list_division.py`)

**Challenge:** Divide corresponding elements of two lists element-by-element, handling
three different error cases (wrong type, division by zero, out of range) with different
error messages — introducing nested exception handling and `continue` inside `except`.

**Approach:** Use a nested `try`/`except` structure. The outer `try`/`finally` ensures the
result list is always returned. The inner `try` attempts the division, and three separate
`except` blocks handle `TypeError`, `ZeroDivisionError`, and `IndexError` — each appending
`0` to the result, printing a specific message, and using `continue` to move to the next iteration.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| Nested `try`/`except` (inner + outer) | Handle errors at different scopes — inner for per-iteration, outer for overall |
| Multiple `except` blocks (one per error type) | Handle each exception type differently with distinct messages |
| `continue` inside `except` | Skip to next iteration after handling an error |
| `finally` returning a built-up list | Guarantee the accumulated result is returned regardless of errors |

> **Key takeaway:** Nested `try`/`except` gives you fine-grained control — the inner handler
> deals with per-element errors while the outer `finally` ensures the function always returns.

---

### Task 5 — Raise an Exception (`5-raise_exception.py`)

**Challenge:** Explicitly trigger an exception — introducing the `raise` statement and
showing that exceptions are objects you can create and throw.

**Approach:** Define `def raise_exception():` that contains a single statement:
`raise TypeError`. No `try`/`except` — the function's sole purpose is to raise an exception.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `raise ExceptionType` | Explicitly raise (throw) an exception |

> **Key takeaway:** `raise` is how you generate exceptions. It interrupts normal flow and
> propagates up the call stack until caught or the program exits. `raise TypeError` is
> equivalent to `raise TypeError()`.

---

### Task 6 — Raise with a Message (`6-raise_exception_msg.py`)

**Challenge:** Raise an exception that carries a custom error message — introducing
exception constructors with arguments.

**Approach:** Define `def raise_exception_msg(message=""):` that calls
`raise NameError(message)`. The string argument becomes the exception's human-readable
message, visible when the traceback is printed.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `raise ExceptionType("message")` | Raise an exception with a descriptive message |
| `NameError` (a new exception type) | Raised when a local or global name is not found |

> **Key takeaway:** Most built-in exceptions accept a message string as their first argument.
> This message appears in tracebacks and helps with debugging. `NameError` is distinct from
> `TypeError` — it's about undefined names, not wrong types.

---

### Task 7 — Print Errors to stderr (`100-safe_print_integer_err.py`)

**Challenge:** When an error occurs, print the error message to standard error (stderr)
instead of standard output (stdout) — introducing the distinction between output streams.

**Approach:** Similar to Task 1, but catch `(TypeError, ValueError)` specifically with
`as err` to capture the exception object. Use `print(…, file=sys.stderr)` to direct the
error message to stderr instead of the default stdout.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `except (TypeError, ValueError) as err:` | Capture the exception object in variable `err` |
| `print(…, file=sys.stderr)` | Write output to standard error stream instead of standard output |
| `sys.stderr` | Standard error file object — separate from `sys.stdout` |

> **Key takeaway:** stderr is the correct destination for error messages and diagnostics.
> It keeps errors separate from normal program output, which matters for piping and
> redirection (`2>` in shells).

---

### Task 8 — Safe Function Executor (`101-safe_function.py`)

**Challenge:** Write a wrapper that can safely call ANY function with ANY arguments —
catching multiple exception types and returning `None` on failure — introducing higher-order
functions and generic error handling.

**Approach:** Define `def safe_function(fct, *args):`. Inside `try:`, call `fct(*args)` and
return its result. Catch `(IndexError, ZeroDivisionError, TypeError, ValueError) as err`,
print the error to stderr, and return `None`.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| Function as parameter (`fct`) | Pass a callable as an argument — higher-order function pattern |
| `*args` in signature + `fct(*args)` call | Forward variable arguments to another function |
| `return None` on error | Sentinel return value indicating failure |

> **Key takeaway:** Passing functions as arguments enables generic wrappers, decorators, and
> callbacks. `*args` lets you relay any number of arguments without knowing them in advance.

---

### Task 9 — Magic Calculation with Recovery (`102-magic_calculation.py`)

**Challenge:** Implement a calculation where an exception is raised mid-loop and triggers
an alternate computation path — introducing `raise` inside `try` and exception-based
control flow.

**Approach:** Loop `range(1, 4)`. Inside `try:`, check `if i > a:` and `raise Exception("Too far")`
if so. Otherwise, accumulate `(a ** b) / i`. If the `Exception` fires, the `except Exception:`
block sets `result = a + b` instead, effectively providing a fallback computation.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `raise` inside `try` | Conditionally trigger an exception from within a try block |
| `except` as fallback computation | Use exception handling to switch to an alternate algorithm |
| `raise Exception("message")` | Raise a generic Exception with a custom message |

> **Key takeaway:** Exceptions can be used for control flow (not just error handling). Raising
> inside `try` and catching in `except` lets you implement "try this, else fall back to that"
> patterns elegantly.

---

## Technique Inventory

| Task | New technique summarized | Category |
|------|--------------------------|----------|
| 0 | `try`/`except IndexError`/`finally`, `return` in `finally` | Exception Handling |
| 1 | Bare `except:`, `{:d}` format, boolean success/failure pattern | Exception Handling |
| 2 | `except (TypeError, IndexError)`, `type() is int` in try | Exception Handling |
| 3 | `except ZeroDivisionError`, `None` as fallback | Exception Handling |
| 4 | Nested `try`/`except`, multiple `except` blocks, `continue` in except | Exception Handling |
| 5 | `raise TypeError` | Raising Exceptions |
| 6 | `raise NameError("message")`, exception with custom message | Raising Exceptions |
| 7 | `except as err`, `file=sys.stderr`, stderr output | stderr |
| 8 | Function as parameter, `*args` forwarding, `return None` sentinel | Higher-Order Functions |
| 9 | `raise` inside `try`, except as fallback path, `raise Exception("msg")` | Raising Exceptions |

---

## Resources

- [8. Errors and Exceptions — Python Docs](https://docs.python.org/3/tutorial/errors.html)
- [Built-in Exceptions — Python Docs](https://docs.python.org/3/library/exceptions.html)
- [The `sys` module — `sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr)
- [Handling Exceptions — Python Tutorial](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)
- [Raising Exceptions — Python Tutorial](https://docs.python.org/3/tutorial/errors.html#raising-exceptions)