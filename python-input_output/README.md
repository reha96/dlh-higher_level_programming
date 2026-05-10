# Python — Input/Output

A progressive study of file I/O, JSON serialization/deserialization, and object introspection in Python.

---

## Learning Objectives

| # | Concept |
|---|---------|
| 1 | Why Python programming is awesome |
| 2 | How to open a file |
| 3 | How to write text in a file |
| 4 | How to read the full content of a file |
| 5 | How to read a file line by line |
| 6 | How to move the cursor in a file |
| 7 | How to make sure a file is closed after using it |
| 8 | What is and how to use the `with` statement |
| 9 | What is JSON |
| 10 | What is serialization |
| 11 | What is deserialization |
| 12 | How to convert a Python data structure to a JSON string |
| 13 | How to convert a JSON string to a Python data structure |
| 14 | How to access command line parameters in a Python script |

---

## Task-by-Task Reference

Each task below highlights the **unique challenge** it posed and the **new technique** introduced to solve it — techniques from earlier tasks are not repeated. Use this as a quick revision guide.

---

### Task 0 — Read File (`0-read_file.py`)

**Challenge:** Read the entire contents of a UTF-8 text file and print it to stdout — without
adding an extra trailing newline beyond what the file already contains.

**Approach:** Use the `with open(filename, "r")` context manager to ensure the file is
automatically closed. Call `file.read()` to slurp the whole file, then pass `end=""` to
`print()` to suppress Python's automatic newline.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `with open(…, "r") as f:` | Context manager — guarantees file closure even on error |
| `file.read()` | Read entire file contents as a single string |
| `print(…, end="")` | Suppress the trailing newline `print` normally adds |

> **Key takeaway:** The `with` statement is the idiomatic way to work with files in Python —
> you never need to manually call `f.close()`.

---

### Task 1 — Write to a File (`1-write_file.py`)

**Challenge:** Write a string to a file (creating or overwriting it) and return the exact number
of characters written — counted *after* the write, not estimated from the input string.

**Approach:** Open the file in write mode `"w"` with explicit `encoding="utf-8"`, write the
text, then re-open the file in read mode inside a second `with` block and return
`len(file.read())`.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `encoding="utf-8"` | Explicitly declare the file's text encoding |
| `open(…, "w")` | Write mode — creates the file if missing, truncates if present |
| Re-opening in `"r"` for counting | Guarantees the character count matches what was actually persisted |

---

### Task 2 — Append to a File (`2-append_write.py`)

**Challenge:** Append text to a file and return the number of characters added — but more
efficiently than Task 1, without re-reading the file after writing.

**Approach:** Open in append mode `"a"`, write the text, and return `len(text)` directly.
Since append always writes exactly the provided string, there is no need to re-open and
measure from disk.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `open(…, "a")` | Append mode — writes to end of file, creates if missing |
| `return len(text)` | Direct length from the argument instead of re-reading the file |

> **Key takeaway:** Append mode never truncates; repeated calls keep accumulating content.

---

### Task 3 — To JSON String (`3-to_json_string.py`)

**Challenge:** Convert any serializable Python object (list, dict, string, int, float, bool,
None) into its JSON string representation — the first use of an external module in the project.

**Approach:** `import json` and call `json.dumps(my_obj)` to serialize the object.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `import json` | First import — brings the JSON encoder/decoder into scope |
| `json.dumps(obj)` | Serialize a Python object → JSON string |

> **Key takeaway:** `json.dumps()` stands for "dump string". Non-serializable types like
> `set` will raise `TypeError`.

---

### Task 4 — From JSON String (`4-from_json_string.py`)

**Challenge:** Convert a valid JSON string back into its native Python data structure
(list, dict, int, str, bool, None).

**Approach:** Use `json.loads(my_str)` — the inverse of `dumps`.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `json.loads(str)` | Deserialize a JSON string → Python object |

> **Key takeaway:** `json.loads()` stands for "load string". Malformed JSON raises
> `json.JSONDecodeError`.

---

### Task 5 — Save Object to a JSON File (`5-save_to_json_file.py`)

**Challenge:** Combine serialization and file writing into a single atomic-like operation —
take a Python object, convert it to JSON, and persist it to disk in one function call.

