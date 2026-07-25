# 📄 JSON in Python

A collection of Python examples demonstrating how to work with JSON data using Python's built-in `json` module. These examples cover JSON parsing, serialization, and custom serialization techniques commonly used in Python applications.

## 📚 Topics Covered

- JSON Basics
- `json.loads()`
- `json.dumps()`
- Custom JSON Serialization
- Universal JSON Serialization
- Reading JSON Files *(Coming Soon)*
- Writing JSON Files *(Coming Soon)*

---

## 🛠 Technologies Used

- Python 3
- JSON Module (`json`)
- datetime Module

---

## 📂 Project Structure

```text
JSON/
├── 01_json_loads.py
├── 02_json_dumps.py
├── 03_json_custom_serializer.py
├── 04_json_universal_serializer.py
└── README.md
```

---

## 01. JSON Loads

Parse a JSON string into a Python dictionary using `json.loads()`.

### ✨ Features

- Convert JSON string to Python dictionary
- Handle Boolean (`true` → `True`)
- Handle `null` (`null` → `None`)
- Access nested objects and arrays

### 🛠 Concepts

- `json.loads()`
- JSON Parsing
- Python Dictionary
- Lists in JSON

---

## 02. JSON Dumps

Convert a Python dictionary into a JSON-formatted string using `json.dumps()`.

### ✨ Features

- Convert Python dictionary to JSON string
- Serialize nested dictionaries and lists
- Handle Boolean and `None` values
- Generate API-ready JSON

### 🛠 Concepts

- `json.dumps()`
- JSON Serialization
- Nested JSON Objects
- Lists in JSON

---

## 03. JSON Custom Serializer

Serialize non-JSON objects such as `datetime.date` using a custom serializer.

### ✨ Features

- Serialize `datetime.date`
- Use `default` parameter
- Convert date to ISO 8601 format
- Handle unsupported objects safely

### 🛠 Concepts

- `json.dumps()`
- Custom Serializer
- `default`
- `datetime.date`
- ISO 8601

---

## 04. JSON Universal Serializer

Serialize multiple non-JSON Python objects using a single custom serializer function.

### ✨ Features

- Serialize `datetime` objects
- Convert `bytes` to strings
- Convert `set` to lists
- Serialize custom Python class objects
- Use the `default` parameter in `json.dumps()`

### 🛠 Concepts

- `json.dumps()`
- Custom Serializer
- `default`
- `datetime`
- `bytes`
- `set`
- Custom Class Serialization

---

## 🎯 Learning Outcomes

- Parse JSON strings into Python objects
- Convert Python objects into JSON strings
- Work with nested JSON objects and arrays
- Handle Boolean and `null` values
- Serialize custom Python objects
- Build JSON data for APIs and web applications

---

## 👨‍💻 Author

**Akash Raval**  
Python Developer Aspirant | Learning Web Development & Cyber Security
