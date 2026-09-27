# Reusable Automation Class

## Definition

A reusable automation class should encapsulate **common automation behavior** while keeping application-specific details separate.

The goal is:

- Reuse common functionality
- Avoid duplicated code
- Keep tests simple
- Reduce coupling
- Make maintenance easier
- Allow different implementations when needed

A good design usually combines:

- Encapsulation
- Abstraction
- Composition
- Dependency injection
- Interfaces or protocols
- Single Responsibility Principle

---

## Example

Suppose we are building a reusable UI automation framework.

Instead of putting Selenium code directly inside every test:

```python
def test_login():
    driver = webdriver.Chrome()
    driver.get("https://example.com")

    driver.find_element(...).send_keys("user")
    driver.find_element(...).send_keys("password")
    driver.find_element(...).click()
```

Create reusable components.

```python
class Browser:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def close(self):
        self.driver.quit()
```

Now tests become simpler:

```python
browser = Browser(driver)

browser.open("https://example.com")
browser.type(("id", "username"), "admin")
browser.type(("id", "password"), "secret")
browser.click(("id", "login"))
```

---

# Better Design

Instead of making one huge automation class, separate responsibilities.

```text
Test
 |
 +-- Page Object
 |     |
 |     +-- Browser / Driver
 |
 +-- Test Data
 |
 +-- Configuration
 |
 +-- Utilities
```

For example:

```python
class LoginPage:

    USERNAME = ("id", "username")
    PASSWORD = ("id", "password")
    LOGIN = ("id", "login")

    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        self.browser.type(self.USERNAME, username)
        self.browser.type(self.PASSWORD, password)
        self.browser.click(self.LOGIN)
```

Test:

```python
browser = Browser(driver)
login_page = LoginPage(browser)

login_page.login("admin", "secret")
```

The test does not need to know how Selenium finds or clicks elements.

---

# Use Abstraction

If you want the framework to support different automation tools, define an interface.

```python
from abc import ABC, abstractmethod


class BrowserDriver(ABC):

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
    def close(self):
        pass
```

Selenium implementation:

```python
class SeleniumDriver(BrowserDriver):

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def type(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def close(self):
        self.driver.quit()
```

Now the Page Object depends on the abstraction:

```python
class LoginPage:

    def __init__(self, browser: BrowserDriver):
        self.browser = browser

    def login(self, username, password):
        self.browser.type(("id", "username"), username)
        self.browser.type(("id", "password"), password)
        self.browser.click(("id", "login"))
```

This makes the framework less dependent on Selenium.

---

# Dependency Injection

Do not create the driver inside every class.

Avoid:

```python
class LoginPage:

    def __init__(self):
        self.driver = webdriver.Chrome()
```

Prefer:

```python
class LoginPage:

    def __init__(self, browser):
        self.browser = browser
```

Then inject the dependency:

```python
browser = Browser(driver)
login_page = LoginPage(browser)
```

Benefits:

- Easier testing
- Easier mocking
- Less coupling
- Easier replacement of implementations
- Better reuse

---

# What Should the Class Contain?

A reusable automation class should generally contain:

```text
Configuration
    |
Driver management
    |
Common actions
    |
Synchronization / waits
    |
Logging
    |
Error handling
```

For example:

```python
class Browser:

    def open(self, url):
        ...

    def click(self, locator):
        ...

    def type(self, locator, text):
        ...

    def get_text(self, locator):
        ...

    def wait_for_visible(self, locator):
        ...

    def wait_for_clickable(self, locator):
        ...

    def screenshot(self, name):
        ...

    def close(self):
        ...
```

But avoid putting business-specific operations here.

Bad:

```python
class Browser:

    def login_to_admin_portal(self):
        ...

    def create_customer(self):
        ...

    def generate_invoice(self):
        ...
```

These belong in Page Objects, services, or business-level components.

---

# Separation of Responsibilities

| Component | Responsibility |
|---|---|
| Driver | Communicate with browser |
| Browser wrapper | Common browser operations |
| Page Object | Page-specific interactions |
| Component Object | Reusable UI component |
| Test | Verify behavior |
| Test Data | Provide input |
| Config | Environment/settings |
| Utility | Generic helper functionality |
| Reporter | Test results |
| Logger | Diagnostic information |

---

# Design Principles

### Single Responsibility

Each class should have one primary responsibility.

```text
Browser
    -> browser operations

LoginPage
    -> login page operations

LoginTest
    -> login verification
```

### Open/Closed Principle

The framework should be extendable without constantly modifying existing classes.

For example:

```text
BrowserDriver
    |
    +-- SeleniumDriver
    +-- PlaywrightDriver
```

### Dependency Inversion

High-level components should depend on abstractions rather than concrete implementations.

```python
class LoginPage:

    def __init__(self, browser: BrowserDriver):
        self.browser = browser
```

Rather than:

```python
class LoginPage:

    def __init__(self):
        self.driver = SeleniumDriver()
```

---

# Reusable Automation Class Checklist

```text
[ ] Single responsibility
[ ] No hard-coded environment values
[ ] Dependency injection
[ ] Clear public API
[ ] Encapsulated implementation details
[ ] Reusable common actions
[ ] Explicit waits instead of unnecessary sleeps
[ ] Logging
[ ] Error handling
[ ] Screenshot support
[ ] Configuration support
[ ] Easy mocking
[ ] Easy extension
[ ] No application-specific logic in generic classes
```

# Interview Answer

> "I would first identify the common behavior that needs to be reused and encapsulate it behind a small, clean API. For example, in a UI automation framework I would create a Browser or Driver abstraction containing operations such as open, click, type, wait and close. Page-specific behavior would go into Page Objects, while tests would contain only verification logic. I would use dependency injection so the Page Objects depend on an abstraction rather than directly creating Selenium or Playwright drivers. This gives us loose coupling, better testability, easier maintenance and the ability to replace the underlying automation tool without changing the tests."

## Key Interview Point

**Don't design one giant `AutomationUtils` class.**

A strong automation framework separates:

```text
Generic automation
        |
        v
Driver / Browser
        |
        v
Page Objects
        |
        v
Tests
```

This is usually a much better answer than simply saying "I would create a reusable Selenium utility class."