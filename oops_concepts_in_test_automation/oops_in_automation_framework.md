# OOP in Automation Framework

## Definition

OOP can be used to structure an automation framework into **reusable, maintainable and loosely coupled components**.

A typical framework can map OOP concepts like this:

```text
OOP Concept       Automation Example
------------------------------------------------
Encapsulation     Driver, Page Object
Abstraction       Browser interface
Inheritance       BasePage
Polymorphism      Selenium/Playwright implementations
Composition       Page contains Browser
```

---

# 1. Encapsulation

Encapsulation means keeping implementation details inside a class and exposing only what the caller needs.

```python
class Browser:

    def __init__(self, driver):
        self._driver = driver

    def click(self, locator):
        self._driver.find_element(*locator).click()

    def type(self, locator, text):
        element = self._driver.find_element(*locator)
        element.clear()
        element.send_keys(text)
```

The test does not directly interact with `_driver`.

```python
browser.click(("id", "login"))
```

Instead of:

```python
driver.find_element(By.ID, "login").click()
```

### Benefit

- Hides implementation details
- Centralizes common behavior
- Makes changes easier

---

# 2. Abstraction

Expose what the framework can do while hiding how it is implemented.

```python
from abc import ABC, abstractmethod


class Browser(ABC):

    @abstractmethod
    def open(self, url):
        pass

    @abstractmethod
    def click(self, locator):
        pass

    @abstractmethod
    def close(self):
        pass
```

The test only depends on the abstraction:

```python
browser.open(url)
browser.click(locator)
```

It does not need to know whether the implementation uses Selenium or Playwright.

---

# 3. Inheritance

Use inheritance when there is a genuine common base behavior.

```python
class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def click(self, locator):
        self.browser.click(locator)

    def type(self, locator, text):
        self.browser.type(locator, text)
```

Specific pages inherit common functionality:

```python
class LoginPage(BasePage):

    USERNAME = ("id", "username")
    PASSWORD = ("id", "password")
    LOGIN = ("id", "login")

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN)
```

Now every page does not need to implement common actions.

### Important

Do not create deep inheritance hierarchies just to reuse code.

Use inheritance for genuine **is-a** relationships.

---

# 4. Polymorphism

Different implementations can provide the same interface.

```python
class SeleniumBrowser:

    def click(self, locator):
        print("Selenium click")


class PlaywrightBrowser:

    def click(self, locator):
        print("Playwright click")
```

The Page Object can work with either:

```python
class LoginPage:

    def __init__(self, browser):
        self.browser = browser

    def login(self):
        self.browser.click(("id", "login"))
```

The same code works with:

```python
LoginPage(SeleniumBrowser())
LoginPage(PlaywrightBrowser())
```

The behavior changes based on the implementation.

---

# 5. Composition

Composition is often more useful than inheritance in automation frameworks.

A Page Object **has a** browser.

```python
class LoginPage:

    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        self.browser.type(("id", "username"), username)
        self.browser.type(("id", "password"), password)
        self.browser.click(("id", "login"))
```

Here:

```text
LoginPage
    |
    +-- has a --> Browser
```

This is composition.

It avoids tightly coupling `LoginPage` to a specific browser implementation.

---

# 6. Page Object Model

OOP is commonly applied through the Page Object Model.

```text
Test
 |
 +-- LoginPage
 |      |
 |      +-- Browser
 |
 +-- DashboardPage
        |
        +-- Browser
```

Example:

```python
class LoginPage:

    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        self.browser.type(("id", "username"), username)
        self.browser.type(("id", "password"), password)
        self.browser.click(("id", "login"))
```

Test:

```python
def test_login(browser):

    login_page = LoginPage(browser)

    login_page.login("admin", "secret")

    assert browser.get_text(("id", "welcome")) == "Welcome"
```

The test focuses on **what is being tested**, not Selenium implementation details.

---

# 7. Dependency Injection

