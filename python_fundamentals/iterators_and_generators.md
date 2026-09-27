# Iterators and Generators

## Iterable

An **iterable** is an object that can be iterated over.

Common iterables:

```python
list
tuple
str
dict
set
range
```

Example:

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

An iterable can provide an iterator using `iter()`:

```python
iterator = iter(numbers)
```

---

# Iterator

An **iterator** is an object that produces values **one at a time**.

An iterator implements:

```python
__iter__()
__next__()
```

Example:

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Output:

```text
10
20
30
```

When there are no more values:

```python
next(iterator)
```

raises:

```python
StopIteration
```

## `iter()` and `next()`

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))  # 10
print(next(iterator))  # 20
print(next(iterator))  # 30
```

```text
iter() -> creates/gets an iterator
next() -> gets the next value
```

## Iterable vs Iterator

| Feature | Iterable | Iterator |
|---|---|---|
| Can be iterated | Yes | Yes |
| Implements `__iter__()` | Yes | Yes |
| Implements `__next__()` | Not necessarily | Yes |
| Maintains iteration state | Not necessarily | Yes |
| Example | `list`, `tuple`, `str` | `iter(list)` |

Example:

```python
numbers = [1, 2, 3]

iterable = numbers
iterator = iter(numbers)
```

Here:

```text
numbers  -> iterable
iterator -> iterator
```

---

# How `for` Loop Uses Iterators

A `for` loop internally uses the iterator protocol.

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

Conceptually, it works like:

```python
iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
        print(number)
    except StopIteration:
        break
```

You normally don't need to write this manually.

---

# Creating a Custom Iterator

You can create an iterator by implementing `__iter__()` and `__next__()`.

```python
class Count:

    def __init__(self, max_value):
        self.current = 1
        self.max_value = max_value

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max_value:
            value = self.current
            self.current += 1
            return value

        raise StopIteration


counter = Count(3)

for number in counter:
    print(number)
```

Output:

```text
1
2
3
```

---

# Generator

A **generator is a special type of iterator**.

Generators are usually created using the `yield` keyword.

```python
def count():
    yield 1
    yield 2
    yield 3
```

Use it:

```python
numbers = count()

print(next(numbers))
print(next(numbers))
print(next(numbers))
```

Output:

```text
1
2
3
```

After all values are consumed:

```python
next(numbers)
```

raises:

```python
StopIteration
```

---

# `yield`

`yield` returns a value while **pausing the function's execution**.

```python
def numbers():
    print("First")
    yield 1

    print("Second")
    yield 2

    print("Third")
    yield 3
```

```python
gen = numbers()

print(next(gen))
print(next(gen))
print(next(gen))
```

Output:

```text
First
1
Second
2
Third
3
```

The function resumes from where it previously paused.

This is different from `return`, which terminates the function.

---

# Generator vs Normal Function

### Normal function

```python
def numbers():
    return [1, 2, 3]
```

The entire list is created and returned.

### Generator

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

Values are produced **one at a time**.

This is called **lazy evaluation**.

---

# Generator with a Loop

```python
def count(max_value):
    for i in range(1, max_value + 1):
        yield i


for number in count(5):
    print(number)
```

Output:

```text
1
2
3
4
5
```

---

# Generator vs Custom Iterator

The custom iterator:

```python
class Count:

    def __init__(self, max_value):
        self.current = 1
        self.max_value = max_value

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max_value:
            value = self.current
            self.current += 1
            return value

        raise StopIteration
```

Can be simplified using a generator:

```python
def count(max_value):
    for i in range(1, max_value + 1):
        yield i
```

The generator automatically handles the iterator protocol.

---

# Generator Expression

A generator expression is similar to a list comprehension but produces values lazily.

### List comprehension

```python
numbers = [x * 2 for x in range(5)]
```

All values are stored in memory.

### Generator expression

```python
numbers = (x * 2 for x in range(5))
```

Values are generated one at a time.

```python
print(next(numbers))
print(next(numbers))
```

Output:

```text
0
2
```

---

# Memory Efficiency

Generators are useful when dealing with large amounts of data.

Instead of:

```python
numbers = [x * 2 for x in range(10000000)]
```

which creates a large list in memory, you can use:

```python
numbers = (x * 2 for x in range(10000000))
```

Values are generated only when needed.

This makes generators useful for:

- Large files
- Large datasets
- Database results
- Data pipelines
- Streams
- Infinite sequences

Example:

```python
with open("large_file.txt") as file:
    for line in file:
        process(line)
