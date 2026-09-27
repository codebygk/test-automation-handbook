# List

## Definition

A **list/array** is a collection that stores multiple elements in an ordered sequence and allows access using an index.

In Python, the built-in `list` is the commonly used dynamic array-like data structure.

```python
numbers = [10, 20, 30, 40]

print(numbers[0])  # 10
print(numbers[2])  # 30
```

## Key Characteristics

- Ordered
- Index-based
- Mutable
- Allows duplicate values
- Can store different data types
- Dynamic size
- Supports slicing
- Zero-based indexing

## Common Operations

```python
numbers = [10, 20, 30]

numbers.append(40)       # Add at end
numbers.insert(1, 15)    # Add at index
numbers.remove(20)       # Remove value
numbers.pop()            # Remove last element
numbers.pop(1)           # Remove by index

numbers[0] = 100         # Update

print(len(numbers))      # Size
print(20 in numbers)     # Membership
```

## Time Complexity

| Operation             |        Average |
| --------------------- | -------------: |
| Access by index       |           O(1) |
| Update by index       |           O(1) |
| Append                | O(1) amortized |
| Insert at beginning   |           O(n) |
| Insert in middle      |           O(n) |
| Delete from beginning |           O(n) |
| Delete from middle    |           O(n) |
| Search by value       |           O(n) |
| Pop from end          |           O(1) |

## List vs Array

| Feature         | Python List         | Array                                             |
| --------------- | ------------------- | ------------------------------------------------- |
| Size            | Dynamic             | Usually fixed/dynamic depending on implementation |
| Data types      | Can be mixed        | Usually same type                                 |
| Memory          | More overhead       | More memory efficient                             |
| General purpose | Yes                 | More specialized                                  |
| Index access    | O(1)                | O(1)                                              |
| Python default  | Yes                 | No traditional built-in array                     |
| Common use      | General collections | Numeric/homogeneous data                          |

## Interview Points

- Python `list` is implemented as a **dynamic array**.
- Index access is O(1).
- Inserting/deleting at the beginning or middle is O(n) because elements may need to be shifted.
- `append()` is O(1) amortized because Python occasionally resizes the underlying array.
- Python lists can contain heterogeneous objects.
- Lists preserve insertion order.
- A list is mutable, unlike a tuple.

## Common Interview Question

**Why is accessing a list element O(1)?**

Because Python lists use a contiguous dynamic-array structure internally. The address of an element can be calculated directly from its index, so no traversal is required.

**Why is inserting at the beginning O(n)?**

Existing elements have to be shifted to make room for the new element.