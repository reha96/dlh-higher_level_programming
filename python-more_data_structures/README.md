# Python — More Data Structures: Sets, Dictionaries

A progressive study of sets, dictionaries, `map()`/`lambda`, sorting with keys, and advanced data manipulation in Python.

---

## Learning Objectives

| # | Concept |
|---|---------|
| 1 | What are sets and how to use them |
| 2 | What are the most common methods of sets and how to use them |
| 3 | When to use sets versus lists |
| 4 | How to iterate through a set |
| 5 | What are dictionaries and how to use them |
| 6 | When to use dictionaries versus lists or sets |
| 7 | What is a key in a dictionary |
| 8 | How to iterate through a dictionary |
| 9 | What is a lambda function |
| 10 | What are the `map()`, `reduce()`, and `filter()` functions |

---

## Task-by-Task Reference

Each task below highlights the **unique challenge** it posed and the **new technique** introduced to solve it — techniques from earlier tasks are not repeated. Use this as a quick revision guide.

---

### Task 0 — Square Matrix Elements (`0-square_matrix_simple.py`)

**Challenge:** Transform every element of a 2D matrix by squaring it — introducing
`map()` with `lambda` for functional-style transformation.

**Approach:** For each row of the matrix, call `map(lambda x: x*x, matrix[i])` which applies
the squaring function to every element. Wrap in `list()` to materialize the map object, then
append to the result. The outer loop creates a new matrix row by row.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `map(function, iterable)` | Apply a function to every element of an iterable |
| `lambda x: x * x` | Anonymous inline function — takes `x`, returns `x²` |
| `list(map(…))` | Materialize the lazy `map` object into a concrete list |

> **Key takeaway:** `map()` is a functional programming tool — it transforms every element
> without an explicit loop. `lambda` creates a one-line function without `def`. Together
> they're a concise transformation pattern.

---

### Task 1 — Search and Replace (`1-search_replace.py`)

**Challenge:** Replace all occurrences of a value in a list with a new value, returning a
new list — introducing conditional list building.

**Approach:** Create an empty `out` list. Iterate the input list by index, compare each
element to `search`: if equal, append `replace`; otherwise, append the original value.
Return the new list — the original is unchanged.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| Conditional list building (`if`/`else` inside loop) | Build a new list where each element is conditionally transformed |
| Copy-on-write pattern | Return a modified copy without mutating the original |

> **Key takeaway:** When you need to replace matches but preserve non-matches, build a new
> list element by element. This avoids mutating the original and is more predictable.

---

### Task 2 — Sum Unique Elements (`2-uniq_add.py`)

**Challenge:** Sum all elements of a list, counting each value only once — introducing
Python's `set` for automatic deduplication.

**Approach:** Convert the list to a `set(my_list)` — duplicates are automatically removed.
Then iterate the set and accumulate the sum. The order of iteration doesn't matter since
addition is commutative.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `set(iterable)` | Create a set — an unordered collection of unique elements |
| Set iteration (`for i in set`) | Iterate over unique values only |

> **Key takeaway:** A `set` is an unordered collection with no duplicates. Converting a list
> to a set is the simplest way to get unique values. Sets don't support indexing or slicing.

---

### Task 3 — Common Elements (`3-common_elements.py`)

**Challenge:** Find elements present in both of two sets — introducing set intersection.

**Approach:** Use the `&` operator: `set_1 & set_2`. This returns a new set containing only
elements that appear in both operands. Return the intersection directly.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `set_1 & set_2` | Set intersection — elements present in both sets |
| Operator-based set operations | `&` = intersection, `|` = union, `-` = difference, `^` = symmetric difference |

> **Key takeaway:** Set operators are the cleanest way to do mathematical set operations
> in Python. `&` finds common ground — what both sets share.

---

### Task 4 — Elements in Only One Set (`4-only_diff_elements.py`)

**Challenge:** Find elements that appear in exactly one of two sets (not both) — introducing
symmetric difference (XOR for sets).

