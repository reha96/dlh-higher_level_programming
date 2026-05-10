# Python — If/Else, Loops, Functions

A progressive study of control flow, iteration, the ASCII character set, and function definitions in Python.

---

## Learning Objectives

| # | Concept |
|---|---------|
| 1 | Why indentation matters in Python |
| 2 | How to use `if`, `elif`, and `else` statements |
| 3 | How to use the `random` module to generate random numbers |
| 4 | How to use `for` loops with `range()` |
| 5 | How to use `while` loops |
| 6 | How to use `break` and `continue` |
| 7 | How to use `else` clauses on loops |
| 8 | How to work with ASCII codes via `ord()` and `chr()` |
| 9 | How to define and call a function |
| 10 | What a function returns (and functions that don't return) |
| 11 | How to use mathematical operators: `+`, `-`, `*`, `/`, `//`, `%`, `**` |
| 12 | How to use the modulo operator `%` for divisibility checks |

---

## Task-by-Task Reference

Each task below highlights the **unique challenge** it posed and the **new technique** introduced to solve it — techniques from earlier tasks are not repeated. Use this as a quick revision guide.

---

### Task 0 — Positive or Negative (`0-positive_or_negative.py`)

**Challenge:** Classify a randomly generated integer as positive, zero, or negative —
introducing the concept of branching logic and non-deterministic input.

**Approach:** Use `import random` and `random.randint(-10, 10)` to generate a random number.
Then apply a three-way `if`/`elif`/`else` block to test `> 0`, `== 0`, and the catch-all
`else` for negative.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `import random` | Import the random module for non-deterministic values |
| `random.randint(lo, hi)` | Generate a random integer between `lo` and `hi` (inclusive) |
| `if` / `elif` / `else` | Multi-branch conditional — exactly one branch executes |

> **Key takeaway:** Python uses indentation (not braces) to define code blocks.
> `elif` is Python's equivalent of "else if" in other languages.

---

### Task 1 — Last Digit (`1-last_digit.py`)

**Challenge:** Extract the last digit of an integer — including negative numbers — and
compare it against thresholds, requiring correct handling of the sign.

**Approach:** Convert the number to a string with `str()`, slice `[-1]` to get the last
character, then cast back to `int()`. For negative numbers, negate the digit with
`digit = 0 - digit`. Use `type()` to confirm the input is an integer before processing.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `str(number)[-1]` | Convert to string, then slice the last character |
| `int(string)` | Cast a string digit back to an integer |
| Negative digit correction | Manually negate for negative numbers: `0 - digit` |
| `type(obj) is int` | Type-checking before operating on a value |

> **Key takeaway:** Python's `str()[-1]` works for both positive and negative numbers, but
> the sign must be handled separately — the last character of `-98` is `"8"`, not `"-8"`.

---

### Task 2 — Print Alphabet (`2-print_alphabet.py`)

**Challenge:** Print the entire lowercase alphabet on one line without hardcoding 26
characters — introducing iteration and ASCII code manipulation.

**Approach:** Use `for i in range(97, 123)` to iterate over ASCII codes a–z, convert each
code to a character with `chr(i)`, and output with `end=""` to keep everything on one line.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `for i in range(start, end)` | Loop over a numeric sequence from `start` to `end - 1` |
| `chr(ascii_code)` | Convert an ASCII/Unicode code point to its character |
| `"{}".format(value)` | Older string formatting method (pre-f-string) |

> **Key takeaway:** Loops avoid repetition. Instead of typing 26 letters, you generate them
> from their ASCII codes: `a` = 97, `z` = 122.

---

### Task 3 — Print Alphabet Except q and e (`3-print_alphabt.py`)

**Challenge:** Print the alphabet with specific letters excluded — introducing conditional
skipping inside a loop without breaking out of it.

**Approach:** Inside the `for` loop, check if `chr(i)` equals `"q"` or `"e"`. If so,
execute `pass` (do nothing); otherwise, print the character. The loop continues regardless.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `pass` statement | A no-op placeholder — syntactically required when a block must exist but do nothing |
| Conditional skip with `if`/`else` | Filter items within a loop without `break` or `continue` |

> **Key takeaway:** `pass` is Python's way of saying "do nothing here." It's different from
> `continue` — `pass` doesn't skip the rest of the loop body, it just fills an empty block.

---

### Task 4 — Decimal and Hexadecimal (`4-print_hexa.py`)

**Challenge:** Display numbers 0–98 in both decimal and hexadecimal format side by side —
introducing base conversion and string concatenation in output.

**Approach:** Loop `range(99)`, then print each number with `hex(i)` which returns the
hexadecimal representation as a string like `"0x63"`. Concatenate with `+` for the output.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `hex(n)` | Convert an integer to its hexadecimal string representation (prefixed `0x`) |
| `range(99)` (single arg) | Shorthand for `range(0, 99)` — start defaults to 0 |

> **Key takeaway:** `hex()` returns a string like `"0x63"` for 99. Related: `bin()` for
> binary and `oct()` for octal. All three produce prefixed strings, not bare digits.

---

### Task 5 — Two-Digit Combinations (`5-print_comb2.py`)

**Challenge:** Print numbers 00–99 with proper zero-padding, comma-separated, ending
without a trailing comma — introducing formatted number output.

**Approach:** Loop `range(100)`. Use `"{:02d}".format(i)` to zero-pad single-digit numbers.
Check `i < 99` to append `", "` for all but the last item, which is printed plain.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `"{:02d}".format(n)` | Zero-pad integers to 2 digits (`:02d` = width 2, pad with zeros) |
| Conditional separator logic | Append comma only when not the last iteration |

> **Key takeaway:** The format spec `:02d` means: `0` = pad with zeros, `2` = minimum width,
> `d` = decimal integer. Use `{:03d}` for 3-digit padding, etc.

---

### Task 6 — Unique Digit Combinations (`6-print_comb3.py`)

**Challenge:** Generate all unique two-digit combinations (01, 02, … 89) where digits
don't repeat and order matters — introducing nested loops and the `continue` statement.

**Approach:** Use nested `for` loops: outer `i` from 0–9, inner `j` from 1–9. Skip when
`i == j` with `continue`. Only print when `i < j` (ensuring each pair appears once).
Handle the last combination (`i == 8`) without trailing comma.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| Nested `for` loops | Iterate over all pairs `(i, j)` — outer × inner |
| `continue` | Skip the rest of the current iteration and jump to the next |
| Combination logic (`i < j`) | Constrain output to unique ordered pairs without repeats |

> **Key takeaway:** `continue` jumps to the next iteration of the innermost loop.
> Use it to skip unwanted cases without nesting deeply inside `if` blocks.

---

### Task 7 — Is Lowercase (`7-islower.py`)

**Challenge:** Write your own function that determines if a character is lowercase — without
using the built-in `.islower()` method — introducing function definitions and `ord()`.

**Approach:** Define `def islower(c):` that takes a single character. Use `ord(c)` to get
its ASCII code and check if it falls in the lowercase range 97–122. Return `True` or `False`.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `def function_name(param):` | Define a named, reusable function |
| `ord(char)` | Get the ASCII/Unicode code point of a character (inverse of `chr()`) |
| `return True` / `return False` | Return a boolean result from a function |

> **Key takeaway:** Every character has a numeric code. `ord('a')` → 97, `ord('z')` → 122.
> Comparing against these ranges is how you implement character classification from scratch.

---

### Task 8 — Uppercase Converter (`8-uppercase.py`)

**Challenge:** Convert an entire string to uppercase character-by-character using ASCII
arithmetic — introducing in-place character transformation and index-based iteration.

**Approach:** Define `def uppercase(str):` that loops with `range(len(str))` to get each
index. For each character, get its `ord()`, check if lowercase (97–122), and subtract 32
to shift to uppercase. Use `chr()` to convert back and print character by character.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `range(len(string))` | Iterate by index over a string's characters |
| ASCII case shift: `ord(c) - 32` | Convert lowercase to uppercase by subtracting 32 from the code point |
| Character-by-character output | Build output one character at a time inside a loop |

> **Key takeaway:** The ASCII distance between lowercase and uppercase is exactly 32.
> `ord('a')` = 97, `ord('A')` = 65, and 97 − 65 = 32. This holds for all letters.

---

### Task 9 — Print Last Digit (`9-print_last_digit.py`)

**Challenge:** Write a function that both prints the last digit AND returns it — introducing
functions with side effects plus a return value.

**Approach:** Define `def print_last_digit(number):`. Convert to string, slice `[-1]`,
cast to `int`, print it with `end=""`, then `return digit`. The caller gets both the
printed output and the usable value.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| Function with side effect + return | A function that does something observable (prints) AND returns a value |

> **Key takeaway:** Functions can both produce output and return data — they're not mutually
> exclusive. The caller can use the returned value in further computation.

---

### Task 10 — Add Two Integers (`10-add.py`)

**Challenge:** Write the simplest possible reusable function — two inputs, one output —
introducing the clean function signature pattern.

**Approach:** Define `def add(a, b):` that computes `a + b`, stores it in a variable, and
returns it. This is a "pure" function: no side effects, deterministic output for given inputs.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| Multi-parameter function signature | Accept two (or more) named parameters |
| Pure function pattern | Compute result from inputs only, return it, no side effects |

> **Key takeaway:** A function that only depends on its parameters and always returns the same
> output for the same input is called "pure" — it's easier to test and reason about.

---

### Task 11 — Power Function (`11-pow.py`)

**Challenge:** Compute `a` raised to the power `b` without calling `math.pow()` or any
built-in power function besides the language operator.

**Approach:** Use Python's `**` exponentiation operator: `a ** b`. Store the result and
return it from a pure function.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `**` exponentiation operator | Raise a number to a power: `a ** b` = aᵇ |

> **Key takeaway:** Python has `**` for exponentiation (unlike `^` in some languages, which
> is bitwise XOR in Python). For square roots, use `x ** 0.5`.

---

### Task 12 — FizzBuzz (`12-fizzbuzz.py`)

**Challenge:** Implement the classic FizzBuzz algorithm — print numbers 1–100, replacing
multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both with
"FizzBuzz" — introducing the modulo operator and multi-condition ordering.

**Approach:** Loop `range(1, 101)`. Check `i % 3 == 0 and i % 5 == 0` FIRST (both), then
`i % 3 == 0` for Fizz, then `i % 5 == 0` for Buzz, else print the number. Order matters:
the most specific condition must come before the less specific ones.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `%` modulo operator | Returns remainder of division — `x % n == 0` means x is divisible by n |
| `and` logical operator | Combine multiple boolean conditions — both must be True |
| Condition ordering (most specific first) | Place the combined check before individual checks |

> **Key takeaway:** `%` is the key to divisibility checks. In FizzBuzz, checking `% 3 and % 5`
> before checking `% 3` alone is critical — otherwise "FizzBuzz" is never reached.

---

### Task 13 — Alternating Reverse Alphabet (`100-print_tebahpla.py`)

**Challenge:** Print a reversed alphabet where characters alternate between uppercase and
lowercase based on position parity — combining ASCII math with parity checks.

**Approach:** Loop `range(26)` for 26 letters. Use `i % 2 == 0` to check parity. For even
indices, print `chr(122 - i)` (lowercase z backwards); for odd indices, print
`chr(90 - i)` (uppercase Z backwards). The alternating pattern emerges from the parity test.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| Parity-based alternating logic (`i % 2`) | Switch behavior based on even/odd position |
| Decrementing ASCII: `chr(122 - i)` | Iterate backwards through the alphabet by subtracting from z/Z |

> **Key takeaway:** `i % 2` is the universal toggle — 0 for even, 1 for odd. Combine it
> with ASCII arithmetic to produce alternating patterns without a separate flag variable.

---

### Task 14 — Remove Character at Index (`101-remove_char_at.py`)

**Challenge:** Return a copy of a string with the character at position `n` removed —
without using slicing to skip, introducing iterative string building.

**Approach:** Define `def remove_char_at(str, n):`. Initialize an empty `output` string.
Loop with `range(len(str))` and append `str[i]` to `output` only when `i != n`. Return
the accumulated result.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| Iterative string building | Accumulate characters one-by-one into a result string |
| Conditional append (`if i != n`) | Selectively include characters by skipping a specific index |

> **Key takeaway:** Strings are immutable, so "removing" a character means building a new
> string that omits it. This pattern — iterate, check, accumulate — is a fundamental
> string transformation technique.

---

## Technique Inventory

| Task | New technique summarized | Category |
|------|--------------------------|----------|
| 0 | `import random`, `random.randint()`, `if`/`elif`/`else` | Control Flow |
| 1 | `str()`/`int()` casting, `type()` check, negative digit handling | Type Conversion |
| 2 | `for` loop, `range()`, `chr()`, `.format()` | Loops & ASCII |
| 3 | `pass` statement, conditional skip inside loop | Control Flow |
| 4 | `hex()` base conversion, single-arg `range()` | Built-ins |
| 5 | `{:02d}` zero-padded formatting, conditional separator | String Formatting |
| 6 | Nested `for` loops, `continue`, combination generation | Loops |
| 7 | `def` function, `ord()`, boolean return | Functions |
| 8 | `range(len())`, ASCII case shift (`ord - 32`), char-by-char output | ASCII |
| 9 | Function with side effect + return value | Functions |
| 10 | Multi-parameter pure function | Functions |
| 11 | `**` exponentiation operator | Operators |
| 12 | `%` modulo, `and` operator, condition ordering (FizzBuzz) | Operators & Logic |
| 13 | Parity toggle (`i % 2`), decrementing `chr()` pattern | ASCII & Patterns |
| 14 | Iterative string building, conditional character append | String Operations |

---

## Resources

- [4. More Control Flow Tools — Python Docs](https://docs.python.org/3/tutorial/controlflow.html)
- [Built-in Functions — `ord()`, `chr()`, `hex()`](https://docs.python.org/3/library/functions.html)
- [String Formatting — `str.format()`](https://docs.python.org/3/library/string.html#format-string-syntax)
- [The `random` module](https://docs.python.org/3/library/random.html)
- [Operators — Python Docs](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations)