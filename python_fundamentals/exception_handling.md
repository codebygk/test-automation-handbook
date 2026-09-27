# Exception Handling in Python

Exception handling allows a program to handle runtime errors gracefully without terminating unexpectedly.

Python provides `try`, `except`, `else`, `finally` and `raise` for exception handling.

## 1. Basic Exception Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Output:

```text
Cannot divide by zero
```

- `try` - Contains code that might raise an exception.
- `except` - Handles an exception.
- `else` - Executes only if no exception occurs in the `try` block.
- `finally` - Executes regardless of whether an exception occurs.
- `raise` - Explicitly raises an exception.

## 2. Complete try-except-else-finally

```python
try:
    number = int("10")
    result = 100 / number

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)

finally:
    print("Execution completed")
```

Output:

```text
Result: 10.0
Execution completed
```

### Execution Flow

| Scenario              | try      | except              | else     | finally                     |
| --------------------- | -------- | ------------------- | -------- | --------------------------- |
| No exception          | Executes | Skipped             | Executes | Executes                    |
| Exception handled     | Executes | Executes            | Skipped  | Executes                    |
| Exception not handled | Executes | No matching handler | Skipped  | Executes before propagation |
| Return inside try     | Executes | Skipped             | Skipped  | Executes before return      |

## 3. Handling Multiple Exceptions

### Separate except Blocks

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

### Multiple Exceptions in One Block

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number

except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")
```

### Generic Exception Handler

```python
try:
    result = 10 / 0

except Exception as e:
    print(type(e).__name__)
    print(e)
```

Output:

```text
ZeroDivisionError
division by zero
```

**Best practice:** Catch specific exceptions whenever possible. Avoid using a generic handler when you cannot meaningfully handle the error.

## 4. Raising Exceptions

Use `raise` to explicitly trigger an exception.

```python
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")

    if amount > balance:
        raise ValueError("Insufficient balance")

    return balance - amount


try:
    withdraw(1000, 1500)

except ValueError as e:
    print(e)
```

Output:

```text
Insufficient balance
```

## 5. Re-raising Exceptions

Use `raise` without arguments inside an exception handler to propagate the current exception.

```python
def divide(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        print("Logging the error")
        raise


divide(10, 0)
```

The exception is logged and then propagated to the caller.

## 6. Custom Exceptions

Create custom exceptions by inheriting from `Exception`.

```python
class InsufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(
            "Insufficient account balance"
        )

    return balance - amount


try:
    withdraw(1000, 2000)

except InsufficientBalanceError as e:
    print(e)
```

Output:

```text
Insufficient account balance
```

Custom exceptions make application-specific errors easier to identify and handle.

## 7. Exception Chaining

Use `raise ... from ...` to preserve the original cause of an exception.

```python
def parse_age(value):
    try:
        return int(value)

    except ValueError as e:
        raise ValueError("Invalid age provided") from e


parse_age("abc")
```

The traceback displays both the original `ValueError` and the new exception.

## 8. Common Built-in Exceptions

| Exception             | Description                                      |
| --------------------- | ------------------------------------------------ |
| `Exception`           | Base class for most application-level exceptions |
| `ValueError`          | Correct type but invalid value                   |
| `TypeError`           | Operation applied to an inappropriate type       |
| `ZeroDivisionError`   | Division by zero                                 |
| `IndexError`          | Invalid sequence index                           |
| `KeyError`            | Dictionary key not found                         |
| `AttributeError`      | Attribute does not exist                         |
| `FileNotFoundError`   | File does not exist                              |
| `ImportError`         | Import operation fails                           |
| `ModuleNotFoundError` | Module cannot be found                           |
| `NameError`           | Variable name is not defined                     |
| `RuntimeError`        | General runtime error                            |
| `TimeoutError`        | Operation times out                              |
| `AssertionError`      | Assertion fails                                  |

## 9. Important Interview Questions

### Q1. What is the difference between an error and an exception?

An exception is an event that interrupts normal program execution and can potentially be handled.

Syntax errors prevent invalid Python code from being compiled, while exceptions such as `ValueError` and `ZeroDivisionError` typically occur during execution.

### Q2. What is the difference between `except Exception` and bare `except`?

```python
except Exception:
    ...
```

Catches most application-level exceptions.

```python
except:
    ...
```

Catches all exceptions, including `KeyboardInterrupt` and `SystemExit`.

Prefer catching specific exceptions.

### Q3. Does finally execute when return is used?

Yes, under normal execution.

```python
def example():
    try:
        return 10

    finally:
        print("Finally executed")


print(example())
```

Output:

```text
Finally executed
10
```

### Q4. What happens if finally also contains return?

```python
def example():
    try:
        return 10

    finally:
        return 20


print(example())
# 20
```

The `finally` return overrides the original return.

Avoid returning from `finally` because it can suppress exceptions and override return values.

### Q5. Can we use try without except?

Yes, if it has a `finally` block.

```python
try:
    print("Executing")

finally:
    print("Cleanup")
```

### Q6. What is the difference between raise and assert?

| Feature               | `raise`                     | `assert`                      |
| --------------------- | --------------------------- | ----------------------------- |
| Purpose               | Explicitly raise exceptions | Check assumptions             |
| Exception             | Any exception               | `AssertionError`              |
| Production validation | Suitable                    | Not recommended               |
| Can be disabled       | No                          | Yes, with Python optimization |

```python
# raise
if age < 18:
    raise ValueError("Age must be at least 18")

# assert
assert result == expected, "Unexpected result"
```

Use `raise` for input validation and `assert` for debugging assumptions or test assertions.

## Interview Shortcut

- `try` - Code that might fail.
- `except` - Handle the exception.
- `else` - Execute when no exception occurs.
- `finally` - Execute cleanup code.
- `raise` - Explicitly raise an exception.
- `raise` without arguments - Re-raise the current exception.
- `raise ... from ...` - Chain exceptions.
- Custom exception - Inherit from `Exception`.
- Best practice - Catch specific exceptions, preserve tracebacks and never silently swallow unexpected errors.