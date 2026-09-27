# Dependency Inversion Principle (DIP)

## Definition

The **Dependency Inversion Principle** states:

1. High-level modules should not depend directly on low-level modules. Both should depend on abstractions.
2. Abstractions should not depend on implementation details. Implementations should depend on abstractions.

DIP is the fifth principle of **SOLID**.

### Simple idea

```text
Without DIP:

Test -> SeleniumDriver

With DIP:

Test -> Browser Interface <- SeleniumDriver
```

The high-level code depends on an abstraction rather than a concrete implementation.

---

# 1. Problem Without DIP

Suppose a Page Object directly creates a Selenium driver:

```python
class LoginPage:

    def __init__(self):
        self.driver = SeleniumDriver()

    def login(self, username, password):
        self.driver.type(
            ("id", "username"),
            username
        )

        self.driver.type(
            ("id", "password"),
            password
        )
```

### Problems

`LoginPage` is now tightly coupled to:

```text
LoginPage
    |
    +-- SeleniumDriver
```

If we want to:

- Replace Selenium with Playwright
- Mock the browser in unit tests
- Use a remote driver
- Introduce another implementation

we need to modify `LoginPage`.

---

# 2. Apply DIP

Define an abstraction:

```python
from abc import ABC, abstractmethod


class Browser(ABC):

    @abstractmethod
    def click(self, locator):
        pass

    @abstractmethod
    def type(self, locator, text):
        pass
```

Concrete implementation:

```python
class SeleniumBrowser(Browser):

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def type(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)
```

Now the Page Object depends on the abstraction:

```python
class LoginPage:

    def __init__(self, browser: Browser):
        self.browser = browser

    def login(self, username, password):
        self.browser.type(
            ("id", "username"),
            username
        )

        self.browser.type(
            ("id", "password"),
            password
        )

        self.browser.click(
            ("id", "login")
        )
```

Now:

```text
             Browser
                ^
                |
        +-------+-------+
        |               |
SeleniumBrowser   PlaywrightBrowser
        ^
        |
    LoginPage
```

The Page Object does not care which implementation is being used.

---

# 3. Dependency Injection

**Dependency Injection (DI)** is a common technique used to implement DIP.

Instead of creating the dependency inside the class:

```python
class LoginPage:

    def __init__(self):
        self.browser = SeleniumBrowser()
```

Inject it:

```python
class LoginPage:

    def __init__(self, browser):
        self.browser = browser
```

Then:

```python
browser = SeleniumBrowser(driver)

login_page = LoginPage(browser)
```

The class receives its dependency from outside.

---

# 4. Why DIP Matters in Automation

DIP is especially useful in automation frameworks because tools and infrastructure can change.

For example:

```text
                    Browser
                       |
          +------------+------------+
          |            |            |
       Selenium    Playwright    MockBrowser
          |
          |
      LoginPage
      DashboardPage
      CheckoutPage
```

The Page Objects depend on `Browser`, not Selenium directly.

This makes it easier to:

- Change automation tools
- Mock dependencies
- Unit test Page Objects
- Support multiple implementations
- Reduce framework coupling
- Isolate infrastructure changes

---

# 5. Testing with DIP

Suppose we want to test `LoginPage` without launching a real browser.

Create a fake implementation:

```python
class FakeBrowser(Browser):

    def __init__(self):
        self.actions = []

    def click(self, locator):
        self.actions.append(
            ("click", locator)
        )

    def type(self, locator, text):
        self.actions.append(
            ("type", locator, text)
        )
```

Test:

```python
browser = FakeBrowser()

login_page = LoginPage(browser)

login_page.login(
    "admin",
    "password"
)

print(browser.actions)
```

No Selenium browser is required.

This is one of the major benefits of DIP.

---

# 6. DIP in a Real Automation Framework

A good architecture might look like:

```text
Test
 |
 v
Page Object
 |
 v
Automation Interface
 |
 +----------------------+
 |                      |
 v                      v
Selenium Adapter    Playwright Adapter
 |                      |
 v                      v
Selenium API        Playwright API
```

The higher-level automation code remains independent of the underlying tool.

---

# 7. DIP vs Dependency Injection

These are not the same thing.