Instead of creating dependencies inside classes, inject them.

Avoid:

```python
class LoginPage:

    def __init__(self):
        self.browser = SeleniumBrowser()
```

Prefer:

```python
class LoginPage:

    def __init__(self, browser):
        self.browser = browser
```

Then:

```python
browser = SeleniumBrowser()

login_page = LoginPage(browser)
```

### Benefits

- Loose coupling
- Easier mocking
- Easier unit testing
- Easier replacement of implementations
- Better reuse

---

# Complete Example

A simple framework could look like:

```python
from abc import ABC, abstractmethod


class Browser(ABC):

    @abstractmethod
    def open(self, url):
        pass

    @abstractmethod
    def click(self, locator):
        pass

    @abstractmethod
    def type(self, locator, text):
        pass


class SeleniumBrowser(Browser):

    def __init__(self, driver):
        self._driver = driver

    def open(self, url):
        self._driver.get(url)

    def click(self, locator):
        self._driver.find_element(*locator).click()

    def type(self, locator, text):
        element = self._driver.find_element(*locator)
        element.clear()
        element.send_keys(text)


class BasePage:

    def __init__(self, browser):
        self.browser = browser


class LoginPage(BasePage):

    USERNAME = ("id", "username")
    PASSWORD = ("id", "password")
    LOGIN = ("id", "login")

    def login(self, username, password):
        self.browser.type(self.USERNAME, username)
        self.browser.type(self.PASSWORD, password)
        self.browser.click(self.LOGIN)


class DashboardPage(BasePage):

    def get_title(self):
        return self.browser.get_text(("id", "title"))
```

The architecture becomes:

```text
Test
 |
 +-- LoginPage
 |       |
 |       +-- Browser interface
 |               |
 |               +-- SeleniumBrowser
 |
 +-- DashboardPage
         |
         +-- Browser interface
```

---

# OOP Concept Mapping

| OOP Concept          | Automation Framework                  |
| -------------------- | ------------------------------------- |
| Class                | Page, Browser, Driver, TestData       |
| Object               | `LoginPage()`, `Browser()`            |
| Encapsulation        | Hide driver implementation            |
| Abstraction          | Browser/Driver interface              |
| Inheritance          | `BasePage` -> specific pages          |
| Polymorphism         | Selenium/Playwright implementations   |
| Composition          | Page has Browser                      |
| Dependency Injection | Pass Browser into Page                |
| Method overriding    | Specialized page/framework behavior   |
| Interface            | `Browser` contract                    |
| Properties           | Controlled configuration/state access |

---

# What I Would Avoid

### Giant utility class

```python
class AutomationUtils:
    ...
```

with hundreds of unrelated methods.

### Hard-coded dependencies

```python
class LoginPage:

    def __init__(self):
        self.driver = webdriver.Chrome()
```

### Excessive inheritance

```text
Base
  |
BasePage
  |
BaseWebPage
  |
BaseLoginPage
  |
BaseAdminLoginPage
  |
LoginPage
```

### Business logic inside driver classes

The driver should handle browser operations, not business workflows.

---

# Interview Answer

> "I apply OOP by separating the automation framework into objects with clear responsibilities. I use encapsulation to hide driver implementation, abstraction to define common browser operations, inheritance for genuinely shared page behavior such as a BasePage, and polymorphism when supporting different implementations such as Selenium and Playwright. I prefer composition and dependency injection for Page Objects so they depend on a browser abstraction rather than creating a concrete driver themselves. This gives the framework better reusability, maintainability, testability and loose coupling."

## Strong Follow-up Point

If the interviewer asks **"Which OOP concept is most important in your framework?"**, don't simply name one concept.

A stronger answer is:

> "I use all four principles, but in practice I rely heavily on encapsulation, abstraction, composition and dependency injection to keep the framework loosely coupled. I use inheritance selectively for genuinely common behavior rather than using it as the primary mechanism for code reuse."
