# Functions and Arguments

A **function** is a reusable block of code that performs a specific task.

## Basic Function

```python
def greet():
    print("Hello")


greet()
```

### Function with a Parameter

A **parameter** is a variable defined in the function declaration.

```python
def greet(name):
    print(f"Hello, {name}")


greet("John")
```

Here:

- `name` → parameter
- `"John"` → argument

## Parameter vs Argument

| Term | Meaning | Example |
|---|---|---|
| Parameter | Variable defined in function definition | `def greet(name):` |
| Argument | Actual value passed to the function | `greet("John")` |

```python
def add(a, b):       # a and b are parameters
    return a + b


result = add(10, 20) # 10 and 20 are arguments
```

## Types of Arguments

### 1. Positional Arguments

Arguments are matched based on their position.

```python
def greet(name, age):
    print(name, age)


greet("John", 25)
```

```text
name → "John"
age  → 25
```

### 2. Keyword Arguments

Arguments are passed using parameter names.

```python
def greet(name, age):
    print(name, age)


greet(age=25, name="John")
```

The order does not matter.

### 3. Default Arguments

A parameter can have a default value.

```python
def greet(name, message="Hello"):
    print(message, name)


greet("John")
# Hello John

greet("John", "Hi")
# Hi John
```

If the argument is not provided, the default value is used.

### 4. Variable-Length Positional Arguments — `*args`

`*args` allows a function to accept any number of positional arguments.

```python
def add(*numbers):
    return sum(numbers)


print(add(10, 20))
# 30

print(add(10, 20, 30, 40))
# 100
```

Inside the function, `args` is a tuple.

```python
def show(*args):
    print(type(args))


show(1, 2, 3)
# <class 'tuple'>
```

### 5. Variable-Length Keyword Arguments — `**kwargs`

`**kwargs` allows a function to accept any number of keyword arguments.

```python
def show(**details):
    print(details)


show(name="John", age=25)
# {'name': 'John', 'age': 25}
```

Inside the function, `kwargs` is a dictionary.

```python
def show(**kwargs):
    print(type(kwargs))


show(name="John")
# <class 'dict'>
```

## Combining Arguments

A function can use different types of parameters.

```python
def example(a, b=10, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


example(1, 2, 3, 4, x=100, y=200)
```

Output:

```text
1
2
(3, 4)
{'x': 100, 'y': 200}
```

## Keyword-Only Arguments

Parameters after `*` must be passed as keyword arguments.

```python
def create_user(name, *, age, city):
    print(name, age, city)


create_user("John", age=25, city="Chennai")
```

This is invalid:

```python
create_user("John", 25, "Chennai")
# TypeError
```

## Positional-Only Arguments

Parameters before `/` must be passed positionally.

```python
def add(a, b, /):
    return a + b


add(10, 20)
# 30
```

This is invalid:

```python
add(a=10, b=20)
# TypeError
```

## Return Value

A function can return a value using `return`.

```python
def add(a, b):
    return a + b


result = add(10, 20)

print(result)
# 30
```

If a function doesn't explicitly return anything, it returns `None`.

```python
def greet():
    print("Hello")


result = greet()

print(result)
# None
```

## Important Interview Point: Python Uses Pass-by-Object-Reference

Python arguments are passed as **object references**.

With mutable objects:

```python
def add_item(items):
    items.append(4)


numbers = [1, 2, 3]

add_item(numbers)

print(numbers)
# [1, 2, 3, 4]
```

With immutable objects:

```python
def increment(x):
    x += 1


number = 10

increment(number)

print(number)
# 10
```

The function receives a reference to the object, but reassignment does not change the caller's variable.

## Quick Comparison

| Concept | Example | Meaning |
|---|---|---|
| Function | `def add():` | Reusable block of code |
| Parameter | `def add(a):` | Variable in function definition |
| Argument | `add(10)` | Value passed to function |
| Positional | `add(10, 20)` | Matched by position |
| Keyword | `add(a=10)` | Matched by name |
| Default | `def add(a=10)` | Uses default if omitted |
| `*args` | `def add(*args)` | Multiple positional arguments |
| `**kwargs` | `def add(**kwargs)` | Multiple keyword arguments |
| `return` | `return result` | Sends value back to caller |
| Keyword-only | `def f(*, x)` | Must use keyword |
| Positional-only | `def f(x, /)` | Must use position |

## Interview Shortcut

```text
Parameter - Defined in function
Argument  - Passed to function

*args     - Multiple positional arguments - tuple
**kwargs  - Multiple keyword arguments   - dict

==        - Value comparison
is        - Identity comparison
```