**Approach:** Open the file in write mode, then chain `json.dumps(my_obj)` directly as the
argument to `file.write()` inside the `with` block.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `file.write(json.dumps(obj))` | Chaining serialization + file I/O in one expression |

> **Key takeaway:** This is the composite of Task 1 (file write) + Task 3 (JSON dump).

---

### Task 6 — Load Object from a JSON File (`6-load_from_json_file.py`)

**Challenge:** Read a JSON file from disk and deserialize its contents back into a Python
object in one function.

**Approach:** Open the file in read mode, call `file.read()`, then pass the result to
`json.loads()`.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `json.loads(file.read())` | Chaining file read + deserialization in one expression |

> **Key takeaway:** This is the composite of Task 0 (file read) + Task 4 (JSON load).

---

### Task 7 — Load, Add, Save (`7-add_item.py`)

**Challenge:** Build a *standalone command-line script* (not a library function) that
accumulates arguments across multiple invocations into a persistent JSON list file —
a mini data-store that survives process restarts.

**Approach:** Use `sys.argv[1:]` to capture command-line arguments. Dynamically import
the functions from Tasks 5 and 6 via `__import__()`. On first run, catch `FileNotFoundError`
to start with an empty list. Guard executable code behind `if __name__ == "__main__"`.
Unpack arguments with `*sys.argv[1:]` into `main()`.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `import sys` + `sys.argv` | Access command-line parameters from within the script |
| `__import__("module").func` | Dynamic import — reuse functions from other task files |
| `try: … except FileNotFoundError:` | Gracefully handle the case where `add_item.json` doesn't exist yet |
| `if __name__ == "__main__":` | Guard — ensures code only runs when the file is executed directly |
| `*args` unpacking in function call | Spread `sys.argv[1:]` list into positional arguments of `main()` |

> **Key takeaway:** This task ties together file I/O, JSON, and the `sys` module to create
> a persistent CLI tool. `__import__()` lets you reuse your own earlier modules dynamically.

---

### Task 8 — Class to JSON (`8-class_to_json.py`)

**Challenge:** Extract *all* instance attributes from an arbitrary object as a plain
dictionary suitable for JSON serialization — without knowing the class definition in advance.

**Approach:** Return `obj.__dict__`, Python's built-in attribute that holds every writable
instance attribute as a dictionary. No `import json` needed here — this function produces the
dict, and the caller can serialize it.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `obj.__dict__` | Introspection — retrieve an object's instance namespace as a dict |

> **Key takeaway:** Every Python object has a `__dict__` that maps attribute names to values.
> This is the bridge between OOP and JSON serialization. Note that class-level attributes
> (defined outside `__init__`) are not in `__dict__`, and name-mangled private attributes
> (`__name`) appear with their mangled form (`_ClassName__name`).

---

### Task 9 — Student to JSON (`9-student.py`)

**Challenge:** Embed serialization logic into a class so that instances can serialize
*themselves* — moving from a standalone function (Task 8) to an instance method.

**Approach:** Define a `Student` class with a `to_json(self)` method that returns
`self.__dict__`. This is the same `__dict__` pattern from Task 8, now packaged as a
behavior of the object itself.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `self.__dict__` inside a method | Instance self-serialization — the object knows how to represent itself |
| Class definition with `__init__` | Establishing the `Student` class hierarchy used in Tasks 9–11 |

---

### Task 10 — Student to JSON with Filter (`10-student.py`)

**Challenge:** Allow *selective* serialization — let the caller request only specific
attribute names, and silently ignore any requested names that don't exist on the object.

**Approach:** Accept an optional `attrs` parameter (default `None`). Use `isinstance(attrs, list)` to validate input. If no filter is given, return the full `__dict__`. Otherwise, compute
which keys to remove via **set difference**: `all_keys - set(attrs)`, then `.pop()` each
unwanted key from a `.copy()` of `__dict__`. Wrap the pop loop in `try/except` so that
invalid keys in `attrs` are silently ignored.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `isinstance(obj, type)` | Type-check `attrs` to confirm it's a list before filtering |
| `set(dict.keys())` | Convert dict keys to a set for set operations |
| Set difference `all - requested` | Compute which keys to *remove* (the complement) |
| `dict.copy()` | Shallow-copy `__dict__` so pop doesn't mutate the original |
| `dict.pop(key)` | Remove a key from the copy |
| `try: … except Exception:` | Defensive pop — silently skip keys that don't exist on the instance |