**Approach:** Use the `^` operator: `set_1 ^ set_2`. This returns a new set containing
elements that are in either set but NOT in both. It's the union minus the intersection.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `set_1 ^ set_2` | Symmetric difference — elements in either set but not both |

> **Key takeaway:** `^` on sets is XOR logic: include elements that are unique to each set.
> `{1, 2} ^ {2, 3}` → `{1, 3}` — 2 is excluded because it's in both.

---

### Task 5 — Number of Keys (`5-number_keys.py`)

**Challenge:** Count how many keys a dictionary has — introducing the `keys()` method and
dictionary length.

**Approach:** Call `a_dictionary.keys()` to get a view of all keys, then pass to `len()`.
Alternatively, `len(a_dictionary)` directly works because dictionaries are sized by key count.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `dict.keys()` | Get a view object of all dictionary keys |
| `len(dictionary)` | Count the number of key-value pairs in a dictionary |

> **Key takeaway:** `len(dict)` is the idiomatic way to count keys. `dict.keys()` returns
> a dynamic view — it reflects changes to the dictionary in real time.

---

### Task 6 — Print Sorted Dictionary (`6-print_sorted_dictionary.py`)

**Challenge:** Print dictionary entries sorted alphabetically by key — introducing key
sorting and the `dict.get()` method for value retrieval.

**Approach:** Extract keys with `.keys()`, convert to `list()` and `.sort()`. Iterate
sorted keys and print each as `"{}: {}".format(key, a_dictionary.get(key))`. Using `.get()`
is safe — it returns `None` if the key disappears, though that shouldn't happen here.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `list(dict.keys())` + `.sort()` | Extract and sort dictionary keys |
| `dict.get(key)` | Retrieve value by key — returns `None` instead of raising `KeyError` |
| `"{}: {}".format(key, value)` | Print key-value pairs with consistent formatting |

> **Key takeaway:** Dictionaries are unordered (insertion-ordered in Python 3.7+). To
> display them alphabetically, sort the keys and retrieve values by iterating the sorted
> key list. `.get()` is safer than `[]` for lookup.

---

### Task 7 — Update Dictionary (`7-update_dictionary.py`)

**Challenge:** Add or update a key-value pair in a dictionary — introducing the
`dict.update()` method.

**Approach:** Create a tuple `(key, value)`, wrap in a list `[(key, value)]`, and call
`a_dictionary.update([insert])`. If the key exists, its value is overwritten. If not,
a new key-value pair is added. Return the modified dictionary.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `dict.update([(key, value)])` | Add or update key-value pairs from an iterable of tuples |
| `dict.update()` upsert behavior | If key exists → overwrite; if not → insert |

> **Key takeaway:** `update()` accepts a list of `(key, value)` tuples, another dictionary,
> or keyword arguments. It's the universal way to merge data into a dictionary.

---

### Task 8 — Simple Delete (`8-simple_delete.py`)

**Challenge:** Delete a key from a dictionary only if it exists — introducing `del` on
dictionary keys and key membership testing.

**Approach:** Check `if key in a_dictionary.keys()`. If present, `del a_dictionary[key]`
removes the key-value pair. Return the dictionary either way. The check prevents `KeyError`
on non-existent keys.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `del dict[key]` | Delete a key-value pair from a dictionary in-place |
| `key in dict.keys()` | Test whether a key exists before operating on it |

> **Key takeaway:** `del dict[key]` raises `KeyError` if the key doesn't exist. Always check
> with `key in dict` (or `key in dict.keys()`) first unless you're certain the key exists.

---

### Task 9 — Multiply Values by 2 (`9-multiply_by_2.py`)

**Challenge:** Transform every value in a dictionary by multiplying by 2, returning a new
dictionary — introducing dictionary iteration and value transformation.

**Approach:** Create an empty `out = {}`. Iterate `for i in a_dictionary:` (which gives keys
by default). Assign `out[i] = a_dictionary[i] * 2`. Return the new dictionary; the original
is unchanged.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `for key in dict` iteration | Iterate over dictionary keys (default behavior) |
| `new_dict[key] = value * n` | Transform dictionary values while building a new dict |

