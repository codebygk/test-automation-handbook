# Decorators

A **decorator** is a function that modifies or extends the behavior of another function or class **without changing its original code**.

The key idea:

```text
Original function
       |
   decorator
       |
Modified/enhanced behavior
```

## Basic Example

```python
def my_decorator(func):

    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper


@my_decorator
def greet():
    print("Hello")


greet()
```

Output:

```text
Before function
Hello
After function
```

This:

```python
@my_decorator
def greet():
    print("Hello")
```

is equivalent to:

```python
def greet():
    print("Hello")

greet = my_decorator(greet)
```

The `@decorator` syntax is called **decorator syntax**.

---

# Why Use Decorators?

Decorators are useful when you want to add common behavior to multiple functions.

Common use cases:

- Logging
- Timing
- Authentication
- Authorization
- Validation
- Caching
- Retry logic
- Access control
- Performance measurement

For example:

```python
@log_execution
def create_user():
    pass


@log_execution
def delete_user():
    pass
```

The same logging behavior can be reused without modifying either function.

---

# Decorator with Arguments

A real decorator should usually support functions that accept arguments.

```python
def my_decorator(func):

    def wrapper(*args, **kwargs):
        print("Before function")

        result = func(*args, **kwargs)

        print("After function")

        return result

    return wrapper


@my_decorator
def add(a, b):
    return a + b


print(add(10, 20))
```

Output:

```text
Before function
After function
30
```

Here:

```python
*args
```

handles positional arguments, while:

```python
**kwargs
```

handles keyword arguments.

---

# `functools.wraps`

A decorator can replace the original function with the wrapper.

Without `wraps`:

```python
def decorator(func):

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
```

The function metadata such as `__name__` and `__doc__` can be lost.

Use:

```python
from functools import wraps


def decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
```

Example:

```python
@decorator
def greet():
    """Greets the user."""
    print("Hello")


print(greet.__name__)
print(greet.__doc__)
```

Output:

```text
greet
Greets the user.
```

**Interview point:** `@wraps` preserves the metadata of the original function.

---

# Decorator with Its Own Arguments

Sometimes the decorator itself needs arguments.

Example:

```python
def repeat(times):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator
```

Use:

```python
@repeat(3)
def greet():
    print("Hello")


greet()
```

Output:

```text
Hello
Hello
Hello
```

There are three levels:

```text
repeat()
    |
    v
decorator()
    |
    v
wrapper()
    |
    v
original function
```

---

# Multiple Decorators

You can apply multiple decorators to the same function.

```python
@decorator1
@decorator2
def greet():
    print("Hello")
```

This is equivalent to:

```python
greet = decorator1(decorator2(greet))
```

So the decorators are applied from **bottom to top**.

The execution flow can appear in the reverse order because the outer wrapper runs first.

---

# Decorator for Timing

A common practical example:

```python
import time
from functools import wraps


def timer(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"{func.__name__} took {end - start:.4f} seconds")

        return result

    return wrapper


@timer
def process_data():
    time.sleep(1)
    return "Done"


print(process_data())
```

The original function does not need to contain timing logic.

---

# Decorators for Classes

Decorators can also modify classes.

```python
def add_greeting(cls):

    cls.greet = lambda self: print("Hello")

    return cls


@add_greeting
class Person:
    pass


person = Person()
person.greet()
```

Output:

```text
Hello
```

---

# Built-in Decorators

Python provides several commonly used decorators.

## `@staticmethod`

```python
class Math:

    @staticmethod
    def add(a, b):
        return a + b
```

## `@classmethod`

```python
class Employee:

    @classmethod
    def create(cls):
        return cls()
```

## `@property`

```python
class Person:

    @property
    def name(self):
        return "John"
```

These are all examples of decorators provided by Python.

---

# Decorators in Test Automation

Decorators are particularly useful in test automation.

For example, logging:

```python
def log_test(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Starting: {func.__name__}")

        result = func(*args, **kwargs)

        print(f"Completed: {func.__name__}")

        return result

    return wrapper
```

```python
@log_test
def test_login():
    assert True
```

They can also be used for:

- Retry failed operations
- Screenshot capture
- Execution logging
- Performance measurement
- Test metadata
- Authentication checks
- Custom test setup

---

# Decorator vs Function

| Function | Decorator |
|---|---|
| Performs an operation | Modifies or extends another function/class |
| Called directly | Applied to another function/class |
| Usually takes data as input | Usually takes a function/class as input |
| `func()` | `@decorator` |

---

# Important Concepts

A good understanding of decorators requires knowing:

```text
Functions are objects
Functions can be passed as arguments
Functions can be returned from functions
Nested functions
Closures
*args and **kwargs
@decorator syntax
functools.wraps
```

These concepts are commonly tested together.

---

# Common Interview Questions

### 1. What is a decorator?

**Short answer:**  
A decorator is a function that modifies or extends the behavior of another function or class without changing its source code.

### 2. What does the `@` syntax mean?

**Short answer:**  
`@decorator` is syntactic sugar for passing the decorated function to the decorator.

```python
@decorator
def greet():
    pass
```

is equivalent to:

```python
def greet():
    pass

greet = decorator(greet)
```

### 3. Why are `*args` and `**kwargs` commonly used in decorators?

**Short answer:**  
They allow the wrapper to accept any combination of positional and keyword arguments.

### 4. What is a wrapper function?

**Short answer:**  
A wrapper is an inner function that adds behavior around the original function and then calls it.

### 5. Why use `functools.wraps`?

**Short answer:**  
`wraps` preserves the original function's metadata such as its name and docstring.

### 6. Can a decorator accept arguments?

**Short answer:**  
Yes. It requires an additional outer function that receives the decorator arguments.

```python
@repeat(3)
def greet():
    pass
```

### 7. Can a function have multiple decorators?

**Short answer:**  
Yes. Multiple decorators can be stacked, and they are applied from bottom to top.

### 8. Can decorators be applied to classes?

**Short answer:**  
Yes. A class decorator can modify or enhance a class.

### 9. What is a closure and how is it related to decorators?

**Short answer:**  
A closure is an inner function that remembers variables from its enclosing scope. Decorators commonly use closures to retain the original function.

### 10. What are common use cases for decorators?

**Short answer:**  
Logging, timing, authentication, authorization, caching, validation, retry logic, and monitoring.

### 11. What happens when you call a decorated function?

**Short answer:**  
You actually call the wrapper returned by the decorator, which can execute additional logic before or after calling the original function.

### 12. Are `@staticmethod`, `@classmethod`, and `@property` decorators?

**Short answer:**  
Yes. They are built-in decorators that change how methods or attributes behave.

# Interview Shortcut

```text
Decorator      -> modifies function/class behavior
@decorator     -> syntactic sugar
Wrapper        -> function around the original function
*args          -> positional arguments
**kwargs       -> keyword arguments
@wraps         -> preserves function metadata
Closure        -> remembers enclosing-scope variables
```