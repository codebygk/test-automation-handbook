# Abstraction

## Definition

Abstraction is the OOP principle of **exposing only the essential interface while hiding unnecessary implementation details**.

- Focuses on **what an object does**, not how it does it.
- Reduces complexity.
- Makes code easier to use and maintain.
- Commonly implemented using abstract classes and protocols.

## Simple Example

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using credit card")


class UPIPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using UPI")


payment = CreditCardPayment()
payment.pay(1000)
```

The user only needs to know:

```python
payment.pay(1000)
```

They do not need to know the internal payment processing logic.

## How It Works

```text
Abstract interface
        |
        v
    pay(amount)
        |
        +------> CreditCardPayment
        |
        +------> UPIPayment
```

The abstract class defines **what must be implemented**.

The child classes define **how it is implemented**.

## Abstract Classes

Python provides abstract classes through the `abc` module.

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass
```

A class containing an abstract method cannot normally be instantiated:

```python
animal = Animal()  # TypeError
```

A concrete child class must implement the abstract method:

```python
class Dog(Animal):

    def speak(self):
        print("Bark")


dog = Dog()
dog.speak()
```

## `ABC`

`ABC` stands for **Abstract Base Class**.

```python
from abc import ABC

class Animal(ABC):
    pass
```

It is used as the base class for defining abstract classes.

## `@abstractmethod`

`@abstractmethod` marks a method that subclasses are expected to implement.

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass
```

A subclass that does not implement `speak()` remains abstract.

## Abstract + Concrete Methods

An abstract class can contain both abstract and concrete methods.

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

    def sleep(self):
        print("Sleeping")


class Dog(Animal):

    def speak(self):
        print("Bark")
```

Here:

- `speak()` is abstract.
- `sleep()` is a concrete method.
- `Dog` inherits `sleep()`.
- `Dog` must implement `speak()`.

## Properties

Abstract properties are also possible.

```python
from abc import ABC, abstractmethod


class Employee(ABC):

    @property
    @abstractmethod
    def salary(self):
        pass
```

A subclass must provide the required property implementation.

## Protocols

Python also supports structural abstraction through `Protocol`.

```python
from typing import Protocol


class Drawable(Protocol):

    def draw(self):
        ...


class Circle:

    def draw(self):
        print("Drawing circle")


def render(obj: Drawable):
    obj.draw()
```

`Circle` does not explicitly inherit from `Drawable`.

It only needs to provide the required `draw()` behavior.

This is closely related to Python's **duck typing**.

## Abstract Class vs Protocol

| Feature              | Abstract Class                | Protocol                    |
| -------------------- | ----------------------------- | --------------------------- |
| Main idea            | Define explicit abstraction   | Define expected structure   |
| Inheritance          | Usually required              | Not required                |
| Runtime enforcement  | Yes, with `ABC`               | Mostly static type checking |
| Multiple inheritance | Supported                     | Supported                   |
| Best for             | Shared interface and behavior | Structural typing           |
| Module               | `abc`                         | `typing`                    |

## Abstraction vs Encapsulation

| Feature      | Abstraction                     | Encapsulation                           |
| ------------ | ------------------------------- | --------------------------------------- |
| Main goal    | Hide unnecessary implementation | Control access to internal state        |
| Focus        | What the object does            | How data is accessed                    |
| Question     | "What should I expose?"         | "How should I protect this?"            |
| Common tools | ABC, Protocol                   | Properties, methods, naming conventions |
| Example      | `payment.pay()`                 | Validating `account.balance`            |

## Abstraction vs Inheritance

| Feature      | Abstraction                      | Inheritance              |
| ------------ | -------------------------------- | ------------------------ |
| Purpose      | Define essential interface       | Reuse or extend behavior |
| Focus        | What must be provided            | What is inherited        |
| Relationship | Can use inheritance              | Is a class relationship  |
| Example      | `Animal.speak()` abstract method | `Dog(Animal)`            |

Inheritance is often used to implement abstraction, but they are not the same concept.

