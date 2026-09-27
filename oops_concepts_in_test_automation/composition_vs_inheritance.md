# Composition vs Inheritance

## Definition

**Inheritance** allows a class to reuse and extend the behavior of another class. It represents an **is-a** relationship.

**Composition** allows a class to contain and use objects of other classes. It represents a **has-a** relationship.

The general design principle is to **favor composition over inheritance** when the goal is simply to reuse functionality.

## 1. Inheritance

Use inheritance when classes share a genuine parent-child relationship and the child can safely substitute for the parent.

### Example

```python
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title


class LoginPage(BasePage):

    def login(self, username, password):
        self.driver.find_element(
            "id", "username"
        ).send_keys(username)

        self.driver.find_element(
            "id", "password"
        ).send_keys(password)
```

```python
login_page = LoginPage(driver)

print(login_page.get_title())
login_page.login("admin", "password")
```

Here, `LoginPage` is a specialized `BasePage`.

### When to Choose Inheritance

- There is a genuine is-a relationship.
- Multiple classes share a stable contract.
- Subclasses need to specialize or override behavior.
- The child can safely substitute for the parent.
- Shared behavior is unlikely to change frequently.

## 2. Composition

Use composition when one class needs the functionality of another class without becoming a subtype of it.

### Example

```python
class Browser:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def type(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)


class LoginPage:

    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        self.browser.type(
            ("id", "username"), username
        )

        self.browser.type(
            ("id", "password"), password
        )

        self.browser.click(("id", "login"))
```

```python
browser = Browser(driver)
login_page = LoginPage(browser)

login_page.login("admin", "password")
```

Here, `LoginPage` has a `Browser` object.

It delegates browser operations to that object instead of inheriting them.

### When to Choose Composition

- Classes have a has-a relationship.
- You need to combine independent behaviors.
- Dependencies may change in the future.
- You want to replace or mock components easily.
- You want to avoid deep inheritance hierarchies.
- You need flexible, loosely coupled components.

---

## 3. Key Differences

| Feature | Inheritance | Composition |
|---|---|---|
| Relationship | Is-a | Has-a |
| Reuse mechanism | Extending a parent | Delegating to objects |
| Coupling | Generally tighter | Generally looser |
| Flexibility | Limited by hierarchy | Components can be replaced |
| Polymorphism | Through overriding | Through interchangeable objects |
| Testing | May depend on parent behavior | Dependencies are easy to mock |
| Main risk | Fragile inheritance hierarchy | Additional delegation code |
| Best suited for | Stable specialization | Flexible behavior reuse |

## 4. Automation Framework Example

In a practical automation framework, I would use both.

```text
                Browser Interface
                       |
              SeleniumBrowser
                       |
                Browser Object
                       |
              Injected into Pages
                       |
                    BasePage
                       |
              +--------+--------+
              |                 |
          LoginPage        DashboardPage
```

**Inheritance:** `LoginPage` and `DashboardPage` inherit common page behavior from `BasePage`.

**Composition:** Each page contains a browser dependency to perform browser operations.

**Polymorphism:** The browser dependency can be implemented using Selenium or Playwright.

**Dependency injection:** The browser is supplied to the page instead of being created inside it.

### Combined Example

```python
class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def get_title(self):
        return self.browser.get_title()


class LoginPage(BasePage):

    def login(self, username, password):
        self.browser.type(
            ("id", "username"), username
        )

        self.browser.type(
            ("id", "password"), password
        )

        self.browser.click(("id", "login"))
```

Here:

- `LoginPage` inherits from `BasePage`.
- `BasePage` uses composition to hold a browser.
- The browser is injected through the constructor.
- Browser implementations can be changed without modifying the page classes.

---

## 5. Why Favor Composition?

Composition generally provides more flexibility because it allows behavior to be changed without modifying the class hierarchy.

For example, suppose a framework needs different logging implementations.

With inheritance, you might create multiple specialized subclasses.

With composition, simply inject the required logger:

```python
class Automation:

    def __init__(self, logger):
        self.logger = logger

    def execute(self):
        self.logger.log("Executing test")
```

The same automation class can work with a console logger, file logger or cloud logger.

However, composition introduces additional objects and delegation code. Inheritance can be simpler when the parent-child relationship is stable and meaningful.

---

## 6. Interview Questions

### What is the main difference?

Inheritance represents an is-a relationship, while composition represents a has-a relationship.

### Why is composition preferred over inheritance?

Composition usually provides better flexibility, lower coupling and easier testing. It allows implementations to be replaced without modifying the class hierarchy.

### When should you use inheritance?

When there is a genuine parent-child relationship, a stable shared contract and a need for specialization or method overriding.

### Can composition support polymorphism?

Yes. A class can hold an object implementing a common interface and delegate operations to different implementations.

### Can inheritance and composition be used together?

Yes. A Page Object can inherit common behavior from `BasePage` while using composition to hold a browser or driver dependency.

### What is the fragile base class problem?

Changes to a parent class can unintentionally break subclasses that depend on its implementation details.

### Is dependency injection the same as composition?

No. Composition describes an object containing or using another object. Dependency injection describes how that dependency is supplied.

---

## Interview Answer

> "I choose inheritance when there is a genuine is-a relationship and subclasses need to share or specialize stable behavior. I choose composition when a class needs functionality from another component without becoming its subtype. In automation frameworks, I use inheritance selectively for common page behavior through BasePage, while preferring composition and dependency injection for browser drivers, loggers and other services. This reduces coupling, improves testability and makes components easier to replace."

**Key takeaway:** Use inheritance for specialization and composition for flexible code reuse.