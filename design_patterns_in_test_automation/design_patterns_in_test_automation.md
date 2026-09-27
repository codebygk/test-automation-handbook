# Design Patterns Used in Automation

For an automation framework interview, I would focus on patterns that solve real framework problems rather than listing every GoF pattern.

## Most Relevant Patterns

| Pattern                  | How I use it in automation                               | Example                                           |
| ------------------------ | -------------------------------------------------------- | ------------------------------------------------- |
| **Page Object Model**    | Encapsulate page locators and actions                    | `LoginPage`, `HomePage`                           |
| **Factory**              | Create the required driver/client based on configuration | `BrowserFactory`                                  |
| **Strategy**             | Switch between interchangeable behaviors                 | Selenium vs Playwright, different wait strategies |
| **Singleton**            | Share a controlled instance when truly required          | Configuration or logging                          |
| **Builder**              | Construct complex test data/configuration                | `UserBuilder`                                     |
| **Facade**               | Provide a simple API over complex framework operations   | `TestAutomationFacade`                            |
| **Adapter**              | Make different implementations follow the same interface | Selenium/Playwright adapter                       |
| **Template Method**      | Define common test flow while allowing variations        | Base test setup/teardown                          |
| **Dependency Injection** | Inject dependencies instead of creating them internally  | Inject `Browser` into Page Objects                |
| **Command**              | Represent actions as objects                             | Reusable UI actions / action queues               |

---

# 1. Page Object Model

Probably the most common pattern in UI automation.

```python
class LoginPage:

    def __init__(self, browser):
        self.browser = browser

    def enter_username(self, username):
        self.browser.find("#username").fill(username)

    def enter_password(self, password):
        self.browser.find("#password").fill(password)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.browser.click("#login")
```

Test:

```python
login_page.login("admin", "password")
```

### Why

- Encapsulates locators
- Separates test logic from UI implementation
- Improves maintainability
- Reduces duplication

---

# 2. Factory Pattern

Used when object creation depends on configuration.

```python
class BrowserFactory:

    @staticmethod
    def create(browser_name):
        if browser_name == "chrome":
            return ChromeBrowser()
        elif browser_name == "firefox":
            return FirefoxBrowser()
        raise ValueError("Unsupported browser")
```

Usage:

```python
browser = BrowserFactory.create("chrome")
```

### Automation use cases

- Browser creation
- API client creation
- Database client creation
- Reporter creation
- Environment-specific objects

### Interview point

Factory centralizes object creation so test code does not need to know how the object is constructed.

---

# 3. Strategy Pattern

Used when multiple algorithms or behaviors can be selected at runtime.

```python
class WaitStrategy:
    def wait(self, element):
        raise NotImplementedError


class ExplicitWait(WaitStrategy):
    def wait(self, element):
        ...


class FluentWait(WaitStrategy):
    def wait(self, element):
        ...
```

Then:

```python
class Browser:
    def __init__(self, wait_strategy):
        self.wait_strategy = wait_strategy
```

### Automation use cases

- Different wait strategies
- Different authentication mechanisms
- Different test data generation strategies
- Different environment configurations
- Selenium vs Playwright behavior
- Different reporting strategies

### Key idea

Instead of writing:

```python
if strategy == "explicit":
    ...
elif strategy == "fluent":
    ...
```

we can inject the appropriate strategy.

---

# 4. Adapter Pattern

Useful when different libraries expose different APIs but the framework wants one common interface.

```python
class Browser:
    def click(self, locator):
        raise NotImplementedError
```

Selenium adapter:

```python
class SeleniumAdapter(Browser):

    def click(self, locator):
        self.driver.find_element(...).click()
```

Playwright adapter:

```python
class PlaywrightAdapter(Browser):

    def click(self, locator):
        self.page.locator(locator).click()
```

Now Page Objects can work with:

```python
browser.click("#login")
```

without knowing whether the underlying implementation is Selenium or Playwright.

---

# 5. Facade Pattern

Provides a simple interface over several complex operations.

For example:

```python
class TestAutomationFacade:

    def login_and_create_order(self, user, order):
        self.login(user)
        self.create_order(order)
        self.verify_order()
```

Instead of the test managing:

```text
Browser
    |
Authentication
    |
API Client
    |
Database
    |
Page Objects
    |
Verification
```

the test can use one simple interface.

### Use carefully

