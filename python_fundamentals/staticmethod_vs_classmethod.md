# `@staticmethod` vs `@classmethod`

Both are methods that can be called using the **class itself**, but they differ in what they receive automatically.

| Feature                | `@staticmethod`       | `@classmethod`                                  |
| ---------------------- | --------------------- | ----------------------------------------------- |
| First parameter        | None                  | `cls`                                           |
| Access instance data   | No                    | No                                              |
| Access class data      | Not directly          | Yes                                             |
| Can modify class state | Not directly          | Yes                                             |
| Called using class     | Yes                   | Yes                                             |
| Called using instance  | Yes                   | Yes                                             |
| Typical use            | Utility/helper method | Alternative constructor / class-level operation |

## `@staticmethod`

A static method does **not automatically receive `self` or `cls`.

```python
class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b


print(MathUtils.add(10, 20))
```

Output:

```text
30
```

It is basically a function placed inside a class because it is logically related to that class.

```python
class Validator:

    @staticmethod
    def is_valid_email(email):
        return "@" in email
```

No instance or class data is required.

## `@classmethod`

A class method automatically receives the class as `cls`.

```python
class Employee:

    company = "ABC"

    @classmethod
    def get_company(cls):
        return cls.company


print(Employee.get_company())
```

Output:

```text
ABC
```

`cls` refers to the class:

```python
Employee
```

So:

```python
cls.company
```

is equivalent to:

```python
Employee.company
```

## Class Method Can Modify Class Data

```python
class Employee:

    count = 0

    @classmethod
    def increment_count(cls):
        cls.count += 1


Employee.increment_count()
Employee.increment_count()

print(Employee.count)
```

Output:

```text
2
```

## Class Method as Alternative Constructor

This is one of the most common interview use cases.

```python
class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))


employee = Employee.from_string("John,30")

print(employee.name)
print(employee.age)
```

Output:

```text
John
30
```

Here:

```python
return cls(name, int(age))
```

creates an instance of the class.

## Important Difference

```python
class Example:

    x = 10

    @staticmethod
    def static_method():
        # No automatic access to cls
        pass

    @classmethod
    def class_method(cls):
        print(cls.x)
```

The class method can directly access class-level data:

```python
Example.class_method()
```

The static method cannot:

```python
Example.static_method()
```

unless the class is explicitly referenced.

## `self` vs `cls`

```python
class Employee:

    company = "ABC"

    def instance_method(self):
        print(self)

    @classmethod
    def class_method(cls):
        print(cls)

    @staticmethod
    def static_method():
        print("No self or cls")
```

| Method          | Automatically receives |
| --------------- | ---------------------- |
| Instance method | `self`                 |
| Class method    | `cls`                  |
| Static method   | Nothing                |

## Interview Shortcut

```text
Instance method -> works with object/instance data -> self
Class method    -> works with class data       -> cls
Static method   -> independent utility         -> no self/cls
```

### Common Interview Question

**When should you use `@staticmethod` instead of `@classmethod`?**

Use `@staticmethod` when the method does not need access to either **instance state or class state**.

Use `@classmethod` when the method needs to work with **class-level state** or when implementing an **alternative constructor**.