| DIP                                                    | Dependency Injection                    |
| ------------------------------------------------------ | --------------------------------------- |
| Design principle                                       | Implementation technique                |
| Says what the dependency relationship should look like | Describes how dependencies are supplied |
| High-level code depends on abstractions                | Dependencies are passed into objects    |
| Part of SOLID                                          | Common way to implement DIP             |

Example:

```python
class LoginPage:

    def __init__(self, browser):
        self.browser = browser
```

Passing `browser` into the constructor is **dependency injection**.

Making `browser` an abstraction rather than a concrete Selenium class helps achieve **dependency inversion**.

---

# 8. DIP vs Dependency Inversion

The word "inversion" refers to changing the traditional dependency direction.

### Traditional

```text
High-level module
       |
       v
Low-level implementation
```

Example:

```text
LoginPage
    |
    v
SeleniumBrowser
```

### Inverted

```text
          Browser Interface
             ^        ^
             |        |
      Selenium      Playwright

             ^
             |
         LoginPage
```

Both high-level and low-level modules depend on the abstraction.

---

# 9. DIP and Other SOLID Principles

DIP often works together with the other SOLID principles.

| Principle | Relationship                                           |
| --------- | ------------------------------------------------------ |
| SRP       | Keeps components focused                               |
| OCP       | Makes new implementations easier to add                |
| LSP       | Ensures implementations can substitute the abstraction |
| ISP       | Keeps abstractions small and focused                   |
| DIP       | Makes high-level code depend on abstractions           |

Together:

```text
SRP -> Focused components
ISP -> Focused interfaces
DIP -> Depend on abstractions
LSP -> Implementations remain substitutable
OCP -> Extend without unnecessary modification
```

---

# 10. Common Mistake

DIP does **not** mean:

> "Create an interface for every class."

This can create unnecessary complexity.

Bad:

```text
UserService
    |
IUserService
    |
UserServiceImpl
```

when there is only one implementation and no meaningful abstraction boundary.

Use abstractions where they provide a real architectural benefit, such as:

- Multiple implementations
- External dependencies
- Difficult-to-test infrastructure
- Replaceable technologies
- Clear architectural boundaries

---

# 11. Common Interview Questions

### What is DIP?

DIP states that high-level modules should not depend directly on low-level implementations. Both should depend on abstractions.

### How do you apply DIP in an automation framework?

I define abstractions for infrastructure such as browser operations, API clients or database access. Page Objects and test services depend on those abstractions, while Selenium, Playwright or other tools provide concrete implementations.

### Is dependency injection the same as DIP?

No. DIP is a design principle, while dependency injection is a technique commonly used to implement it.

### Why is DIP useful for automation?

It reduces coupling to automation tools and makes components easier to test, mock and replace.

### Give an example.

Instead of:

```python
class LoginPage:

    def __init__(self):
        self.browser = SeleniumBrowser()
```

I would use:

```python
class LoginPage:

    def __init__(self, browser: Browser):
        self.browser = browser
```

The Page Object depends on the `Browser` abstraction, while the actual Selenium implementation is injected from outside.

### Does DIP always require an abstract class?

No.

Python can use:

- Abstract base classes
- `Protocol`
- Duck typing
- Other abstraction mechanisms

For example:

```python
from typing import Protocol


class Browser(Protocol):

    def click(self, locator):
        ...

    def type(self, locator, text):
        ...
```

A class can satisfy the protocol without explicitly inheriting from it.

---

# Interview Answer

> "The Dependency Inversion Principle says that high-level modules should not depend directly on low-level implementations. Both should depend on abstractions. In an automation framework, instead of making a Page Object directly create or depend on Selenium, I would define a Browser abstraction and inject the concrete Selenium or Playwright implementation into the Page Object. This reduces coupling, makes the framework easier to test and allows the underlying automation technology to be replaced without changing the business-level automation code."

## Quick Revision

```text
DIP
 |
 +-- High-level code -> Abstraction
 |
 +-- Low-level code  -> Abstraction
 |
 +-- Avoid direct dependency on implementations
 |
 +-- Dependency Injection is a common implementation technique
 |
 +-- Improves testability and flexibility
```

**Key takeaway:**

> Depend on abstractions, not concrete implementations.