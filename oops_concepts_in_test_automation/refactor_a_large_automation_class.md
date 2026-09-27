# Refactoring a Large Automation Class

## Definition

Refactoring a large automation class means breaking a monolithic class into smaller, reusable components with clear responsibilities while preserving its existing behavior.

The main goal is to improve maintainability, testability, scalability and code reuse.

## 1. Identify the Problems

A large automation class often contains:

- Driver initialization and management
- Element interactions and waits
- Page-specific locators
- Business workflows
- API and database operations
- Logging and reporting
- Configuration and test data
- Assertions and test execution

This violates the **Single Responsibility Principle (SRP)** because one class has too many reasons to change.

## 2. Refactoring Approach

### Step 1: Understand Existing Behavior

Before changing the implementation:

- Identify all public methods and their callers.
- Group methods by responsibility.
- Identify duplicated code and tightly coupled dependencies.
- Add characterization tests to preserve existing behavior.
- Identify shared mutable state and global dependencies.

Avoid rewriting the entire framework at once.

### Step 2: Separate Responsibilities

Extract related functionality into dedicated classes.

| Component | Responsibility |
|---|---|
| DriverFactory | Create and configure drivers |
| BrowserActions | Click, type, scroll and navigate |
| WaitHelper | Explicit waits and synchronization |
| BasePage | Common page-level behavior |
| Page Objects | Page-specific interactions |
| APIClient | API operations |
| DatabaseClient | Database operations |
| ConfigManager | Environment configuration |
| Reporter | Reporting and screenshots |

Keep assertions primarily in tests rather than generic browser utilities.

### Step 3: Apply Composition and Dependency Injection

Instead of creating dependencies inside each class, inject them through constructors.

This reduces coupling and makes mocking easier.

### Step 4: Introduce Abstraction Where Necessary

Use interfaces or protocols when multiple implementations are required.

For example, define a common browser contract if the framework must support Selenium and Playwright.

Avoid introducing unnecessary abstractions for components that have only one implementation and no foreseeable need for alternatives.

### Step 5: Refactor Incrementally

Move one responsibility at a time, update its callers and run regression tests before proceeding.

---

## 3. Before Refactoring

Consider a monolithic automation class:

```python
class Automation:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def type(self, locator, text):
        self.driver.find_element(
            *locator
        ).send_keys(text)

    def login(self, username, password):
        self.type(("id", "username"), username)
        self.type(("id", "password"), password)
        self.click(("id", "login"))

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    def close(self):
        self.driver.quit()
```

### Problems

- Driver creation is tightly coupled to the class.
- Browser operations and business workflows are mixed.
- Reusing browser functionality requires using the entire class.
- Mocking dependencies is difficult.
- Adding more pages makes the class increasingly complex.

---

## 4. After Refactoring

### Driver Factory

Separate driver creation from browser operations.

```python
from selenium import webdriver


class DriverFactory:

    @staticmethod
    def create(browser="chrome"):

        if browser == "chrome":
            return webdriver.Chrome()

        if browser == "firefox":
            return webdriver.Firefox()

        raise ValueError(
            f"Unsupported browser: {browser}"
        )
```

### Browser Actions

Encapsulate common browser operations.

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BrowserActions:

    def __init__(self, driver, timeout=10):
        self._driver = driver
        self._wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self._driver.get(url)

    def click(self, locator):
        element = self._wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def type(self, locator, text):
        element = self._wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def screenshot(self, filename):
        return self._driver.save_screenshot(filename)

    def close(self):
        self._driver.quit()
```

Browser interactions are now centralized, and explicit waits replace fragile immediate element lookups.

### Page Object

Move page-specific locators and business actions into a dedicated class.

```python
class LoginPage:

    USERNAME = ("id", "username")
    PASSWORD = ("id", "password")
    LOGIN_BUTTON = ("id", "login")

    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        self.browser.type(
            self.USERNAME, username
        )

        self.browser.type(
            self.PASSWORD, password
        )

        self.browser.click(
            self.LOGIN_BUTTON
        )
```

### Test

```python
def test_login():

    driver = DriverFactory.create()
    browser = BrowserActions(driver)

    try:
        browser.open("https://example.com")

        login_page = LoginPage(browser)

        login_page.login(
            "admin",
            "password"
        )

        # Assert the expected login result.

    finally:
        browser.close()
