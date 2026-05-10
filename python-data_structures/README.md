# Python — Data Structures: Lists, Tuples

A progressive study of Python's core sequence types: list iteration, indexing, mutation, copying, tuple operations, and matrix traversal.

---

## Learning Objectives

| # | Concept |
|---|---------|
| 1 | What are lists and how to use them |
| 2 | What are the differences and similarities between strings and lists |
| 3 | What are the most common methods of lists and how to use them |
| 4 | How to use lists as stacks and queues |
| 5 | What are list comprehensions and how to use them |
| 6 | What are tuples and how to use them |
| 7 | When to use tuples versus lists |
| 8 | What is a sequence |
| 9 | What is tuple packing |
| 10 | What is sequence unpacking |
| 11 | What is the `del` statement and how to use it |

---

## Task-by-Task Reference

Each task below highlights the **unique challenge** it posed and the **new technique** introduced to solve it — techniques from earlier tasks are not repeated. Use this as a quick revision guide.

---

### Task 0 — Print List Integers (`0-print_list_integer.py`)

**Challenge:** Iterate over a list and print each integer on its own line — introducing
list traversal and formatted integer printing.

**Approach:** Use `for i in my_list:` to iterate directly over list elements. Print each
with `"{:d}".format(i)` which ensures only integers are formatted. The loop produces one
line per element.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `for element in list:` | Direct iteration — each element is yielded in order |
| `"{:d}".format(i)` | Format an integer for display — raises error on non-integers |

> **Key takeaway:** `for item in my_list` is the idiomatic way to iterate a list in Python.
> You get each element directly — no index variable needed unless you need the position.

---

### Task 1 — Element At Index (`1-element_at.py`)

**Challenge:** Safely retrieve a list element by index — introducing bounds checking and
the `None` sentinel for invalid access.

**Approach:** Before accessing `my_list[idx]`, validate the index: `if idx >= len(my_list) or idx < 0`.
If out of bounds, `return None`. Otherwise, `return my_list[idx]`. The function never crashes
on bad input.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `idx >= len(my_list)` | Check upper bound — maximum valid index is `len(list) - 1` |
| `idx < 0` | Check lower bound — Python allows negative indices, but this function rejects them |
| `return None` as sentinel | Return a special value to indicate "no result" instead of crashing |

> **Key takeaway:** Negative indices are valid in Python (`list[-1]` is the last element),
> but you may want to reject them depending on the function contract. `None` is the standard
> Python sentinel for "no value."

---

### Task 2 — Replace in List (`2-replace_in_list.py`)

**Challenge:** Modify an element in-place at a given index, but only if the index is valid —
introducing list mutation with bounds guarding.

**Approach:** Same bounds check as Task 1. If valid, `my_list[idx] = element` mutates the
original list. Return the (now modified) list. If invalid, return the list unchanged.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `my_list[idx] = value` | Mutate a list element at a specific index |
| Return the mutated list | Allow chaining or further use of the modified list |

> **Key takeaway:** Lists are mutable — assignment at an index changes the list in-place.
> The original list (not a copy) is modified. This is different from strings, which are
> immutable.

---

### Task 3 — Print Reversed List (`3-print_reversed_list_integer.py`)

**Challenge:** Print a list's elements in reverse order without using `.reverse()` or
reversed-range indexing — introducing negative indexing within a forward loop.

**Approach:** Use a forward `for i in my_list:` but access `my_list[-i]` for printing.
Negative indices count from the end: `-1` is last, `-2` is second-to-last, etc. This prints
elements in reverse order.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `my_list[-i]` in forward loop | Access elements from the end using negative indexing |
| Negative index semantics | `-1` = last, `-len(list)` = first — count backwards from end |

> **Key takeaway:** Negative indexing is a concise way to access list elements from the end.
> `my_list[-1]` always gives the last element regardless of list length.

---

### Task 4 — New List with Replacement (`4-new_in_list.py`)

**Challenge:** Return a modified COPY of a list, leaving the original unchanged —
introducing the immutability pattern for list operations.

