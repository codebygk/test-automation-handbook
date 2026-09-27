# Open/Closed Principle (OCP)

## Definition

The **Open/Closed Principle** states that software entities should be:

- **Open for extension:** New functionality can be added.
- **Closed for modification:** Existing, tested code should not need to be changed whenever new functionality is introduced.

OCP is the second principle of **SOLID**.

The goal is to extend behavior without repeatedly modifying existing code.

---

## 1. Example: Violating OCP

Consider an automation framework that supports multiple browsers.

```python
class DriverFactory:

    def create_driver(self, browser):

        if browser == "chrome":
            return webdriver.Chrome()

        elif browser == "firefox":
            return webdriver.Firefox()

        elif browser == "edge":
            return webdriver.Edge()
```

### Problem

Every time a new browser is introduced, we must modify `DriverFactory`.

Adding Safari requires another condition:

```python
elif browser == "safari":
    return webdriver.Safari()
```

This creates a growing conditional structure and increases the risk of affecting existing functionality.

---

## 2. Applying OCP

Use abstraction and polymorphism to support new implementations.

### Step 1: Define an Interface

```python
from abc import ABC, abstractmethod


class BrowserProvider(ABC):

    @abstractmethod
    def create_driver(self):
        pass
```

### Step 2: Create Implementations

```python
from selenium import webdriver


class ChromeProvider(BrowserProvider):

    def create_driver(self):
        return webdriver.Chrome()


class FirefoxProvider(BrowserProvider):

    def create_driver(self):
        return webdriver.Firefox()
```

### Step 3: Use the Abstraction

```python
class DriverManager:

    def __init__(self, provider: BrowserProvider):
        self.provider = provider

    def start(self):
        return self.provider.create_driver()
```

Usage:

```python
manager = DriverManager(
    ChromeProvider()
)

driver = manager.start()
```

### Step 4: Extend Without Modification

To support Edge, introduce another implementation:

```python
class EdgeProvider(BrowserProvider):

    def create_driver(self):
        return webdriver.Edge()
```

```python
manager = DriverManager(
    EdgeProvider()
)

driver = manager.start()
```

`DriverManager` remains unchanged.

Only the new implementation and application configuration need to be added.

---

## 3. How OCP Works

```text
             BrowserProvider
                    |
           +--------+--------+
           |        |        |
         Chrome   Firefox   Edge
           |        |        |
           +--------+--------+
                    |
               DriverManager
```

`DriverManager` depends on the abstraction rather than individual browser implementations.

New providers can be introduced without changing its implementation.

---

## 4. OCP in Automation Frameworks

| Scenario                         | Applying OCP                       |
| -------------------------------- | ---------------------------------- |
| Multiple browsers                | Browser provider implementations   |
| Selenium and Playwright          | Common automation interface        |
| Different report formats         | Reporter implementations           |
| Different databases              | Repository interfaces              |
| Different authentication methods | Authentication strategies          |
| Different test environments      | Configurable environment providers |

### Example: Reporting

Instead of modifying the reporting class whenever a new report format is introduced, define a common contract.

```python
from abc import ABC, abstractmethod


class Reporter(ABC):

    @abstractmethod
    def generate(self, results):
        pass
```

Implement different formats:

```python
class HTMLReporter(Reporter):

    def generate(self, results):
        print("Generating HTML report")


class JSONReporter(Reporter):

    def generate(self, results):
        print("Generating JSON report")
```

The reporting service remains unchanged:

```python
class ReportingService:

    def __init__(self, reporter: Reporter):
        self.reporter = reporter

    def generate_report(self, results):
        self.reporter.generate(results)
```

New reporting formats can be added by creating new implementations.

---

## 5. Design Patterns Supporting OCP

| Pattern         | Purpose                                                  |
| --------------- | -------------------------------------------------------- |
| Strategy        | Add interchangeable behaviors                            |
| Factory         | Encapsulate object creation                              |
| Template Method | Extend selected steps of an algorithm                    |
| Decorator       | Add behavior without modifying the original class        |
| Adapter         | Integrate new implementations through a common interface |

OCP is commonly achieved through abstraction, polymorphism and composition.

However, not every conditional statement violates OCP. Introduce extensibility when there is a genuine requirement for varying implementations.

---

## 6. SRP vs OCP

| SRP                                              | OCP                                                          |
| ------------------------------------------------ | ------------------------------------------------------------ |
| Single Responsibility Principle                  | Open/Closed Principle                                        |
| One reason to change                             | Extend without modifying existing code                       |
| Focuses on cohesion                              | Focuses on extensibility                                     |
| Separates responsibilities                       | Supports new implementations                                 |
| Example: Separate reporting from browser actions | Example: Add new reporters without changing ReportingService |

Both principles help create maintainable automation frameworks.

---

## 7. Common Interview Questions

### What is the Open/Closed Principle?

Software entities should be open for extension but closed for modification. New behavior should be introduced without unnecessarily changing existing, tested code.

### How do you implement OCP in Python?

Using abstract classes, protocols, polymorphism, composition and dependency injection.

### Does OCP mean existing code should never be modified?

No. Existing code can be modified to fix bugs, improve design or accommodate changed requirements.

OCP aims to avoid repeatedly modifying stable components whenever new variations are introduced.

### How does polymorphism support OCP?

Polymorphism allows new implementations to satisfy an existing interface without changing the code that consumes that interface.

### How would you apply OCP in an automation framework?

I would define common interfaces for components that require multiple implementations, such as browser providers, reporters or authentication strategies.

New implementations can then be introduced without modifying the framework components that use them.

### What is the difference between OCP and dependency inversion?

OCP focuses on extending behavior without modifying existing components.

Dependency Inversion focuses on making high-level and low-level modules depend on abstractions.

Dependency Inversion often helps achieve OCP.

---

## Interview Answer

> "The Open/Closed Principle states that software components should be open for extension but closed for modification. In an automation framework, I apply it by defining abstractions for components that require multiple implementations, such as browser providers or reporters. For example, I can create a common BrowserProvider interface and implement ChromeProvider, FirefoxProvider and EdgeProvider. When a new browser is required, I add another implementation without modifying the existing DriverManager. This improves extensibility and reduces the risk of breaking tested functionality."

**Key takeaway:** Extend behavior through new implementations rather than repeatedly modifying stable code.