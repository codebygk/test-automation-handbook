# `==` vs `is`

| Operator | Checks | Meaning |
|---|---|---|
| `==` | Value | Do both objects have the same value? |
| `is` | Identity | Are both variables referring to the exact same object? |

## `==` - Value Comparison

Checks whether two objects have equal values.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
# True
```

`a` and `b` contain the same values, so `==` returns `True`.

However, they are two different list objects.

## `is` - Identity Comparison

Checks whether two variables refer to the **same object in memory**.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)
# False
```

Although the values are the same, `a` and `b` refer to different list objects.

### Same Object

```python
a = [1, 2, 3]
b = a

print(a == b)
# True

print(a is b)
# True
```

Here, both variables refer to the exact same object.

## Important Example

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)
# [1, 2, 3, 4]

print(b)
# [1, 2, 3, 4]
```

Because `a is b` is `True`, modifying the object through `b` also affects `a`.

## `is` with `None`

Use `is` when checking for `None`.

```python
value = None

if value is None:
    print("No value")
```

Prefer:

```python
if value is None:
    ...
```

Instead of:

```python
if value == None:
    ...
```

## Common Interview Trap

Do not rely on `is` for comparing values.

```python
a = [10, 20]
b = [10, 20]

a == b    # True
a is b    # False
```

### Quick Memory Trick

```text
==  - Same VALUE?
is  - Same OBJECT?
```