A Facade simplifies complexity.

It should not become a giant utility class containing every possible automation operation.

---

# 6. Builder Pattern

Useful for creating complex test data.

```python
class UserBuilder:

    def __init__(self):
        self.data = {}

    def with_name(self, name):
        self.data["name"] = name
        return self

    def with_email(self, email):
        self.data["email"] = email
        return self

    def with_role(self, role):
        self.data["role"] = role
        return self

    def build(self):
        return self.data
```

Usage:

```python
user = (
    UserBuilder()
    .with_name("John")
    .with_email("john@test.com")
    .with_role("admin")
    .build()
)
```

### Automation use cases

- Test data
- API request payloads
- Complex configuration
- Test users
- Orders/products/customers

---

# 7. Template Method

Useful when tests share the same overall lifecycle but have different steps.

```python
class BaseTest:

    def run(self):
        self.setup()
        self.execute()
        self.cleanup()

    def setup(self):
        pass

    def execute(self):
        raise NotImplementedError

    def cleanup(self):
        pass
```

Concrete test:

```python
class LoginTest(BaseTest):

    def execute(self):
        # login test steps
        pass
```

The base class defines the overall workflow while subclasses provide specific behavior.

### Automation use cases

- Test setup/teardown
- Common API workflows
- Common UI workflows
- Environment initialization

---

# 8. Singleton Pattern

Ensures only one instance of a class exists.

Example:

```python
class ConfigManager:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

Possible automation uses:

- Configuration
- Logger
- Shared framework state

### Important interview point

Do not say:

> "I use Singleton everywhere."

Singleton introduces global state and can make tests harder to isolate.

Prefer dependency injection when practical.

---

# 9. Dependency Injection

DI is technically a technique rather than a classic GoF design pattern, but it is extremely important in automation architecture.

Instead of:

```python
class LoginPage:

    def __init__(self):
        self.browser = SeleniumBrowser()
```

inject the dependency:

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
- Easy Selenium/Playwright replacement
- Better maintainability

---

# How They Work Together

A realistic automation framework might look like:

```text
Tests
  |
  v
Page Objects
  |
  v
Browser Interface
  |
  +---- Selenium Adapter
  |
  +---- Playwright Adapter
  |
  v
Factory
  |
  v
Configuration
```

And test data could use:

```text
Test
  |
  v
User Builder
  |
  v
Test Data
```

While common workflows could use:

```text
Test
  |
  v
Facade
  |
  +---- Page Objects
  +---- API Client
  +---- Database Client
```

---

# What I Would Say in an Interview

> "I have used several design patterns in automation frameworks. The most common ones are Page Object Model, Factory, Strategy, Adapter, Facade, Builder and Template Method. I use Page Objects to encapsulate UI elements and workflows, Factory for driver and client creation, Strategy when I need interchangeable behaviors, Adapter to provide a common interface over different automation tools, Builder for complex test data, and Facade to simplify complex framework operations. I also use dependency injection extensively to reduce coupling and improve testability. I try to use patterns based on an actual design problem rather than forcing a pattern into the framework."

## Quick Revision

```text
POM       -> Encapsulate pages and UI behavior
Factory   -> Create objects
Strategy  -> Switch behavior
Adapter   -> Make different APIs look the same
Facade    -> Simplify complex operations
Builder   -> Build complex test data
Template  -> Define common workflow
Singleton -> One shared instance, when justified
DI        -> Inject dependencies and reduce coupling
```

## Common Interview Follow-ups

### Which design pattern do you use most?

> "Page Object Model is one of the most commonly used patterns in UI automation because it separates test logic from page-specific implementation. Along with that, I commonly use Factory, Strategy, Adapter and Dependency Injection depending on the framework requirements."

### Factory vs Strategy?

> "Factory is mainly concerned with object creation, whereas Strategy is concerned with selecting interchangeable behavior."

### Adapter vs Facade?

> "Adapter changes the interface of an existing component so it can work with our system. Facade provides a simpler interface over multiple components."

### Why not use inheritance everywhere?

> "I prefer composition and dependency injection where possible because they reduce coupling. I use inheritance when there is a genuine is-a relationship and shared behavior."

### Do design patterns always improve a framework?

> "No. Patterns solve specific design problems. Overusing them can add unnecessary abstraction and complexity. I use a pattern when it improves maintainability, flexibility, testability or separation of concerns."