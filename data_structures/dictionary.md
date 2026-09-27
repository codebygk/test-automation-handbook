# Dictionary

## Definition

A **dictionary** is a mutable collection that stores data as **key-value pairs**.

```python
user = {
    "name": "John",
    "age": 30,
    "role": "QA"
}

print(user["name"])  # John
```

## Key Characteristics

- Stores key-value pairs
- Keys must be unique
- Keys must be hashable
- Values can be of any type
- Mutable
- Preserves insertion order
- Fast lookup by key
- Supports different value types

## Common Operations

```python
user = {"name": "John", "age": 30}

user["email"] = "john@example.com"   # Add
user["age"] = 31                     # Update

user.pop("age")                      # Remove
del user["email"]                    # Delete

print(user.get("name"))              # Get value safely
print("name" in user)                # Check key

print(user.keys())                   # Keys
print(user.values())                 # Values
print(user.items())                  # Key-value pairs
```

## Iteration

```python
user = {"name": "John", "age": 30}

for key, value in user.items():
    print(key, value)
```

## Time Complexity

| Operation | Average | Worst |
|---|---:|---:|
| Access by key | O(1) | O(n) |
| Insert | O(1) | O(n) |
| Update | O(1) | O(n) |
| Delete | O(1) | O(n) |
| Search by key | O(1) | O(n) |

## Why Is Dictionary Lookup O(1)?

Python dictionaries are implemented using a **hash table**.

```text
Key
 |
 v
Hash Function
 |
 v
Hash Value
 |
 v
Dictionary Table
 |
 v
Value
```

The hash of the key is used to locate the corresponding entry directly, making average lookup O(1).

## What Can Be a Key?

Keys must be **hashable** and therefore generally immutable.

```python
data = {
    "name": "John",
    10: "integer",
    (1, 2): "tuple"
}
```

Valid:

```python
str
int
float
tuple
frozenset
```

Invalid:

```python
list
dict
set
```

Example:

```python
data = {
    [1, 2]: "value"  # TypeError
}
```

## Dictionary vs List

| Feature | Dictionary | List |
|---|---|---|
| Structure | Key-value | Values |
| Access | By key | By index |
| Lookup | O(1) average | O(n) |
| Ordering | Insertion order | Ordered |
| Duplicate keys/values | Keys no, values yes | Yes |
| Use case | Fast lookup/mapping | Sequential collection |

## Dictionary vs Set

| Feature | Dictionary | Set |
|---|---|---|
| Stores | Key-value pairs | Values |
| Duplicate elements | Keys no | No |
| Lookup | O(1) average | O(1) average |
| Example | `{"id": 10}` | `{10, 20}` |

## Interview Points

- Python dictionaries use a hash table internally.
- Dictionary keys must be hashable.
- Keys must be unique.
- Values can be duplicated.
- Dictionary lookup is O(1) on average.
- Python dictionaries preserve insertion order.
- Mutable objects such as lists cannot be dictionary keys.
- `get()` is useful when a key may not exist.

## Common Interview Question

**Why can't a list be a dictionary key?**

Because a dictionary key must be hashable. Lists are mutable, so their contents can change and they are therefore not hashable.

**Why are dictionary lookups fast?**

Because Python uses hashing to locate keys rather than searching through every key sequentially.