**Approach:** Create an empty list `new_list = []`. Copy all elements from `my_list` with
`for i in my_list: new_list.append(i)`. Then mutate `new_list[idx] = element` and return
the copy. The original `my_list` is never touched.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `new_list.append(i)` for copying | Build a new list by iterating and appending from the original |
| Immutable update pattern | Return a modified copy; original remains unchanged |

> **Key takeaway:** The "copy, modify, return" pattern preserves the original data. This is
> important when other code holds references to the original list and expects it not to change.

---

### Task 5 — Remove 'c' and 'C' (`5-no_c.py`)

**Challenge:** Remove all occurrences of both 'c' and 'C' from a string without using
`.replace()` — introducing the `split`/`join` pattern for character removal.

**Approach:** Check if `"C" in my_string`, then `split('C')` breaks the string at every 'C',
and `''.join()` reassembles it without them. Repeat for `'c'`. Loop until no more 'c' or 'C'
remains (each iteration removes one level).

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `str.split(separator)` | Split a string into a list of substrings at each occurrence of separator |
| `''.join(list_of_strings)` | Join a list of strings with no separator (empty string) |
| `"C" in my_string` membership test | Check if a substring exists in a string |
| Split/join for character removal | Remove characters by splitting on them and rejoining the pieces |

> **Key takeaway:** `split(char)` + `''.join()` is a pattern for stripping characters from
> a string. It works because `split` removes the separator, and `join` reassembles the
> remaining pieces.

---

### Task 6 — Print Matrix (`6-print_matrix_integer.py`)

**Challenge:** Print a 2D matrix (list of lists) with proper formatting: numbers separated
by spaces, rows separated by newlines — introducing nested iteration over a matrix.

**Approach:** Outer loop iterates rows: `for i in range(len(matrix))`. Print a newline
before each row (except the first). Inner loop iterates columns: `for j in range(len(matrix[i]))`.
Print each cell with `"{:d}".format()`, appending a space unless it's the last column.
End with a final newline.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `matrix[i][j]` 2D access | Access element at row `i`, column `j` in a list of lists |
| `len(matrix[i])` for row length | Each row can have its own length |
| Conditional separator: `if j != len(matrix[i]) - 1` | Add spaces between cells but not after the last |
| Row-separator newlines (`if i > 0: print()`) | Add newline between rows, not before the first |

> **Key takeaway:** A matrix in Python is a list of lists. Access is `matrix[row][col]`.
> Each row is a separate list, so rows can have different lengths (ragged arrays).

---

### Task 7 — Add Two Tuples (`7-add_tuple.py`)

**Challenge:** Add two tuples element-wise, but handle tuples shorter than 2 elements by
padding with 0 — introducing tuple manipulation, conversion, and padding.

**Approach:** Convert both tuples to lists with `list()`. Pad to at least 2 elements by
appending 0 if needed. Convert back to `tuple()`. Add `tuple_a[0] + tuple_b[0]` and
`tuple_a[1] + tuple_b[1]`, then return the result as a tuple: `(sum_1, sum_2)`.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `list(tuple)` / `tuple(list)` | Convert between tuple (immutable) and list (mutable) |
| `list.append(0)` for padding | Extend a sequence to the required length with default values |
| Element-wise tuple addition | Add corresponding positions from two tuples |
| `(x, y)` tuple literal return | Create and return a tuple inline |

> **Key takeaway:** Tuples are immutable, so to add elements you convert to list, modify,
> and convert back. Padding ensures short tuples behave as if they have default values (0).

---

### Task 8 — Multiple Returns (`8-multiple_returns.py`)

**Challenge:** Return two related pieces of data from a single function — introducing tuple
packing in return statements and handling empty input gracefully.

**Approach:** Compute `length = len(sentence)`. If `length > 0`, return `(length, sentence[0])`
— a tuple of the length and first character. If empty, return `(0, None)` — the first
character is `None` since there isn't one.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `return (value1, value2)` | Return multiple values as a tuple — the caller can unpack them |
| `None` for missing first character | Represent "no character" when the string is empty |

> **Key takeaway:** Python functions can return multiple values by packing them into a tuple.
> The caller typically unpacks: `length, first = multiple_returns("hello")`.

---

### Task 9 — Max Integer (`9-max_integer.py`)

