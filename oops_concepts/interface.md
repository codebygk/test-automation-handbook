# Interfaces

## Definition

An **interface** defines a contract that specifies **what a class must provide**, without requiring a specific implementation.

Python does not have a traditional `interface` keyword like Java or C#.

In Python, interfaces are commonly implemented using:

- `abc.ABC` + `@abstractmethod`
- `typing.Protocol`
- Duck typing

---

## Syntax

### Using ABC

```python
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

A concrete class must implement the abstract method:

```python
class UPI(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using UPI")
```

```python
payment = UPI()
payment.pay(1000)
```

---

## Protocol

`Protocol` provides **structural typing**.

```python
from typing import Protocol

class Payment(Protocol):

    def pay(self, amount):
        ...
```

Any class having the required method can satisfy the protocol:

```python
class UPI:

    def pay(self, amount):
        print("Paid using UPI")


def process_payment(payment: Payment):
    payment.pay(1000)
```

No inheritance is required:

```python
upi = UPI()
process_payment(upi)
```

---

## ABC vs Protocol

| Feature | ABC | Protocol |
|---|---|---|
| Explicit inheritance | Usually required | Not required |
| Enforcement at runtime | Yes | Mostly type-checking |
| Structural typing | No | Yes |
| Nominal typing | Yes | No |
| Best for | Strict contracts | Flexible interfaces |
| Python style | Explicit | Duck typing friendly |

---

## Interface vs Abstract Class

| Interface | Abstract Class |
|---|---|
| Primarily defines a contract | Defines contract + shared behavior |
| Usually contains abstract methods | Can contain abstract and concrete methods |
| Focuses on what must be implemented | Can provide common implementation |
| Multiple interfaces are commonly supported | Multiple inheritance is possible in Python |
| Example: `Payment` contract | Example: `BaseTest` with common setup |

In Python, `ABC` can effectively serve as an interface when it contains only abstract members.

---

## Interface Example

```python
from abc import ABC, abstractmethod

class Browser(ABC):

    @abstractmethod
    def open(self, url):
        pass

    @abstractmethod
    def close(self):
        pass
```

Implementations:

```python
class Chrome(Browser):

    def open(self, url):
        print(f"Opening {url} in Chrome")

    def close(self):
        print("Closing Chrome")


class Firefox(Browser):

    def open(self, url):
        print(f"Opening {url} in Firefox")

    def close(self):
        print("Closing Firefox")
```

The client code depends on the interface:

```python
def run_test(browser: Browser):
    browser.open("https://example.com")
    browser.close()
```

This allows different implementations to be used without changing the client.

---

## Multiple Interfaces

Python supports multiple inheritance, so a class can implement multiple ABC-based interfaces.

```python
from abc import ABC, abstractmethod

class Printable(ABC):

    @abstractmethod
    def print_document(self):
        pass


class Scannable(ABC):

    @abstractmethod
    def scan(self):
        pass


class Printer(Printable, Scannable):

    def print_document(self):
        print("Printing")

    def scan(self):
        print("Scanning")
```

---

## Duck Typing

Python often does not require an explicit interface at all.

```python
class Dog:

    def speak(self):
        print("Bark")


class Cat:

    def speak(self):
        print("Meow")


def make_speak(animal):
    animal.speak()
```

Both work because they provide the expected behavior:

```python
make_speak(Dog())
make_speak(Cat())
```

This is the essence of:

> "If it behaves like the required object, use it."

---

## Why Use Interfaces?

- Reduce coupling
- Define clear contracts
- Enable multiple implementations
- Improve testability
- Support dependency inversion
- Make code easier to extend
- Allow client code to depend on abstractions instead of concrete classes

---

## Interface in Test Automation

A common automation example:

```python
from abc import ABC, abstractmethod

class BrowserDriver(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def navigate(self, url):
        pass

    @abstractmethod
    def close(self):
        pass
```

Different implementations:

```python
class SeleniumDriver(BrowserDriver):

    def start(self):
        print("Starting Selenium")

    def navigate(self, url):
        print(f"Selenium navigating to {url}")

    def close(self):
        print("Closing Selenium")


class PlaywrightDriver(BrowserDriver):

    def start(self):
        print("Starting Playwright")

    def navigate(self, url):
        print(f"Playwright navigating to {url}")

    def close(self):
        print("Closing Playwright")
```

The test framework can depend on `BrowserDriver` instead of Selenium or Playwright directly.

---

## Interface vs Duck Typing

| Interface | Duck Typing |
|---|---|
| Explicit contract | Implicit contract |
| Uses ABC/Protocol | Relies on behavior |
| More structured | More flexible |
| Better for large systems with explicit boundaries | Very Pythonic |
| Can provide stronger tooling/contracts | Less formal |
| Client knows expected interface | Client simply calls required methods |

---

## Important Interview Points

- Python has **no built-in `interface` keyword**.
- `ABC` and `@abstractmethod` are commonly used to create explicit interfaces.
- `Protocol` provides structural typing.
- Duck typing is Python's natural approach to interfaces.
- An abstract class can contain both abstract and concrete methods.
- A class containing abstract methods cannot normally be instantiated.
- A subclass must implement required abstract methods before it can be instantiated.
- Interfaces help achieve loose coupling.
- Programming against an interface rather than a concrete implementation supports the **Dependency Inversion Principle**.

---

## Common Interview Questions

### What is an interface?

An interface defines a contract that specifies what operations a class must provide, without prescribing the implementation.

### Does Python support interfaces?

Python does not have a dedicated `interface` keyword. Interfaces can be implemented using `ABC`, `@abstractmethod`, `Protocol`, or duck typing.

### How do you create an interface in Python?

Using an abstract base class:

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass
```

### What is the difference between ABC and Protocol?

`ABC` generally uses explicit inheritance and provides runtime enforcement of abstract methods. `Protocol` uses structural typing, so a class can satisfy the interface without inheriting from it.

### Can an abstract class have concrete methods?

Yes.

```python
class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

    def sleep(self):
        print("Sleeping")
```

### Can Python implement multiple interfaces?

Yes. Python supports multiple inheritance, so a class can inherit from multiple ABCs or implement multiple protocols.

### What is duck typing?

Duck typing means Python focuses on whether an object supports the required behavior rather than checking its exact type.

### Why use an interface?

To reduce coupling, define clear contracts, support multiple implementations, improve testability, and make systems easier to extend.

---

## Quick Revision

| Concept | Meaning |
|---|---|
| Interface | Defines a contract |
| ABC | Explicit abstraction mechanism |
| `@abstractmethod` | Requires subclasses to implement a method |
| Protocol | Structural interface |
| Duck typing | Behavior-based interface |
| Concrete class | Provides actual implementation |
| Loose coupling | Depend on abstractions rather than implementations |

## Interview Answer

> "Python does not have a traditional interface keyword. We can define interfaces using ABC and abstract methods when we want an explicit contract, or Protocol when we want structural typing. Python also naturally supports interfaces through duck typing. The main purpose is to define expected behavior and reduce coupling between components."