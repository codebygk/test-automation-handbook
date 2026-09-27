# Polymorphism

## Definition

Polymorphism means **one interface or method name can represent different behaviors depending on the object or arguments**.

The two important interview concepts are:

- **Method overriding** - same method, different implementation in a child class.
- **Method overloading** - same method name, different parameter combinations.

## Types

| Type                 | Meaning                                            | Python Support  |
| -------------------- | -------------------------------------------------- | --------------- |
| Method overriding    | Child changes parent method behavior               | Yes             |
| Method overloading   | Same method name with different parameters         | Not traditional |
| Operator overloading | Operators behave differently for different objects | Yes             |
| Duck typing          | Behavior is determined by supported operations     | Yes             |

# Method Overriding

## Definition

Method overriding occurs when a **child class provides its own implementation of a method already defined in the parent class**.

It is the most common example of runtime polymorphism.

## Example

```python
class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    def speak(self):
        print("Bark")


class Cat(Animal):
    def speak(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
```

Output:

```text
Bark
Meow
```

The same method call:

```python
animal.speak()
```

produces different behavior depending on the actual object.

## `super()`

A child can extend the parent's implementation instead of completely replacing it.

```python
class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    def speak(self):
        super().speak()
        print("Bark")
```

Output:

```text
Animal sound
Bark
```

## Key Points

- Requires inheritance.
- Child provides a different implementation.
- Method signature is generally kept compatible.
- Supports runtime polymorphism.
- `super()` can be used to reuse parent behavior.

# Method Overloading

## Definition

Method overloading means having **multiple methods with the same name but different parameter lists**.

Traditional method overloading is common in languages such as Java and C++.

Python does **not** support traditional method overloading.

This will NOT create overloaded methods:

```python
class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c
```

The second `add()` replaces the first one.

## Python Alternatives

### Default Arguments

```python
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c


calc = Calculator()

print(calc.add(10, 20))
print(calc.add(10, 20, 30))
```

### `*args`

```python
class Calculator:
    def add(self, *args):
        return sum(args)


calc = Calculator()

print(calc.add(10, 20))
print(calc.add(10, 20, 30))
print(calc.add(10, 20, 30, 40))
```

### `functools.singledispatch`

Python can also dispatch a function based on the type of its first argument.

```python
from functools import singledispatch


@singledispatch
def process(value):
    print("Generic")


@process.register
def _(value: int):
    print("Integer")


@process.register
def _(value: str):
    print("String")
```

This is useful for type-based dispatch, but it is not traditional method overloading.

# Overloading vs Overriding

| Feature                    | Overloading                            | Overriding                               |
| -------------------------- | -------------------------------------- | ---------------------------------------- |
| Meaning                    | Same method name, different parameters | Child redefines parent method            |
| Inheritance required       | No                                     | Yes                                      |
| Purpose                    | Handle different argument combinations | Change inherited behavior                |
| Traditional Python support | No                                     | Yes                                      |
| Common technique           | Default args, `*args`                  | Child method                             |
| Polymorphism               | Compile-time concept in some languages | Runtime polymorphism                     |
| Example                    | `add(a, b)` / `add(a, b, c)`           | `Dog.speak()` replacing `Animal.speak()` |

# Duck Typing

Python also supports polymorphism through duck typing.

```python
class Dog:
    def speak(self):
        print("Bark")


class Robot:
    def speak(self):
        print("Beep")


def make_sound(obj):
    obj.speak()


make_sound(Dog())
make_sound(Robot())
```

`Dog` and `Robot` do not need to inherit from the same class.

The important thing is that both provide `speak()`.

> If an object supports the required behavior, Python can use it.

# Operator Overloading

Operators can behave differently depending on the operands.

```python
print(10 + 20)          # 30
print("Hello " + "GK")  # Hello GK
print([1, 2] + [3, 4])  # [1, 2, 3, 4]
```

User-defined classes can customize operators using special methods.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )
```

# How Polymorphism Works

```python
class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("Bark")


class Cat(Animal):
    def speak(self):
        print("Meow")


def make_sound(animal):
    animal.speak()


make_sound(Dog())
make_sound(Cat())
```

At runtime:

```text
make_sound(Dog())
        |
        v
Dog.speak()
        |
       Bark


make_sound(Cat())
        |
        v
Cat.speak()
        |
       Meow
```

The actual object's implementation determines the behavior.

# Related Concepts

| Concept       | Key Idea                                        |
| ------------- | ----------------------------------------------- |
| Inheritance   | Child reuses or extends parent behavior         |
| Overriding    | Child changes inherited method behavior         |
| Overloading   | Same operation handles different parameters     |
| Duck typing   | Behavior matters more than explicit type        |
| Abstraction   | Expose essential interface, hide implementation |
| Encapsulation | Control access to internal state                |

# Use Cases

- Multiple implementations of the same interface.
- Browser automation frameworks.
- API clients for different services.
- Payment providers.
- Database implementations.
- Plugin architectures.
- Test automation frameworks.
- Extensible application designs.

Example:

```python
class ChromeDriver:
    def click(self):
        print("Chrome click")


class FirefoxDriver:
    def click(self):
        print("Firefox click")


def perform_click(driver):
    driver.click()


perform_click(ChromeDriver())
perform_click(FirefoxDriver())
```

The caller does not need to know the concrete driver type.

# Interview Tips

- **Overriding = inheritance + same method + different implementation.**
- **Overloading = same method name + different parameters.**
- Python supports method overriding.
- Python does not support traditional method overloading.
- Default arguments and `*args` can achieve similar behavior.
- Duck typing is an important form of Python polymorphism.
- Operator overloading uses special methods such as `__add__()`.
- Do not say that method overloading and overriding are the same.
- Be prepared to explain why the second method definition replaces the first in Python.

# Common Questions

### Q1. What is polymorphism?

**Answer:** Polymorphism allows the same interface or operation to produce different behavior depending on the object or input.

### Q2. What is method overriding?

**Answer:** Method overriding occurs when a child class provides its own implementation of a method inherited from its parent class.

### Q3. What is method overloading?

**Answer:** Method overloading means defining the same method name with different parameter lists. Python does not support traditional method overloading.

### Q4. How can Python achieve overloading-like behavior?

**Answer:** Python can use default arguments, `*args`, `**kwargs`, or techniques such as `functools.singledispatch`.

### Q5. What happens if you define the same method twice in Python?

**Answer:** The later definition replaces the earlier definition in the class namespace.

### Q6. What is the difference between overloading and overriding?

**Answer:** Overloading handles different parameter combinations with the same method name, while overriding allows a child class to change the implementation of an inherited method.

### Q7. Does method overriding require inheritance?

**Answer:** Yes. Overriding specifically refers to redefining inherited behavior in a child class.

### Q8. Does method overloading require inheritance?

**Answer:** No. Traditional method overloading is based on having multiple method signatures, not inheritance.

### Q9. Is duck typing polymorphism?

**Answer:** Yes. Duck typing enables polymorphic behavior based on whether an object supports the required operations rather than its inheritance hierarchy.

### Q10. What is runtime polymorphism?

**Answer:** Runtime polymorphism occurs when the implementation executed is determined at runtime based on the actual object, commonly through method overriding.


# One-Line Answers

- **Polymorphism:** Same interface, different behavior.
- **Overriding:** Child class changes inherited method behavior.
- **Overloading:** Same method name with different parameter combinations.
- **Duck typing:** Object compatibility is based on supported behavior.
- **Operator overloading:** Customizing operators using special methods.