> **Key takeaway:** Filtering by *removing* unwanted keys (rather than building up from the
> requested list) is a clever set-theory approach: you compute the complement and discard it.

---

### Task 11 — Student to Disk and Reload (`11-student.py`)

**Challenge:** Implement the *deserialization* side of the lifecycle — take a dictionary
(loaded from a JSON file) and restore a `Student` instance's state from it, overwriting
whatever attributes it currently holds.

**Approach:** Add a `reload_from_json(self, json)` method that calls
`self.__dict__.update(json)`. This mutates the instance's namespace in-place, replacing all
attributes with those in the dictionary. Combined with `to_json` (Task 10) and
`save_to_json_file`/`load_from_json_file` (Tasks 5/6), this completes the full round-trip:
serialize → persist → load → deserialize.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `self.__dict__.update(dict)` | In-place deserialization — restore object state from a dictionary |

> **Key takeaway:** `dict.update()` overwrites matching keys and adds new ones, making it a
> natural fit for rebuilding an object's state. This closes the serialization/deserialization
> loop: **Python object → `__dict__` → JSON string → file → JSON string → dict → `update()` → Python object**.

---

### Task 12 — Pascal's Triangle (`12-pascal_triangle.py`)

**Challenge:** Generate Pascal's triangle up to *n* rows algorithmically using only built-in
Python — no imports, no math formulas, no external libraries.

**Approach:** Pre-allocate an *n*×*n* matrix of zeros using a **list comprehension**:
`[[0] * n for _ in range(n)]`. Set the first and last element of each row to 1. Compute
internal cells by summing the two cells above-left and above. Finally, **trim** each row
to its first *i*+1 elements via slicing `a[i][:i+1]`.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `[[0] * n for _ in range(n)]` | List comprehension for 2D matrix initialization |
| In-place cell assignment `a[i][j] = …` | Build the triangle by mutating the pre-allocated grid |
| `int(a[i-1][j-1]) + int(a[i-1][j])` | Pascal's rule: each cell = sum of the two above it |
| Row trimming `a[i][:i+1]` | Slice each row down to the correct triangular length |

> **Key takeaway:** The matrix-first approach (fill a square, then trim) avoids the complexity
> of dynamically appending rows and is a common pattern for tabular algorithmic problems.

---

## Technique Inventory

| Task | New technique summarized | Category |
|------|--------------------------|----------|
| 0 | `with open()`, `file.read()`, `print(…, end="")` | File I/O |
| 1 | `encoding="utf-8"`, write mode `"w"`, re-open to count | File I/O |
| 2 | Append mode `"a"`, direct `len(text)` return | File I/O |
| 3 | `import json`, `json.dumps()` | JSON |
| 4 | `json.loads()` | JSON |
| 5 | Chain `file.write(json.dumps(obj))` | File I/O + JSON |
| 6 | Chain `json.loads(file.read())` | File I/O + JSON |
| 7 | `sys.argv`, `__import__()`, `try/except`, `__name__`, `*` unpacking | CLI & Scripting |
| 8 | `obj.__dict__` introspection | OOP |
| 9 | `self.__dict__` in a class method | OOP |
| 10 | `isinstance()`, set difference, `dict.copy()` + `dict.pop()` | OOP & Data |
| 11 | `self.__dict__.update(dict)` deserialization | OOP |
| 12 | 2D list comprehension, in-place matrix fill, row slicing | Algorithms |

---

## Resources

- [7.2. Reading and Writing Files — Python Docs](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [8.7. Predefined Clean-up Actions — Python Docs](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
- [Dive Into Python 3: Chapter 11. Files](https://diveintopython3.net/files.html)
- [JSON encoder and decoder — Python Docs](https://docs.python.org/3/library/json.html)
- [sys — System-specific parameters and functions](https://docs.python.org/3/library/sys.html)