```

The file can be processed one line at a time instead of loading the entire file into memory.

---

# Iterator vs Generator

| Feature | Iterator | Generator |
|---|---|---|
| Definition | Object implementing iterator protocol | Special type of iterator |
| `__iter__()` | Yes | Automatically provided |
| `__next__()` | Yes | Automatically provided |
| `yield` | Not required | Usually uses `yield` |
| Implementation | Can require more code | Usually simpler |
| Lazy evaluation | Yes | Yes |
| Memory efficient | Yes | Yes |
| Common use | Custom iteration behavior | Lazy data generation |

The key relationship:

```text
Every generator is an iterator.
Not every iterator is a generator.
```

---

# Iterator Can Be Exhausted

```python
numbers = [1, 2, 3]

iterator = iter(numbers)

print(list(iterator))
print(list(iterator))
```

Output:

```python
[1, 2, 3]
[]
```

Once an iterator is exhausted, it cannot automatically restart.

Create a new iterator:

```python
iterator = iter(numbers)
```

The same applies to generators:

```python
gen = (x for x in range(3))

print(list(gen))
print(list(gen))
```

Output:

```python
[0, 1, 2]
[]
```

---

# Infinite Generators

Generators can produce an unlimited number of values.

```python
def counter():
    number = 1

    while True:
        yield number
        number += 1
```

Use only the values you need:

```python
gen = counter()

print(next(gen))
print(next(gen))
print(next(gen))
```

Output:

```text
1
2
3
```

This would not be practical with a normal list because an infinite list cannot be fully created.

---

# Common Interview Questions

### 1. What is an iterator?

**Short answer:**  
An iterator is an object that produces values one at a time using `__iter__()` and `__next__()`.

### 2. What is an iterable?

**Short answer:**  
An iterable is an object that can be iterated over and can provide an iterator through `iter()`.

### 3. What is the difference between an iterable and an iterator?

**Short answer:**  
An iterable can provide an iterator, while an iterator maintains the current iteration state and produces the next value using `next()`.

### 4. What does `iter()` do?

**Short answer:**  
`iter()` returns an iterator for an iterable.

### 5. What does `next()` do?

**Short answer:**  
`next()` returns the next value from an iterator and raises `StopIteration` when there are no more values.

### 6. What is `StopIteration`?

**Short answer:**  
`StopIteration` indicates that an iterator has no more values to produce.

### 7. Is a list an iterator?

**Short answer:**  
No. A list is an iterable, but it is not an iterator.

```python
numbers = [1, 2, 3]

iterator = iter(numbers)
```

### 8. What is a generator?

**Short answer:**  
A generator is a special type of iterator that produces values lazily, usually using `yield`.

### 9. What is the difference between `return` and `yield`?

**Short answer:**  
`return` terminates a function and returns a value, while `yield` pauses the function and produces a value that can be resumed later.

### 10. Why are generators memory efficient?

**Short answer:**  
Generators produce values one at a time instead of storing all values in memory.

### 11. Can a generator be reused?

**Short answer:**  
No. Once a generator is exhausted, you need to create a new generator.

### 12. What is a generator expression?

**Short answer:**  
A generator expression is a lazy expression similar to a list comprehension but produces values one at a time.

```python
gen = (x * 2 for x in range(5))
```

### 13. What is the relationship between iterators and generators?

**Short answer:**  
A generator is a special type of iterator, but an iterator does not have to be a generator.

### 14. Why would you use a generator instead of a list?

**Short answer:**  
Use a generator when you want lazy evaluation and lower memory usage, especially for large or streaming data.

# Interview Shortcut

```text
Iterable  -> can be iterated
Iterator  -> produces one value at a time
iter()    -> gets an iterator
next()    -> gets the next value
StopIteration -> no more values
Generator -> special type of iterator
yield     -> produces a value and pauses execution
Generator expression -> lazy comprehension
```