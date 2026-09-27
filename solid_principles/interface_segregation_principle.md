# Interface Segregation Principle (ISP)

## Definition

The **Interface Segregation Principle** states:

> Clients should not be forced to depend on methods they do not use.

ISP is the fourth principle of **SOLID**.

In simple terms:

**Prefer small, focused interfaces over one large interface.**

---

## 1. Violating ISP

Imagine a large automation interface:

```python
from abc import ABC, abstractmethod


class AutomationDriver(ABC):

    @abstractmethod
    def open(self, url):
        pass

    @abstractmethod
    def click(self, locator):
        pass

    @abstractmethod
    def type(self, locator, text):
        pass

    @abstractmethod
    def upload_file(self, path):
        pass

    @abstractmethod
    def download_file(self, path):
        pass

    @abstractmethod
    def take_screenshot(self, path):
        pass

    @abstractmethod
    def execute_javascript(self, script):
        pass
```

Now suppose an API-based implementation only needs `open()` and does not support browser operations.

```python
class APIClient(AutomationDriver):

    def open(self, url):
        print(f"Calling {url}")

    def click(self, locator):
        raise NotImplementedError

    def type(self, locator, text):
        raise NotImplementedError

    def upload_file(self, path):
        raise NotImplementedError

    def download_file(self, path):
        raise NotImplementedError

    def take_screenshot(self, path):
        raise NotImplementedError

    def execute_javascript(self, script):
        raise NotImplementedError
```

This is a design problem.

`APIClient` is forced to depend on functionality that it does not need or support.

---

# 2. Applying ISP

Split the large interface into smaller, focused interfaces.

```python
from abc import ABC, abstractmethod


class Navigable(ABC):

    @abstractmethod
    def open(self, url):
        pass


class Clickable(ABC):

    @abstractmethod
    def click(self, locator):
        pass


class Typeable(ABC):

    @abstractmethod
    def type(self, locator, text):
        pass


class ScreenshotCapable(ABC):

    @abstractmethod
    def take_screenshot(self, path):
        pass
```

Now implementations can depend only on the capabilities they actually support.

```python
class WebDriver(
    Navigable,
    Clickable,
    Typeable,
    ScreenshotCapable
):

    def open(self, url):
        print(f"Opening {url}")

    def click(self, locator):
        print(f"Clicking {locator}")

    def type(self, locator, text):
        print(f"Typing {text}")

    def take_screenshot(self, path):
        print(f"Screenshot: {path}")
```

An API client only needs the relevant interface:

```python
class APIClient(Navigable):

    def open(self, url):
        print(f"Calling {url}")
```

No unnecessary methods are required.

---

# 3. Automation Framework Example

Instead of one huge interface:

```text
AutomationDriver
 |
 +-- open
 +-- click
 +-- type
 +-- upload
 +-- download
 +-- screenshot
 +-- execute_js
 +-- cookies
 +-- local_storage
 +-- mobile_actions
```

Use focused interfaces:

```text
Navigable
Clickable
Typeable
ScreenshotCapable
FileUploadCapable
JavaScriptExecutable
MobileActions
```

A particular implementation can implement only the capabilities it supports.

---

# 4. Why ISP Is Useful

### Without ISP

```text
Large Interface
       |
       +-- Selenium
       +-- Playwright
       +-- API Client
       +-- Mobile Client
```

Every implementation may be forced to support irrelevant operations.

### With ISP

```text
                 +-- Navigable
                 |
                 +-- Clickable
                 |
                 +-- Typeable
                 |
                 +-- ScreenshotCapable
                 |
                 +-- FileUploadCapable
```

Components depend only on the capabilities they need.

---

# 5. ISP + Dependency Injection

ISP becomes particularly useful with dependency injection.

Instead of:

```python
class LoginPage:

    def __init__(self, driver: AutomationDriver):
        self.driver = driver
```

The LoginPage only needs navigation, typing and clicking.

