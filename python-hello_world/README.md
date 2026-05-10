# Python — Hello, World

A progressive introduction to printing, string manipulation, formatting, and module imports in Python.

---

## Learning Objectives

| # | Concept |
|---|---------|
| 1 | How to use the `print()` function |
| 2 | How to suppress Python's automatic newline with `end=""` |
| 3 | How to format strings with f-strings |
| 4 | How to format floats to a specific precision |
| 5 | How to repeat and slice strings |
| 6 | How to concatenate strings with `+` |
| 7 | How to extract substrings with positive and negative indices |
| 8 | How to import and use a built-in Python module |

---

## Task-by-Task Reference

Each task below highlights the **unique challenge** it posed and the **new technique** introduced to solve it — techniques from earlier tasks are not repeated. Use this as a quick revision guide.

---

### Task 0 — Print a String (`2-print.py`)

**Challenge:** Print a string containing double-quote characters and a newline — without
adding an extra trailing newline beyond what the content specifies.

**Approach:** Call `print()` with the literal string including an embedded `\n` escape
sequence. Pass `end=''` to suppress `print`'s automatic trailing newline, so the output
ends exactly where the embedded newline places it.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `print()` | Built-in function that writes text to stdout |
| `\n` escape sequence | Embeds a newline character inside a string literal |
| `print(…, end='')` | Suppresses the automatic newline `print` normally appends |

> **Key takeaway:** `print()` adds a newline by default unless you override it with `end=""`.
> Use `\n` to insert explicit line breaks within a string.

---

### Task 1 — Print an Integer (`3-print_number.py`)

**Challenge:** Embed a variable's integer value directly inside a human-readable sentence
without manual string concatenation or type casting.

**Approach:** Use an **f-string** — prefix the string with `f`, then wrap the variable
`number` in curly braces `{number}`. Python evaluates the expression inline and produces
a single formatted string.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `f"{variable} text"` | f-string — interpolates variables directly into a string literal |

> **Key takeaway:** f-strings (Python 3.6+) are the cleanest way to embed variables in
> strings. Anything inside `{}` is evaluated as a Python expression.

---

### Task 2 — Print a Float (`4-print_float.py`)

**Challenge:** Display a floating-point number rounded to exactly 2 decimal places —
controlling precision in the output without modifying the underlying variable.

**Approach:** Use an f-string with a **format specifier**: `{number:.2f}`. The `.2f`
tells Python to format the float with 2 digits after the decimal point.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `f"{var:.2f}"` | Format specifier — `.2f` rounds a float to 2 decimal places |

> **Key takeaway:** Format specifiers like `:.2f` give you fine-grained control over how
> numbers appear in output. `f` stands for fixed-point notation.

---

### Task 3 — Repeat and Slice a String (`5-print_string.py`)

**Challenge:** Print a string three times in a row, then print only its first 9 characters
on the next line — all from a single variable assignment.

**Approach:** Use string **repetition** (`str * 3`, expressed via f-string as `{str}{str}{str}`)
and string **slicing** (`str[:9]`) to extract the first 9 characters.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `str[:9]` | Slice notation — extract characters from index 0 up to (but not including) 9 |
| String repetition via f-string | Duplicate a string multiple times inline |

> **Key takeaway:** Python strings support slicing with `[start:stop]` syntax. Omitted start
> defaults to 0; omitted stop defaults to the string's length.

---

### Task 4 — Concatenate Strings (`6-concat.py`)

**Challenge:** Build a sentence by joining three separate string pieces, with spaces
between the words.

**Approach:** Use the `+` operator to concatenate strings. Insert a literal space `" "`
between variables to separate words: `str1 + " " + str2`.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| String concatenation with `+` | Join two or more strings into a single string |

> **Key takeaway:** The `+` operator on strings performs concatenation (not numeric addition).
> You must manually include spaces — Python does not insert them automatically.

---

### Task 5 — Extract Substrings (`7-edges.py`)

**Challenge:** Extract three different slices from a single string: the first 3 characters,
the last 2 characters, and everything except the first and last character.

**Approach:** Use three slice variants: `word[:3]` (first 3), `word[-2:]` (last 2 using
negative indexing from the end), and `word[1:-1]` (middle, omitting the extremes).

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `str[-2:]` | Negative indexing — `-1` is the last character, `-2` is second-to-last |
| `str[1:-1]` | Combined positive/negative bounds — start at index 1, stop before last |

> **Key takeaway:** Negative indices count backward from the end of the string. `str[-1]`
> is always the last character regardless of string length.

---

### Task 6 — Advanced Slicing & Reassembly (`8-concat_edges.py`)

**Challenge:** Reconstruct a brand-new sentence by extracting three non-contiguous slices
from a long string and concatenating them in a different order.

**Approach:** Chain three slice operations — `str[39:66]`, `str[106:112]`, `str[:6]` —
and combine them with `+`. The result reorders the original text into a completely new phrase.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| Multi-range slicing + concatenation | Compose a new string from non-adjacent parts of an original |
| Chained `str[a:b] + str[c:d] + str[e:f]` | Combine multiple slices in any order to form new content |

> **Key takeaway:** Slicing is non-destructive — the original string is never modified.
> You can extract, reorder, and reassemble slices to build entirely new strings.

---

### Task 7 — Import a Module (`9-easter_egg.py`)

**Challenge:** Display "The Zen of Python" poem without writing it yourself — leverage
Python's built-in module that contains it.

**Approach:** Use `import this` — Python's famous Easter egg. The `this` module prints the
Zen of Python automatically upon import, with no additional code needed.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `import module_name` | Import a built-in Python module to access its functionality |

> **Key takeaway:** Python ships with many built-in modules (`this`, `math`, `sys`, etc.).
> `import` gives you access to their contents without installing anything.

---

## Technique Inventory

| Task | New technique summarized | Category |
|------|--------------------------|----------|
| 0 | `print()`, `\n` escape, `end=""` | Basic I/O |
| 1 | f-string `f"{var} text"` | String Formatting |
| 2 | Format specifier `:.2f` for float precision | String Formatting |
| 3 | String slicing `str[:9]`, repetition in f-strings | String Operations |
| 4 | String concatenation with `+` | String Operations |
| 5 | Negative indexing `str[-2:]`, `str[1:-1]` | String Operations |
| 6 | Multi-range slicing & reassembly | String Operations |
| 7 | `import` statement for built-in modules | Modules |

---

## Resources

- [7. Input and Output — Python Docs](https://docs.python.org/3/tutorial/inputoutput.html)
- [f-strings — Python 3 Formatted String Literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
- [Format Specification Mini-Language](https://docs.python.org/3/library/string.html#formatspec)
- [Common String Operations — Python Docs](https://docs.python.org/3/library/string.html)
- [The `this` module — Python Easter Egg](https://docs.python.org/3/library/this.html)