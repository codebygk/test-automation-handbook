# List, Dictionary and Set Comprehensions

Comprehensions provide a concise way to create lists, dictionaries and sets from existing iterables.

## 1. List Comprehension

List comprehension creates a new list by applying an expression to each element of an iterable.

**Syntax:**

```python
[expression for item in iterable if condition]
```

### Basic Example

Without comprehension:

```python
squares = []

for i in range(1, 6):
    squares.append(i ** 2)

print(squares)
# [1, 4, 9, 16, 25]
```

With comprehension:

```python
squares = [i ** 2 for i in range(1, 6)]

print(squares)
# [1, 4, 9, 16, 25]
```

### List Comprehension with a Condition

```python
numbers = [1, 2, 3, 4, 5, 6]

evens = [n for n in numbers if n % 2 == 0]

print(evens)
# [2, 4, 6]
```

### List Comprehension with if-else

```python
numbers = [1, 2, 3, 4, 5]

result = ["Even" if n % 2 == 0 else "Odd" for n in numbers]

print(result)
# ['Odd', 'Even', 'Odd', 'Even', 'Odd']
```

**Important:** When using `if-else` to choose an expression, it appears before the `for` clause. When filtering elements, `if` appears after the `for` clause.

### Nested List Comprehension

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [num for row in matrix for num in row]

print(flattened)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## 2. Dictionary Comprehension

Dictionary comprehension creates a dictionary using key-value pairs.

**Syntax:**

```python
{key_expression: value_expression for item in iterable if condition}
```

### Basic Example

```python
squares = {n: n ** 2 for n in range(1, 6)}

print(squares)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Dictionary Comprehension with a Condition

```python
numbers = [1, 2, 3, 4, 5, 6]

evens = {n: n ** 2 for n in numbers if n % 2 == 0}

print(evens)
# {2: 4, 4: 16, 6: 36}
```

### Swapping Dictionary Keys and Values

```python
original = {"a": 1, "b": 2, "c": 3}

swapped = {value: key for key, value in original.items()}

print(swapped)
# {1: 'a', 2: 'b', 3: 'c'}
```

This works without losing entries when the original values are unique and hashable.

### Dictionary Comprehension with if-else

```python
numbers = [1, 2, 3, 4, 5]

result = {
    n: "Even" if n % 2 == 0 else "Odd"
    for n in numbers
}

print(result)
# {1: 'Odd', 2: 'Even', 3: 'Odd', 4: 'Even', 5: 'Odd'}
```

## 3. Set Comprehension

Set comprehension creates a set containing unique elements.

**Syntax:**

```python
{expression for item in iterable if condition}
```

### Basic Example

```python
numbers = [1, 2, 2, 3, 3, 4, 5]

unique = {n for n in numbers}

print(sorted(unique))
# [1, 2, 3, 4, 5]
```

Sets automatically eliminate duplicate values.

### Set Comprehension with a Condition

```python
numbers = [1, 2, 3, 4, 5, 6]

evens = {n for n in numbers if n % 2 == 0}

print(sorted(evens))
# [2, 4, 6]
```

### Set Comprehension with String Operations

```python
words = ["Python", "Java", "python", "JAVA", "Go"]

unique = {word.lower() for word in words}

print(sorted(unique))
# ['go', 'java', 'python']
```

## 4. Nested Comprehensions

Nested comprehensions are useful when working with multiple iterables.

### Generate All Combinations

```python
combinations = [
    (x, y)
    for x in [1, 2]
    for y in [3, 4]
]

print(combinations)
# [(1, 3), (1, 4), (2, 3), (2, 4)]
```

Equivalent to:

```python
combinations = []

for x in [1, 2]:
    for y in [3, 4]:
        combinations.append((x, y))
```

### Flatten a Matrix

```python
matrix = [[1, 2], [3, 4], [5, 6]]

flattened = [n for row in matrix for n in row]

print(flattened)
# [1, 2, 3, 4, 5, 6]
```

## 5. Generator Expressions

Generator expressions look similar to list comprehensions but use parentheses.

```python
squares = (n ** 2 for n in range(1, 6))

print(list(squares))
# [1, 4, 9, 16, 25]
```

Unlike list comprehensions, generator expressions produce values lazily instead of creating the entire list immediately.

```python
total = sum(n ** 2 for n in range(1000000))
```

This avoids creating an intermediate list.

## 6. Comparison

| Feature     | List                | Dictionary                | Set                       | Generator                  |
| ----------- | ------------------- | ------------------------- | ------------------------- | -------------------------- |
| Syntax      | `[]`                | `{key: value}`            | `{}`                      | `()`                       |
| Result      | List                | Dictionary                | Set                       | Generator                  |
| Duplicates  | Allowed             | Keys unique               | Not allowed               | Allowed                    |
| Ordering    | Preserved           | Insertion order           | Not guaranteed            | Iteration order            |
| Evaluation  | Eager               | Eager                     | Eager                     | Lazy                       |
| Primary use | Transform sequences | Create key-value mappings | Create unique collections | Memory-efficient iteration |

## 7. Common Interview Questions

### Q1. What is the difference between list comprehension and generator expression?

```python
numbers = [n ** 2 for n in range(10)]

generator = (n ** 2 for n in range(10))
```

- List comprehension creates the complete list immediately.
- Generator expression produces values lazily.
- Generator expressions are useful for large datasets when values can be processed sequentially.

### Q2. Can comprehensions contain multiple conditions?

Yes.

```python
numbers = range(1, 21)

result = [
    n for n in numbers
    if n % 2 == 0
    if n % 3 == 0
]

print(result)
# [6, 12, 18]
```

### Q3. Can comprehensions call functions?

Yes.

```python
def square(n):
    return n ** 2


result = [square(n) for n in range(1, 6)]

print(result)
# [1, 4, 9, 16, 25]
```

### Q4. Can a dictionary comprehension have duplicate keys?

Yes, but later values overwrite earlier values for the same key.

```python
pairs = [("a", 1), ("b", 2), ("a", 3)]

result = {key: value for key, value in pairs}

print(result)
# {'a': 3, 'b': 2}
```

### Q5. Are comprehensions always better than loops?

No. Comprehensions are useful for simple transformations and filtering. Regular loops are often more readable for complex logic, multiple operations or exception handling.

## Interview Shortcut

- List comprehension - Creates a list using `[]`.
- Dictionary comprehension - Creates key-value pairs using `{key: value}`.
- Set comprehension - Creates a collection of unique elements using `{}`.
- Generator expression - Produces values lazily using `()`.
- Filtering - Place `if condition` after the `for` clause.
- Conditional expression - Place `if-else` before the `for` clause.
- Nested comprehension - Use multiple `for` clauses.
- Best practice - Prefer readability over writing excessively complex one-line expressions.