**Challenge:** Find the maximum value in a list without using `max()` — introducing
in-place sorting and the empty-list edge case.

**Approach:** Check `len(my_list) > 0`. If so, call `my_list.sort()` (sorts in-place,
ascending), then return `my_list[-1]` (the last element = largest). If empty, return `None`.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `list.sort()` | Sort a list in-place (ascending by default) |
| `my_list[-1]` for max via sorting | After sorting, the last element is the maximum |
| `return None` for empty list | Sentinel for "no maximum" when list is empty |

> **Key takeaway:** `list.sort()` modifies the list in-place and returns `None` (not the
> sorted list). For a non-destructive alternative, use `sorted(list)` which returns a new
> sorted copy.

---

### Task 10 — Divisible by 2 (`10-divisible_by_2.py`)

**Challenge:** Map each integer in a list to a boolean indicating divisibility by 2 —
introducing the pattern of building a parallel boolean list.

**Approach:** Create an empty `out = []` list. For each element, check `i % 2 == 0` and
append `True` or `False`. Return the boolean list, which has the same length as the input.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| Boolean list building with `list.append()` | Create a parallel list of True/False values |
| `i % 2 == 0` divisibility check | Modulo provides a boolean test for even/odd |

> **Key takeaway:** This is a classic "map" pattern — transform each element of a list into
> a corresponding value in a new list. The result list is parallel (same length, same order).

---

### Task 11 — Delete At Index (`11-delete_at.py`)

**Challenge:** Remove an element at a specific index from a list — introducing list removal
methods and index-based deletion.

**Approach:** Validate the index with the standard bounds check. If valid, call
`my_list.remove(idx + 1)` — using `.remove()` to delete by value, not by index. Return
the modified list.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `list.remove(value)` | Remove the first occurrence of a value from the list |

> **Key takeaway:** `list.remove(x)` removes by VALUE (first match), while `del list[i]`
> removes by INDEX. `list.pop(i)` removes by index AND returns the removed element.

---

### Task 12 — Switch Values (`12-switch.py`)

**Challenge:** Swap the values of two variables without using a temporary third variable —
introducing Python's tuple unpacking swap idiom.

**Approach:** `a, b = b, a` — the right side creates a tuple `(b, a)`, and the left side
unpacks it into `a` and `b` simultaneously. No temporary variable needed.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `a, b = b, a` tuple unpacking swap | Swap two variables in a single line without a temp variable |

> **Key takeaway:** Python's tuple packing/unpacking makes swapping trivial. The right side
> is evaluated first (creating a temporary tuple), then assigned. This is not just a syntax
> trick — it's a core feature of Python's assignment semantics.

---

## Technique Inventory

| Task | New technique summarized | Category |
|------|--------------------------|----------|
| 0 | `for item in list`, `{:d}` integer format | List Iteration |
| 1 | Bounds checking (`idx < 0 or idx >= len`), `None` sentinel | List Access |
| 2 | `list[idx] = value` in-place mutation | List Mutation |
| 3 | Negative indexing `list[-i]` for reverse order | List Indexing |
| 4 | `list.append()` copy, immutable update pattern | List Patterns |
| 5 | `str.split()`, `''.join()`, `in` membership, character removal | String Operations |
| 6 | 2D matrix `matrix[i][j]`, nested `len()`, conditional separators | Matrix |
| 7 | `list()`/`tuple()` conversion, padding, element-wise tuple addition | Tuples |
| 8 | `return (val1, val2)` multiple return, `None` for missing char | Tuples |
| 9 | `list.sort()` in-place, `list[-1]` for max | List Methods |
| 10 | Boolean list building with `append()` | List Patterns |
| 11 | `list.remove(value)` remove by value | List Methods |
| 12 | `a, b = b, a` tuple unpacking swap | Tuples |

---

## Resources

- [5. Data Structures — Python Docs](https://docs.python.org/3/tutorial/datastructures.html)
- [Lists — Python Tutorial](https://docs.python.org/3/tutorial/introduction.html#lists)
- [Tuples and Sequences — Python Docs](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [Sequence Types — `list`, `tuple`, `range`](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)
- [Sorting HOW TO — Python Docs](https://docs.python.org/3/howto/sorting.html)