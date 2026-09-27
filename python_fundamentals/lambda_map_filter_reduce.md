# Lambda, `map()`, `filter()`, `reduce()`

These are commonly used together for **functional-style programming**.

| Feature    | Purpose                           | Returns      |
| ---------- | --------------------------------- | ------------ |
| `lambda`   | Create a small anonymous function | Function     |
| `map()`    | Transform every item              | Iterator     |
| `filter()` | Keep items matching a condition   | Iterator     |
| `reduce()` | Combine all items into one result | Single value |

## Lambda

A `lambda` is a small anonymous function.

### Normal function

```python
def add(a, b):
    return a + b
```

### Lambda

```python
add = lambda a, b: a + b

print(add(10, 20))
```

Output:

```text
30
```

Syntax:

```python
lambda arguments: expression
```

Example:

```python
square = lambda x: x * x

print(square(5))
```

Output:

```text
25
```

A lambda should generally be used for **simple one-expression functions**.

---

# `map()`

`map()` applies a function to **every item** in an iterable.

Syntax:

```python
map(function, iterable)
```

Example:

```python
numbers = [1, 2, 3, 4]

result = map(lambda x: x * 2, numbers)

print(list(result))
```

Output:

```text
[2, 4, 6, 8]
```

### With a normal function

```python
def square(x):
    return x * x

numbers = [1, 2, 3, 4]

result = map(square, numbers)

print(list(result))
```

Output:

```text
[1, 4, 9, 16]
```

### Important

`map()` returns an **iterator**, not a list.

```python
result = map(lambda x: x * 2, [1, 2, 3])

print(result)
```

To get a list:

```python
list(result)
```

---

# `filter()`

`filter()` keeps only the items for which the function returns `True`.

Syntax:

```python
filter(function, iterable)
```

Example:

```python
numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))
```

Output:

```text
[2, 4, 6]
```

Here:

```python
lambda x: x % 2 == 0
```

returns:

```text
True  -> keep the item
False -> discard the item
```

Like `map()`, `filter()` returns an **iterator**.

---

# `reduce()`

`reduce()` repeatedly applies a function to the elements and produces **one final value**.

It comes from the `functools` module.

```python
from functools import reduce
```

Example:

```python
numbers = [1, 2, 3, 4]

result = reduce(lambda a, b: a + b, numbers)

print(result)
```

Output:

```text
10
```

Conceptually:

```text
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
```

Another example:

```python
numbers = [1, 2, 3, 4]

result = reduce(lambda a, b: a * b, numbers)

print(result)
```

Output:

```text
24
```

Conceptually:

```text
1 * 2 = 2
2 * 3 = 6
6 * 4 = 24
```

---

# `map()` vs `filter()` vs `reduce()`

Given:

```python
numbers = [1, 2, 3, 4, 5]
```

### `map()`

**Transform every item**

```python
list(map(lambda x: x * 2, numbers))
```

Result:

```python
[2, 4, 6, 8, 10]
```

### `filter()`

**Select some items**

```python
list(filter(lambda x: x % 2 == 0, numbers))
```

Result:

```python
[2, 4]
```

### `reduce()`

**Combine items into one value**

```python
reduce(lambda a, b: a + b, numbers)
```

Result:

```python
15
```

---

# Combining Them

They can be chained together.

Example:

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

result = reduce(
    lambda a, b: a + b,
    map(
        lambda x: x * 2,
        filter(lambda x: x % 2 == 0, numbers)
    )
)

print(result)
```

Process:

```text
[1, 2, 3, 4, 5, 6]
        |
     filter
        |
     [2, 4, 6]
        |
      map
        |
     [4, 8, 12]
        |
     reduce
        |
       24
```

---

# Comprehension Alternative

In many cases, comprehensions are more readable.

Instead of:

```python
list(map(lambda x: x * 2, numbers))
```

Use:

```python
[x * 2 for x in numbers]
```

Instead of:

```python
list(filter(lambda x: x % 2 == 0, numbers))
```

Use:

```python
[x for x in numbers if x % 2 == 0]
```

For simple operations, comprehensions are often preferred for readability.

---

# Interview Comparison

| Operation  | Question to remember                        |
| ---------- | ------------------------------------------- |
| `lambda`   | How do I create a small anonymous function? |
| `map()`    | How do I transform every item?              |
| `filter()` | How do I select matching items?             |
| `reduce()` | How do I combine items into one value?      |

## Interview Shortcut

```text
lambda  -> function
map     -> transform
filter  -> select
reduce  -> combine
```

# Interview Questions

### 1. What is a lambda function?

**Short answer:**  
A lambda is an anonymous function used for small, simple, one-expression operations.

### 2. What is the difference between `map()` and `filter()`?

**Short answer:**  
`map()` transforms every item, while `filter()` selects only items that satisfy a condition.

### 3. What does `map()` return?

**Short answer:**  
`map()` returns an iterator containing the transformed values.

### 4. What does `filter()` return?

**Short answer:**  
`filter()` returns an iterator containing the items for which the condition evaluates to `True`.

### 5. What is `reduce()` used for?

**Short answer:**  
`reduce()` repeatedly combines elements of an iterable to produce a single final value.

### 6. Where is `reduce()` available?

**Short answer:**  
`reduce()` is available in the `functools` module.

```python
from functools import reduce
```

### 7. What is the difference between `lambda` and `def`?

**Short answer:**  
`lambda` creates a small anonymous one-expression function, while `def` creates a regular named function that can contain multiple statements.

### 8. Can `map()` work with multiple iterables?

**Short answer:**  
Yes. `map()` can accept multiple iterables, and the function receives one value from each iterable.

```python
list(map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6]))
```

Result:

```python
[5, 7, 9]
```

### 9. Can `filter()` be used without a lambda?

**Short answer:**  
Yes. You can pass any function that accepts one argument and returns a truthy or falsy value.

```python
def is_even(x):
    return x % 2 == 0

list(filter(is_even, [1, 2, 3, 4]))
```

### 10. When would you prefer a list comprehension over `map()` or `filter()`?

**Short answer:**  
When it makes the code simpler and more readable, especially for straightforward transformations or filtering.
