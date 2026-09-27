# Set

## Definition

A **set** is an unordered collection of **unique elements**.

```python
numbers = {10, 20, 30, 20}

print(numbers)  # {10, 20, 30}
```

Duplicate values are automatically removed.

## Key Characteristics

- Stores unique elements
- No duplicate values
- Mutable
- Unordered conceptually
- Elements must be hashable
- Fast membership testing
- Supports mathematical set operations
- Does not support indexing

## Common Operations

```python
numbers = {10, 20, 30}

numbers.add(40)          # Add
numbers.remove(20)       # Remove
numbers.discard(50)      # Remove safely
numbers.pop()            # Remove arbitrary element

print(20 in numbers)     # Membership
```

## Set Operations

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b    # Union
a & b    # Intersection
a - b    # Difference
a ^ b    # Symmetric difference
```

| Operation | Meaning |
|---|---|
| `a \| b` | Elements in either set |
| `a & b` | Elements common to both |
| `a - b` | Elements in `a` but not `b` |
| `a ^ b` | Elements in either set, but not both |

## Time Complexity

| Operation | Average |
|---|---:|
| Add | O(1) |
| Remove | O(1) |
| Search / Membership | O(1) |
| Union | O(n + m) |
| Intersection | O(min(n, m)) |

## Set vs List

| Feature | Set | List |
|---|---|---|
| Duplicates | No | Yes |
| Indexing | No | Yes |
| Ordering | Unordered | Ordered |
| Membership | O(1) average | O(n) |
| Mutable | Yes | Yes |
| Use case | Unique values / fast lookup | Ordered collection |

## Set vs Dictionary

| Feature | Set | Dictionary |
|---|---|---|
| Stores | Values | Key-value pairs |
| Duplicates | No | Keys no, values yes |
| Lookup | O(1) average | O(1) average |
| Example | `{1, 2, 3}` | `{"id": 10}` |

## What Can Be Stored?

Set elements must be **hashable**.

Valid:

```python
{1, "hello", (1, 2)}
```

Invalid:

```python
{[1, 2]}       # TypeError
{{"a": 1}}     # TypeError
```

Lists and dictionaries cannot be set elements because they are mutable and unhashable.

## Creating an Empty Set

Be careful:

```python
x = {}      # Empty dictionary
x = set()   # Empty set
```

## Common Interview Questions

**Why are sets useful for removing duplicates?**

Because a set only stores unique elements.

```python
numbers = [1, 2, 2, 3, 3, 4]

unique = set(numbers)

print(unique)
```

**Why is set membership O(1) on average?**

Because sets use a hash table internally, allowing Python to locate an element using its hash rather than searching every element.

**Can you access a set using an index?**

No.

```python
numbers = {10, 20, 30}

numbers[0]  # TypeError
```

Use a set when you primarily need **uniqueness and fast membership testing**.