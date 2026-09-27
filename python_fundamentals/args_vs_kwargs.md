# `*args` and `**kwargs` in Python

`*args` and `**kwargs` allow functions to accept a variable number of arguments.

- `*args` - Accepts multiple positional arguments as a **tuple**.
- `**kwargs` - Accepts multiple keyword arguments as a **dictionary**.

## 1. `*args` - Variable-Length Positional Arguments

Use `*args` when you don't know how many positional arguments will be passed to a function.

```python
def add(*args):
    print(args)
    return sum(args)


print(add(10, 20, 30))
```

Output:

```text
(10, 20, 30)
60
```

**Key points:**
- Accepts zero or more positional arguments.
- Arguments are collected into a tuple.
- The name `args` is a convention; the `*` is what matters.

```python
def add(*numbers):
    return sum(numbers)


print(add(10, 20, 30))
# 60
```

## 2. `**kwargs` - Variable-Length Keyword Arguments

Use `**kwargs` when you don't know how many named arguments will be passed.

```python
def display_user(**kwargs):
    print(kwargs)


display_user(name="John", age=30, city="Chennai")
```

Output:

```text
{'name': 'John', 'age': 30, 'city': 'Chennai'}
```

**Key points:**
- Accepts zero or more keyword arguments.
- Arguments are collected into a dictionary.
- The name `kwargs` is a convention; the `**` is what matters.

```python
def display_user(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


display_user(name="John", age=30)
```

Output:

```text
name: John
age: 30
```

## 3. Combining `*args` and `**kwargs`

A function can accept both positional and keyword arguments.

```python
def display(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)


display(10, 20, name="John", age=30)
```

Output:

```text
Positional: (10, 20)
Keyword: {'name': 'John', 'age': 30}
```

### Parameter Order

The usual parameter order is:

```python
def function(positional, default=10, *args, **kwargs):
    pass
```

Example:

```python
def example(a, b=10, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


example(1, 2, 3, 4, name="John")
```

Output:

```text
1
2
(3, 4)
{'name': 'John'}
```

## 4. Argument Unpacking Using `*` and `**`

The same operators can also unpack collections when calling functions.

### Unpacking a List or Tuple Using `*`

```python
def add(a, b, c):
    return a + b + c


numbers = [10, 20, 30]

print(add(*numbers))
# 60
```

Equivalent to:

```python
add(10, 20, 30)
```

### Unpacking a Dictionary Using `**`

```python
def display_user(name, age):
    print(name, age)


user = {
    "name": "John",
    "age": 30
}

display_user(**user)
```

Equivalent to:

```python
display_user(name="John", age=30)
```

## 5. Practical Example - Function Wrapper

`*args` and `**kwargs` are commonly used in decorators and wrapper functions.

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print("Function called")
        return func(*args, **kwargs)

    return wrapper


@logger
def add(a, b):
    return a + b


print(add(10, 20))
```

Output:

```text
Function called
30
```

The wrapper can accept and forward arbitrary arguments without knowing the original function's parameters.

## 6. Common Interview Questions

### Q1. Are `args` and `kwargs` reserved keywords?

No. Only `*` and `**` have special meaning here.

```python
def example(*numbers, **details):
    print(numbers)
    print(details)
```

### Q2. Can we use both together?

Yes.

```python
def example(*args, **kwargs):
    pass
```

`*args` must appear before `**kwargs` in the parameter list.

### Q3. What happens if no arguments are provided?

```python
def example(*args, **kwargs):
    print(args)
    print(kwargs)


example()
```

Output:

```text
()
{}
```

### Q4. What is the difference between `*args` and `**kwargs`?

| Feature | `*args` | `**kwargs` |
|---|---|---|
| Argument type | Positional | Keyword |
| Stored as | Tuple | Dictionary |
| Syntax | Single `*` | Double `**` |
| Access | Index | Key |
| Example | `func(10, 20)` | `func(a=10, b=20)` |
| Unpacking | List or tuple | Dictionary |

## Interview Shortcut

- `*args` - Collects positional arguments into a tuple.
- `**kwargs` - Collects keyword arguments into a dictionary.
- `*list` - Unpacks positional arguments.
- `**dict` - Unpacks keyword arguments.
- Common use cases - Decorators, wrappers, forwarding arguments and flexible APIs.