```

In a pytest framework, driver creation and cleanup would normally be handled by fixtures.

---

## 5. Refactored Architecture

```text
Automation Framework
|
+-- Core
|   +-- DriverFactory
|   +-- BrowserActions
|   +-- WaitHelper
|
+-- Pages
|   +-- BasePage
|   +-- LoginPage
|   +-- DashboardPage
|
+-- Services
|   +-- APIClient
|   +-- DatabaseClient
|
+-- Utilities
|   +-- ConfigManager
|   +-- Logger
|   +-- Reporter
|
+-- Tests
    +-- test_login.py
    +-- test_dashboard.py
```

Create separate components only when their responsibilities justify the separation.

---

## 6. OOP Principles Applied

| Principle | Application |
|---|---|
| Encapsulation | Hide driver implementation inside BrowserActions |
| Abstraction | Expose common browser operations |
| Inheritance | Share common page behavior through BasePage |
| Polymorphism | Support interchangeable browser implementations |
| Composition | Page Objects contain browser dependencies |
| Dependency Injection | Pass dependencies through constructors |
| SRP | Separate browser, page, API and reporting responsibilities |
| DRY | Centralize repeated interactions and workflows |

**Prefer composition over deep inheritance hierarchies.**

For example, a `LoginPage` should receive a browser dependency rather than inherit directly from a Selenium WebDriver.

---

## 7. Refactoring Patterns

| Pattern | When to Use |
|---|---|
| Extract Class | Separate unrelated responsibilities |
| Extract Method | Break down long methods |
| Strategy | Support interchangeable algorithms or implementations |
| Factory | Centralize driver creation |
| Adapter | Standardize different automation tools |
| Facade | Provide a simple API over multiple components |
| Page Object Model | Separate UI interactions from tests |
| Dependency Injection | Remove hard-coded dependencies |

Do not introduce every pattern automatically. Choose patterns that solve an existing design problem.

---

## 8. Common Mistakes

- Rewriting the entire framework without regression tests.
- Creating excessive utility classes.
- Introducing deep inheritance hierarchies.
- Moving all methods into a giant `BasePage`.
- Mixing assertions with generic browser actions.
- Creating a new WebDriver inside every Page Object.
- Using global drivers and shared mutable state.
- Introducing unnecessary interfaces and design patterns.
- Changing framework behavior during structural refactoring.
- Breaking existing tests without a migration strategy.

For a framework with many existing tests, maintain backward compatibility temporarily through a facade or adapter while migrating callers.

---

## 9. Interview Questions

### How would you start refactoring a large automation class?

I would analyze its responsibilities and dependencies, identify duplicated functionality, add tests to preserve existing behavior and gradually extract cohesive components.

### Which SOLID principle is most relevant?

The Single Responsibility Principle is particularly relevant because a large automation class often combines unrelated responsibilities.

Dependency Inversion is also important when separating Page Objects from concrete driver implementations.

### Would you use inheritance or composition?

I would prefer composition for browser actions, API clients, loggers and other dependencies. I would use inheritance selectively for genuinely shared page behavior.

### How would you ensure refactoring does not break existing tests?

I would establish baseline regression tests, refactor incrementally, preserve existing public interfaces where practical and run tests after each change.

### How would you handle hundreds of tests depending on the original class?

I would introduce a compatibility facade that delegates existing methods to the new components, then gradually migrate tests to the new APIs.

---

## Interview Answer

> "I would first analyze the large automation class to identify its responsibilities, dependencies and duplicated functionality. I would add regression tests to preserve existing behavior and then incrementally extract separate components for driver management, browser actions, synchronization, Page Objects, API operations and reporting. I would apply the Single Responsibility Principle, use composition and dependency injection to reduce coupling, and introduce interfaces only where multiple implementations are needed. For an existing framework, I would maintain backward compatibility through a facade while gradually migrating tests. After each change, I would run regression tests to ensure the refactoring has not introduced functional changes."

## Key Takeaway

**Refactor incrementally, separate responsibilities and preserve existing behavior.**

The objective is not to create more classes. It is to create cohesive, independently testable components with clear boundaries.