```python
class LoginPage:

    def __init__(
        self,
        navigator: Navigable,
        typer: Typeable,
        clicker: Clickable
    ):
        self.navigator = navigator
        self.typer = typer
        self.clicker = clicker
```

Now the Page Object does not depend on unrelated driver functionality.

---

# 6. ISP in Real Automation Design

A practical framework might define interfaces such as:

```python
class Browser(ABC):

    @abstractmethod
    def navigate(self, url):
        pass


class ElementActions(ABC):

    @abstractmethod
    def click(self, locator):
        pass

    @abstractmethod
    def type(self, locator, text):
        pass


class ScreenshotProvider(ABC):

    @abstractmethod
    def screenshot(self, path):
        pass
```

Then a class can depend only on what it requires.

For example:

```python
class LoginPage:

    def __init__(self, actions: ElementActions):
        self.actions = actions

    def login(self, username, password):
        self.actions.type(
            ("id", "username"),
            username
        )

        self.actions.type(
            ("id", "password"),
            password
        )

        self.actions.click(
            ("id", "login")
        )
```

`LoginPage` does not need access to screenshots, downloads or JavaScript execution.

---

# 7. ISP vs SRP

These principles are related but different.

| SRP                                            | ISP                                                        |
| ---------------------------------------------- | ---------------------------------------------------------- |
| Single Responsibility Principle                | Interface Segregation Principle                            |
| Focuses on classes/modules                     | Focuses on interfaces/contracts                            |
| One reason to change                           | Clients should not depend on unused methods                |
| Promotes cohesive classes                      | Promotes focused interfaces                                |
| Example: separate reporting from browser logic | Example: separate screenshot and browser action interfaces |

### Simple distinction

```text
SRP
"Does this class have too many responsibilities?"

ISP
"Does this interface force clients to depend on functionality they don't need?"
```

---

# 8. ISP vs LSP

| ISP                         | LSP                                      |
| --------------------------- | ---------------------------------------- |
| Split large interfaces      | Ensure implementations are substitutable |
| Focuses on interface design | Focuses on behavioral compatibility      |
| Avoids unused methods       | Avoids broken contracts                  |
| Prevents fat interfaces     | Prevents invalid substitutions           |

ISP can help prevent LSP violations because smaller interfaces make it less likely that a class will be forced to implement unsupported behavior.

---

# 9. Common Interview Questions

### What is ISP?

ISP states that clients should not be forced to depend on methods they do not use.

### What is a fat interface?

A large interface containing many unrelated methods that forces implementations to support functionality they may not need.

### How do you apply ISP in an automation framework?

I split large driver interfaces into focused capabilities such as navigation, element actions, screenshots and file operations. Components then depend only on the interfaces required for their specific responsibilities.

### Is ISP about having as many interfaces as possible?

No.

The goal is not to create an interface for every method. Interfaces should represent meaningful, cohesive capabilities.

### How does ISP improve testing?

Smaller interfaces make dependencies easier to mock and allow unit tests to provide only the behavior required by the component under test.

### Can one class implement multiple interfaces?

Yes.

```python
class SeleniumDriver(
    Navigable,
    Clickable,
    Typeable,
    ScreenshotCapable
):
    ...
```

This is a common way to model multiple capabilities.

---

# Interview Answer

> "The Interface Segregation Principle says that clients should not be forced to depend on methods they don't use. In an automation framework, instead of creating one large driver interface containing navigation, clicking, screenshots, file operations and JavaScript execution, I would split it into smaller, cohesive interfaces. For example, LoginPage might depend only on an ElementActions interface. This reduces coupling, makes dependencies easier to mock and prevents implementations from having to provide unsupported functionality."

## Quick Revision

```text
ISP
 |
 +-- Avoid fat interfaces
 +-- Create focused contracts
 +-- Depend only on required capabilities
 +-- Easier mocking and testing
 +-- Reduces coupling
 +-- Works well with composition and dependency injection
```

**Key takeaway:**

> Don't make a class implement or depend on functionality it doesn't need.