# Factory Pattern

A **Factory** is useful when object creation depends on configuration, environment, or runtime conditions.

The main idea is:

> Test code should ask for an object without knowing how that object is created.

## 1. Browser Factory

A common automation use case is creating different browser implementations.

### Simple Version

```python
class BrowserFactory:

    @staticmethod
    def create(browser_name):

        if browser_name == "chrome":
            return ChromeBrowser()

        if browser_name == "firefox":
            return FirefoxBrowser()

        if browser_name == "edge":
            return EdgeBrowser()

        raise ValueError(f"Unsupported browser: {browser_name}")
```

Usage:

```python
browser = BrowserFactory.create("chrome")
```

This is simple, but it has an OCP problem:

```text
Add Safari
    |
    v
Modify BrowserFactory
```

### SOLID-Compliant Version

If the framework needs to support adding new browsers without modifying the Factory, use registration.

```python
from abc import ABC, abstractmethod


class Browser(ABC):

    @abstractmethod
    def start(self):
        pass


class ChromeBrowser(Browser):

    def start(self):
        print("Starting Chrome")


class FirefoxBrowser(Browser):

    def start(self):
        print("Starting Firefox")


class EdgeBrowser(Browser):

    def start(self):
        print("Starting Edge")
```

Factory:

```python
class BrowserFactory:

    def __init__(self):
        self._browsers = {}

    def register(self, name, browser_class):
        self._browsers[name] = browser_class

    def create(self, name):
        browser_class = self._browsers.get(name)

        if browser_class is None:
            raise ValueError(f"Unsupported browser: {name}")

        return browser_class()
```

Registration:

```python
factory = BrowserFactory()

factory.register("chrome", ChromeBrowser)
factory.register("firefox", FirefoxBrowser)
factory.register("edge", EdgeBrowser)
```

Usage:

```python
browser = factory.create("chrome")
browser.start()
```

Adding Safari:

```python
class SafariBrowser(Browser):

    def start(self):
        print("Starting Safari")


factory.register("safari", SafariBrowser)
```

The `BrowserFactory` itself does not change.

```text
BrowserFactory
      |
      v
   Registry
      |
      +-- ChromeBrowser
      +-- FirefoxBrowser
      +-- EdgeBrowser
      +-- SafariBrowser
```

### Why This Follows OCP

```text
Existing Factory
      |
      | remains unchanged
      v
New Browser Implementation
      |
      v
Register new implementation
```

The Factory is:

- Open for extension
- Closed for modification

---

# 2. Reporter Factory

Another useful automation example is creating different reporting implementations.

```text
HTML Reporter
JSON Reporter
Allure Reporter
```

### Simple Version

```python
class ReporterFactory:

    @staticmethod
    def create(report_type):

        if report_type == "html":
            return HTMLReporter()

        if report_type == "json":
            return JSONReporter()

        if report_type == "allure":
            return AllureReporter()

        raise ValueError(f"Unsupported reporter: {report_type}")
```

Usage:

```python
reporter = ReporterFactory.create("html")
```

### OCP-Compliant Version

Define the abstraction:

```python
from abc import ABC, abstractmethod


class Reporter(ABC):

    @abstractmethod
    def generate(self, results):
        pass
```

Implementations:

```python
class HTMLReporter(Reporter):

    def generate(self, results):
        print("Generating HTML report")


class JSONReporter(Reporter):

    def generate(self, results):
        print("Generating JSON report")


class AllureReporter(Reporter):

    def generate(self, results):
        print("Generating Allure report")
```

Factory:

```python
class ReporterFactory:

    def __init__(self):
        self._reporters = {}

    def register(self, name, reporter_class):
        self._reporters[name] = reporter_class

    def create(self, name):
        reporter_class = self._reporters.get(name)

        if reporter_class is None:
            raise ValueError(f"Unsupported reporter: {name}")

        return reporter_class()
```

Registration:

```python
factory = ReporterFactory()

factory.register("html", HTMLReporter)
factory.register("json", JSONReporter)
factory.register("allure", AllureReporter)
```

Usage:

```python
reporter = factory.create("html")
reporter.generate(test_results)
```

Adding a new reporter:

```python
class XMLReporter(Reporter):

    def generate(self, results):
        print("Generating XML report")


factory.register("xml", XMLReporter)
```

Again, `ReporterFactory` itself does not change.

---

# Factory vs Dependency Injection

These are often confused.

| Factory | Dependency Injection |
|---|---|
| Creates the object | Provides the object |
| Controls object creation | Controls dependency delivery |
| Answers "What should I create?" | Answers "What should this class receive?" |
| `BrowserFactory.create()` | `LoginPage(browser)` |

They can work together:

```python
browser = BrowserFactory.create("chrome")

login_page = LoginPage(browser)
```

The Factory creates the dependency.

DI provides that dependency to the Page Object.

---

# When Should You Use Factory?

Use Factory when:

- There are multiple implementations
- Object creation depends on configuration
- Object creation is non-trivial
- Creation depends on environment
- You want to centralize creation logic
- You want test code to remain independent of concrete implementations

Don't create a Factory just because a class needs to be instantiated.

For example:

```python
user = User("John")
```

does not need:

```python
UserFactory.create("John")
```

unless object creation has meaningful variation or complexity.

---

# Interview Answer

> "In an automation framework, I would use Factory for things like browser and reporter creation. For example, a BrowserFactory can create Chrome, Firefox or Edge based on configuration, while a ReporterFactory can create HTML, JSON or Allure reporters. A simple if/elif Factory is easy to implement, but adding a new implementation requires modifying the Factory, which violates OCP. If the framework needs extensibility, I would use a registration-based Factory. The Factory maintains a registry and creates implementations through that registry, so new browsers or reporters can be added without modifying the Factory itself."

## Quick Revision

```text
Factory
    |
    +-- Browser creation
    +-- Reporter creation

Simple Factory
    -> Easy to understand
    -> New implementation requires Factory modification
    -> OCP violation

Registration-based Factory
    -> Factory contains creation mechanism
    -> Implementations are registered externally
    -> New implementation does not modify Factory
    -> OCP compliant
```