> **Key takeaway:** `for key in dict` iterates over keys by default. Use `dict.items()` if
> you need both keys and values. `dict.values()` iterates over values only.

---

### Task 10 — Best Score (`10-best_score.py`)

**Challenge:** Find the key with the highest associated value in a dictionary — introducing
`dict.items()`, `sorted()` with a custom `key` function, and `lambda`.

**Approach:** Handle empty/None case first (return `None`). Otherwise, use
`sorted(a_dictionary.items(), key=lambda item: item[1], reverse=True)` to sort by value
(descending). The `lambda item: item[1]` extracts the value from each `(key, value)` tuple.
Return the key of the first (highest) entry.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `dict.items()` | Get an iterable of `(key, value)` tuples |
| `sorted(iterable, key=lambda item: item[1])` | Sort by a custom criterion — here, by value |
| `reverse=True` | Sort in descending order (highest first) |
| `lambda item: item[1]` | Anonymous function that extracts the second element of a tuple |

> **Key takeaway:** `sorted()` with `key` is Python's most powerful sorting tool. The `key`
> function transforms each element before comparison. `lambda` is perfect for these one-off
> extraction functions. `items()` is essential for working with key-value pairs.

---

### Task 11 — Multiply List by Map (`11-multiply_list_map.py`)

**Challenge:** Multiply every element in a list by a given number using `map()` — introducing
a parameterized lambda that captures an external variable.

**Approach:** `map(lambda x: x * number, my_list)` applies the multiplication to each
element. The `lambda` captures `number` from the enclosing scope (closure). Wrap in `list()`
and return.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `lambda x: x * number` (closure) | Lambda that captures an external variable from the enclosing scope |
| `map()` with parameterized function | Transform each element using a configurable multiplier |

> **Key takeaway:** Lambdas can access variables from the enclosing scope (closures). In
> `lambda x: x * number`, `number` is captured at call time. This makes `map()` flexible —
> the transformation adapts to the parameter.

---

### Task 12 — Roman to Integer (`12-roman_to_int.py`)

**Challenge:** Convert a Roman numeral string to its integer value — introducing dictionary
lookup tables for symbol-value mapping and the subtraction rule for Roman numerals.

**Approach:** Create a `map = {"M": 1000, …}` lookup dictionary. Validate input type.
For single-character strings, return the mapped value directly. For multi-character strings,
compare each symbol to its neighbor: if the current symbol is smaller than the next, apply
the subtraction rule (IV = 4, IX = 9, etc.); otherwise, add normally.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| Dictionary as a lookup table | Map symbols to values for O(1) retrieval |
| Roman numeral subtraction rule | If a smaller value precedes a larger, subtract instead of add |
| `type() is not str` validation | Reject non-string input at the start |
| Neighbor comparison in strings | Compare `map[s[i]]` to `map[s[i+1]]` for precedence decisions |

> **Key takeaway:** Dictionaries are natural lookup tables. The Roman numeral algorithm
> hinges on one rule: if symbol[i] < symbol[i+1], subtract it; otherwise, add it. This
> is a classic use case for dict-based symbol mapping.

---

### Task 13 — Weighted Average (`100-weight_average.py`)

**Challenge:** Calculate the weighted average from a list of `(score, weight)` tuples —
introducing tuple unpacking in loops and the weighted mean formula.

**Approach:** Handle empty list (return 0). For each tuple in the list, unpack as
`i[0]` (score) and `i[1]` (weight). Accumulate `score * weight` and `weight` separately.
Return `total_weighted / total_weight`. This implements Σ(score × weight) / Σ(weight).

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| Tuple unpacking in loop (`i[0]`, `i[1]`) | Extract score and weight from each tuple |
| Weighted average formula | `Σ(score × weight) / Σ(weight)` |
| Dual accumulator pattern | Track two running totals simultaneously |

