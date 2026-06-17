# Python — Serialization

A progressive study of marshaling, pickling, CSV/JSON/XML serialization, and deserialization — transforming Python objects into storable, transmittable formats and back.

---

## Learning Objectives

| # | Concept |
|---|---------|
| 1 | Articulate the differences and similarities between marshaling and serialization |
| 2 | Implement serialization with JSON (`json.dumps`/`json.loads`) and Pickle |
| 3 | Convert between data formats (CSV → JSON) using standard library modules |
| 4 | Serialize and deserialize data using XML (`xml.etree.ElementTree`) |
| 5 | Evaluate tradeoffs between JSON, XML, Pickle, and CSV for different use cases |

---

## Task-by-Task Reference

Each task below highlights the **unique challenge** it posed and the **new technique** introduced — techniques from earlier tasks are not repeated.

---

### Task 0 — Basic JSON Serialization (`task_00_basic_serialization.py`)

**Challenge:** Serialize a Python dictionary to a JSON file and deserialize it back — introducing the fundamental write-then-read cycle of data persistence.

**Approach:** `serialize_and_save_to_file()` opens the file in write mode and uses `json.dump(data, f)` to write. `load_and_deserialize()` opens in read mode and uses `json.load(f)` to reconstruct the dictionary.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `json.dump(obj, file)` | Serialize a Python object directly to a file handle |
| `json.load(file)` | Deserialize JSON from a file handle back into a Python object |
| `with open(filename, 'w')` for write | Open a file for writing (creates or replaces) |

> **Key takeaway:** `json.dump`/`json.load` work with file handles — the `with` statement ensures proper file closure even on errors.

---

### Task 1 — Pickling Custom Classes (`task_01_pickle.py`)

**Challenge:** Serialize an entire Python class instance (not just primitive data) — introducing the Pickle module for object-state persistence and `@classmethod` for alternative constructors.

**Approach:** `serialize()` uses `pickle.dump(self, file)` to save the full instance state. `deserialize()` is a `@classmethod` that reads with `pickle.load(file)` and returns a reconstructed `CustomObject`. Exception handling returns `None` for missing/corrupt files.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `pickle.dump(obj, file)` | Serialize an arbitrary Python object (including class instances) to a file |
| `pickle.load(file)` | Deserialize and reconstruct a Python object from a pickled file |
| `@classmethod` alternative constructor | Create an instance from serialized data without a pre-existing instance |
| Try/except for file-not-found | Defensive serialization — return `None` instead of crashing |

> **Key takeaway:** Pickle preserves the full state of Python objects, including custom classes. Unlike JSON, it's Python-specific and can execute arbitrary code — only unpickle trusted data.

---

### Task 2 — CSV to JSON Conversion (`task_02_csv.py`)

**Challenge:** Read tabular CSV data and transform it into structured JSON — introducing format conversion between two common data interchange formats.

**Approach:** `csv.DictReader` reads each CSV row as an `OrderedDict`. The list of dicts is then serialized with `json.dump()` to `data.json`. A try/except wraps the entire operation, returning `False` on failure.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `csv.DictReader(file)` | Read CSV rows as dictionaries with column headers as keys |
| `json.dump(list_of_dicts, file, indent=4)` | Serialize a list of dicts with pretty-printing |
| Cross-format conversion pattern | Read from format A, write to format B in one function |
| Boolean return for success/failure | Signal conversion status to calling code |

> **Key takeaway:** `csv.DictReader` maps column headers to dictionary keys automatically — the bridge from tabular data to structured serialization is one import away.

---

### Task 3 — XML Serialization (`task_03_xml.py`)

**Challenge:** Build an XML tree from a dictionary and parse it back — introducing hierarchical markup serialization as an alternative to JSON.

**Approach:** `serialize_to_xml()` creates a root `<data>` element with `ET.Element`, iterates dict items, creates child elements with `.text` assignments, and writes with `ET.ElementTree.write()`. `deserialize_from_xml()` uses `ET.parse()` and iterates child elements to rebuild the dictionary.

**New techniques introduced:**

| Technique | Purpose |
|-----------|---------|
| `ET.Element(tag)` | Create an XML element node with a given tag name |
| `ET.SubElement(parent, tag)` | Create and attach a child element in one step |
| `element.text = value` | Set the text content of an XML element |
| `ET.ElementTree(root).write(file)` | Serialize an XML tree to a file with optional encoding/declaration |
| `ET.parse(file).getroot()` | Parse an XML file and retrieve the root element |

> **Key takeaway:** XML is more verbose than JSON but supports attributes, namespaces, and schema validation. `ElementTree` provides a lightweight DOM-like API for tree construction and traversal.

---

## Technique Inventory

| Task | New technique summarized | Category |
|------|--------------------------|----------|
| 0 | `json.dump()` / `json.load()` for dict-to-file serialization | JSON Serialization |
| 1 | `pickle.dump()` / `pickle.load()` for full object-state persistence | Pickling |
| 2 | `csv.DictReader()` + format conversion pattern (CSV → JSON) | File I/O & Formats |
| 3 | `xml.etree.ElementTree` — tree construction, parsing, and serialization | XML Serialization |

---

## Resources

- [Python JSON Module — Official Docs](https://docs.python.org/3/library/json.html)
- [Python Pickle Module — Official Docs](https://docs.python.org/3/library/pickle.html)
- [Python CSV Module — Official Docs](https://docs.python.org/3/library/csv.html)
- [xml.etree.ElementTree — Official Docs](https://docs.python.org/3/library/xml.etree.elementtree.html)
- [Real Python: Serialization and Deserialization](https://realpython.com/python-serialize-data/)
- [Real Python: Working With JSON Data in Python](https://realpython.com/python-json/)
- [Real Python: Serialize Python Objects With Pickle](https://realpython.com/python-pickle-module/)

