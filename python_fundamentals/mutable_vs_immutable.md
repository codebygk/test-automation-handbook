# Mutable vs Immutable in Python

| Feature                          | Mutable               | Immutable                                           |
| -------------------------------- | --------------------- | --------------------------------------------------- |
| Can be changed after creation?   | Yes                   | No                                                  |
| Existing object can be modified? | Yes                   | No                                                  |
| Examples                         | `list`, `dict`, `set` | `int`, `float`, `bool`, `str`, `tuple`, `frozenset` |

## Mutable

A mutable object can be modified after it is created.

```python
numbers = [10, 20, 30]

numbers[0] = 100

print(numbers)
# [100, 20, 30]
```

The same list object is modified.

### Common Mutable Types

- `list`
- `dict`
- `set`
- `bytearray`

## Immutable

An immutable object cannot be modified after it is created.

```python
name = "John"

# name[0] = "R"
# TypeError: 'str' object does not support item assignment
```

Instead, a new object is created:

```python
name = "John"

name = "R" + name[1:]

print(name)
# Rohn
```

### Common Immutable Types

- `int`
- `float`
- `bool`
- `str`
- `tuple`
- `frozenset`
- `bytes`

## Function Example

### Mutable

```python
def add_item(items):
    items.append(4)


numbers = [1, 2, 3]

add_item(numbers)

print(numbers)
# [1, 2, 3, 4]
```

The original list changes because `list` is mutable.

### Immutable

```python
def add_one(x):
    x = x + 1


number = 10

add_one(number)

print(number)
# 10
```

The original integer does not change because `int` is immutable.

## Interview Shortcut

**Mutable - Can be modified after creation.**

**Immutable - Cannot be modified after creation; changing the value results in a new object.**