> **Key takeaway:** A weighted average gives more importance to items with higher weights.
> The formula is `sum(score_i × weight_i) / sum(weight_i)`. Two accumulators in one loop
> is a clean way to compute both sums.

---

### Task 14 — Square Matrix Map (`101-square_matrix_map.py`)

**Challenge:** Square every element of a 2D matrix using ONLY `map()` and `lambda` — no
explicit loops or list comprehensions — introducing nested `map()`.

**Approach:** The outer `map()` iterates over rows. Its lambda does an inner
`map(lambda x: x**2, i)` on each row, wrapped in `list()`. The outer result is also wrapped
in `list()`. This is `map()` all the way down — functional programming style.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| Nested `map()` (outer + inner) | Apply `map()` at two levels — for rows and for elements within rows |
| `map(lambda i: list(map(lambda x: x**2, i)), matrix)` | Pure functional 2D transformation |
| `x**2` exponentiation in lambda | Alternative to `x*x` — `**2` is the square operator |

> **Key takeaway:** `map()` can be nested to handle multi-dimensional data. The outer map
> processes rows, and each row's lambda applies an inner map to its elements. This is
> functional programming without a single `for` loop.

---

### Task 15 — Complex Delete (`102-complex_delete.py`)

**Challenge:** Delete ALL dictionary entries whose value matches a given value — introducing
safe iteration during deletion by taking a snapshot of keys.

**Approach:** Extract `keys = list(a_dictionary.keys())` — a snapshot of all keys at this
moment. Iterate this snapshot (not the live dict) and call `a_dictionary.pop(i)` for each
key whose value matches. Returning a snapshot avoids the "dictionary changed size during
iteration" error.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `list(dict.keys())` snapshot | Create a static copy of keys for safe iteration during deletion |
| `dict.pop(key)` | Remove a key and return its value |
| Safe deletion during iteration | Never modify a dict while iterating over it — use a key snapshot |

> **Key takeaway:** You cannot modify a dictionary (add/remove keys) while iterating over it
> directly — Python raises `RuntimeError: dictionary changed size during iteration`. The
> fix is to iterate over a snapshot: `list(dict.keys())`.

---

## Technique Inventory

| Task | New technique summarized | Category |
|------|--------------------------|----------|
| 0 | `map()` + `lambda`, `list(map(…))` materialization | Functional Programming |
| 1 | Conditional list building, copy-on-write pattern | Lists |
| 2 | `set()` deduplication, set iteration | Sets |
| 3 | `&` set intersection operator | Sets |
| 4 | `^` symmetric difference (XOR) operator | Sets |
| 5 | `dict.keys()`, `len(dict)` for key count | Dictionaries |
| 6 | `sorted(keys)`, `dict.get()`, key: value formatting | Dictionaries |
| 7 | `dict.update([(key, value)])` upsert | Dictionaries |
| 8 | `del dict[key]`, `key in dict.keys()` membership | Dictionaries |
| 9 | `for key in dict` iteration, value transformation | Dictionaries |
| 10 | `dict.items()`, `sorted()` with `key=lambda`, `reverse=True` | Sorting & Lambda |
| 11 | Closure lambda `lambda x: x*number`, parameterized `map()` | Functional Programming |
| 12 | Dict lookup table, Roman numeral algorithm, neighbor comparison | Algorithms |
| 13 | Tuple unpacking in loop, weighted average, dual accumulator | Algorithms |
| 14 | Nested `map()`, `x**2` exponentiation, pure functional 2D transform | Functional Programming |
| 15 | `list(dict.keys())` snapshot, `dict.pop()`, safe iteration during deletion | Dictionaries |

---

## Resources

- [5. Data Structures — Sets and Dictionaries](https://docs.python.org/3/tutorial/datastructures.html)
- [Built-in Functions — `map()`, `sorted()`, `lambda`](https://docs.python.org/3/library/functions.html)
- [Sorting HOW TO — `key` parameter](https://docs.python.org/3/howto/sorting.html#key-functions)
- [Set Types — `set`, `frozenset`](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
- [Mapping Types — `dict`](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)