## Abstraction vs Polymorphism

| Feature           | Abstraction                  | Polymorphism                       |
| ----------------- | ---------------------------- | ---------------------------------- |
| Main idea         | Hide implementation details  | Same interface, different behavior |
| Focus             | Interface                    | Behavior                           |
| Example           | `Payment.pay()`              | Card payment vs UPI payment        |
| Common connection | Defines the common interface | Provides different implementations |

## Use Cases

- Payment systems
- Database interfaces
- API clients
- Browser automation frameworks
- Notification systems
- Storage providers
- Plugin architectures
- Test automation frameworks

Example:

```python
from abc import ABC, abstractmethod


class Browser(ABC):

    @abstractmethod
    def open(self, url):
        pass


class Chrome(Browser):

    def open(self, url):
        print(f"Opening {url} in Chrome")


class Firefox(Browser):

    def open(self, url):
        print(f"Opening {url} in Firefox")
```

The framework can work with:

```python
browser.open(url)
```

without depending on the internal implementation of Chrome or Firefox.

## Interview Tips

- Remember: **Abstraction = what, implementation = how**.
- `ABC` and `@abstractmethod` are the most important Python mechanisms.
- An abstract class can contain both abstract and concrete methods.
- A class with unimplemented abstract methods cannot be instantiated.
- Python also supports structural abstraction using `Protocol`.
- Do not confuse abstraction with encapsulation.
- Abstraction reduces complexity by exposing only what the consumer needs.

## Common Questions

### Q1. What is abstraction?

**Answer:** Abstraction is the process of exposing essential functionality while hiding unnecessary implementation details.

### Q2. How do you achieve abstraction?

**Answer:** In Python, abstraction can be implemented using abstract base classes with `ABC` and `@abstractmethod`, or structurally using `Protocol`.

### Q3. Can we instantiate an abstract class?

**Answer:** Not if it contains unimplemented abstract methods. Python raises a `TypeError`.

### Q4. Can an abstract class have concrete methods?

**Answer:** Yes. An abstract class can contain both abstract methods and fully implemented concrete methods.

### Q5. What is `ABC`?

**Answer:** `ABC` is the base class provided by Python's `abc` module for creating abstract base classes.

### Q6. What does `@abstractmethod` do?

**Answer:** It marks a method as abstract, requiring concrete subclasses to provide an implementation before they can be instantiated.

### Q7. What is the difference between abstraction and encapsulation?

**Answer:** Abstraction hides unnecessary implementation complexity, while encapsulation controls access to an object's internal state.

### Q8. Can an abstract class have `__init__()`?

**Answer:** Yes. An abstract class can define an initializer, and subclasses can call it using `super()`.

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):

    def speak(self):
        print(self.name, "says Bark")
```

### Q9. What happens if a subclass does not implement an abstract method?

**Answer:** The subclass remains abstract and cannot be instantiated.

### Q10. What is a Protocol?

**Answer:** A Protocol defines the expected structure or behavior of an object. A class can satisfy the protocol without explicitly inheriting from it.

## Quick Revision

| Concept           | Key Idea                             |
| ----------------- | ------------------------------------ |
| Abstraction       | Hide implementation complexity       |
| ABC               | Base class for abstract classes      |
| `@abstractmethod` | Defines required behavior            |
| Concrete class    | Implements required abstract methods |
| Protocol          | Defines expected structure           |
| Encapsulation     | Controls access to internal state    |
| Polymorphism      | Same interface, different behavior   |

## Four OOP Pillars

| Pillar        | Core Idea                          | Typical Python Mechanisms |
| ------------- | ---------------------------------- | ------------------------- |
| Encapsulation | Control internal state             | Properties, methods       |
| Inheritance   | Reuse and extend behavior          | Parent/child classes      |
| Polymorphism  | Same interface, different behavior | Overriding, duck typing   |
| Abstraction   | Hide implementation complexity     | ABC, Protocol             |

## One-Line Answer

> **Abstraction exposes what an object can do while hiding the unnecessary details of how it does it.**