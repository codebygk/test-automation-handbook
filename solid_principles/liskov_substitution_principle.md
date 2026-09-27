# Liskov Substitution Principle (LSP)

## Definition

The **Liskov Substitution Principle** states that objects of a subclass should be replaceable with objects of their parent class without breaking the expected behavior of the program.

LSP is the third principle of **SOLID**.

In simple terms:

- A subclass must honor the contract of its parent class.
- Subclasses should preserve expected behavior.
- Client code should work correctly with any valid subclass.

---

## 1. Example: Violating LSP

Consider an automation framework with different browser implementations.

```python
class Browser:

    def open(self, url):
        raise NotImplementedError

    def take_screenshot(self, path):
        raise NotImplementedError


class ChromeBrowser(Browser):

    def open(self, url):
        print(f"Opening {url} in Chrome")

    def take_screenshot(self, path):
        print(f"Saving screenshot to {path}")


class APIBrowser(Browser):

    def open(self, url):
        print(f"Sending request to {url}")

    def take_screenshot(self, path):
        raise NotImplementedError(
            "Screenshots are not supported"
        )
```

Client code:

```python
def capture_page(browser: Browser):
    browser.open("https://example.com")
    browser.take_screenshot("page.png")
```

This works with `ChromeBrowser` but fails with `APIBrowser`.

### Problem

`APIBrowser` cannot fulfill the contract defined by `Browser`.

Substituting it for the parent breaks the expected behavior.

This violates LSP.

---

## 2. Applying LSP

Design interfaces around meaningful capabilities.

### Step 1: Separate Contracts

```python
from abc import ABC, abstractmethod


class Browser(ABC):

    @abstractmethod
    def open(self, url):
        pass


class ScreenshotCapable(ABC):

    @abstractmethod
    def take_screenshot(self, path):
        pass
```

### Step 2: Implement Appropriate Interfaces

```python
class ChromeBrowser(Browser, ScreenshotCapable):

    def open(self, url):
        print(f"Opening {url} in Chrome")

    def take_screenshot(self, path):
        print(f"Saving screenshot to {path}")


class APIClient:

    def open(self, url):
        print(f"Sending request to {url}")
```

### Step 3: Depend on the Correct Contract

```python
def capture_page(
    browser: Browser,
    screenshot: ScreenshotCapable
):
    browser.open("https://example.com")
    screenshot.take_screenshot("page.png")
```

Usage:

```python
chrome = ChromeBrowser()

capture_page(chrome, chrome)
```

Now classes implement only the contracts they can actually fulfill.

---

## 3. Rules of LSP

A subclass should preserve the behavioral expectations of its parent.

| Rule           | Explanation                                               |
| -------------- | --------------------------------------------------------- |
| Preconditions  | Do not impose stricter input requirements                 |
| Postconditions | Do not weaken promised results                            |
| Invariants     | Preserve required object state                            |
| Exceptions     | Do not introduce unexpected failures for valid operations |
| Behavior       | Maintain the parent's documented contract                 |

### Preconditions

If a parent method accepts any non-negative timeout, a subclass should not unexpectedly reject timeouts below 10 seconds.

### Postconditions

If a parent method promises to return a valid screenshot path after successfully saving a screenshot, a subclass should not return `None` without changing the contract.

### Invariants

If a browser contract requires an initialized driver before navigation, subclasses must preserve that requirement.

---

## 4. Automation Framework Example

Suppose multiple browser implementations share a common interface.

```python
from abc import ABC, abstractmethod


class BrowserDriver(ABC):

    @abstractmethod
    def navigate(self, url):
        pass

    @abstractmethod
    def click(self, locator):
        pass
```

Implementations:

```python
class SeleniumDriver(BrowserDriver):

    def navigate(self, url):
        print(f"Selenium navigating to {url}")

    def click(self, locator):
        print(f"Selenium clicking {locator}")


class PlaywrightDriver(BrowserDriver):

    def navigate(self, url):
        print(f"Playwright navigating to {url}")

    def click(self, locator):
        print(f"Playwright clicking {locator}")
```

Client:

```python
def run_login_test(browser: BrowserDriver):
    browser.navigate("https://example.com")
    browser.click(("id", "login"))
```

Both implementations can be substituted as long as they honor the same contract.

For a real framework, locator formats, waiting behavior and error handling must also be consistent.

---

## 5. Inheritance vs LSP

| Inheritance                      | LSP                                    |
| -------------------------------- | -------------------------------------- |
| Mechanism for extending classes  | Principle governing substitutability   |
| Establishes an is-a relationship | Requires behavioral compatibility      |
| Enables method overriding        | Ensures overriding preserves contracts |
| Focuses on code structure        | Focuses on expected behavior           |

**Inheritance alone does not guarantee LSP.**

A subclass may inherit from a parent but still violate its behavioral contract.

---

## 6. LSP vs OCP

| LSP                             | OCP                                            |
| ------------------------------- | ---------------------------------------------- |
| Liskov Substitution Principle   | Open/Closed Principle                          |
| Ensures substitutability        | Supports extensibility                         |
| Preserves behavioral contracts  | Extends behavior without modifying stable code |
| Focuses on subclass correctness | Focuses on adding implementations              |

LSP supports OCP because new implementations can be introduced safely when they honor existing contracts.

---

## 7. Common Interview Questions

### What is LSP?

LSP states that subclasses should be substitutable for their parent classes without breaking the expected behavior of client code.

### Can a subclass override a parent method?

Yes. However, the overridden method must preserve the parent's behavioral contract.

### Does LSP prohibit raising exceptions?

No. A subclass can raise exceptions permitted by the parent contract. It should not unexpectedly reject operations that the parent promises to support.

### How can you identify an LSP violation?

Look for subclasses that:

- Reject inputs accepted by the parent.
- Return results that violate the parent's contract.
- Override methods with unsupported-operation errors.
- Require client code to check their concrete type.
- Break existing tests when substituted for the parent.

### How would you test LSP?

Create contract tests that run against every implementation of an interface.

```python
import pytest


@pytest.mark.parametrize(
    "browser",
    [
        SeleniumDriver(),
        PlaywrightDriver()
    ]
)
def test_browser_contract(browser):
    browser.navigate("https://example.com")
    browser.click(("id", "login"))
```

In a real framework, these tests should also verify observable behavior, valid inputs, error handling and cleanup.

---

## Interview Answer

> "The Liskov Substitution Principle states that a subclass should be replaceable with its parent without changing the correctness of the program. In an automation framework, if SeleniumDriver and PlaywrightDriver implement the same BrowserDriver interface, tests should work with either implementation without special conditions. Both implementations must honor the same contracts for navigation, clicking, waiting and error handling. I would use shared contract tests to verify substitutability and avoid forcing classes to implement operations they cannot support."

**Key takeaway:** A subclass must preserve its parent's behavioral contract, not merely implement the same methods.