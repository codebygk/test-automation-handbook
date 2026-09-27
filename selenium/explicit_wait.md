# Explicit Wait

## 1. Definition

An explicit wait tells Selenium to **wait until a specific condition is satisfied** or a maximum timeout is reached.

It is more flexible than an implicit wait because you can specify exactly what you are waiting for.

```python
from selenium.webdriver.support.ui import WebDriverWait

wait = WebDriverWait(driver, 10)
```

Here, Selenium waits for a maximum of 10 seconds for a condition.

## 2. Basic Example

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)

login_button = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "login")
    )
)

login_button.click()
```

The flow is:

```text
Wait
 |
 v
Check condition
 |
 +-- True  --> Continue
 |
 +-- False --> Wait briefly
                 |
                 v
            Check again
                 |
                 v
           Timeout reached?
                 |
          +------+------+
          |             |
         No            Yes
          |             |
          v             v
       Retry      TimeoutException
```

## 3. Common Expected Conditions

Selenium provides many built-in conditions through `expected_conditions`.

| Condition                                | Purpose                               |
| ---------------------------------------- | ------------------------------------- |
| `presence_of_element_located`            | Element exists in DOM                 |
| `visibility_of_element_located`          | Element exists and is visible         |
| `element_to_be_clickable`                | Element is visible and enabled        |
| `invisibility_of_element_located`        | Element becomes invisible/absent      |
| `presence_of_all_elements_located`       | Elements exist in DOM                 |
| `text_to_be_present_in_element`          | Element contains expected text        |
| `title_contains`                         | Page title contains text              |
| `title_is`                               | Page title exactly matches            |
| `url_contains`                           | URL contains text                     |
| `url_to_be`                              | URL matches expected URL              |
| `alert_is_present`                       | Alert is present                      |
| `frame_to_be_available_and_switch_to_it` | Frame is available and switches to it |

## 4. Presence vs Visibility vs Clickability

This is important for interviews.

### Presence

```python
wait.until(
    EC.presence_of_element_located(
        (By.ID, "username")
    )
)
```

Means:

```text
Element exists in the DOM
```

It does **not** necessarily mean the element is visible.

### Visibility

```python
wait.until(
    EC.visibility_of_element_located(
        (By.ID, "username")
    )
)
```

Means the element exists and is visible.

### Clickability

```python
wait.until(
    EC.element_to_be_clickable(
        (By.ID, "login")
    )
)
```

Checks that the element is visible and enabled.

## 5. Custom Explicit Wait

You can also wait for your own condition.

```python
wait = WebDriverWait(driver, 10)

wait.until(
    lambda driver: driver.find_element(
        By.ID, "status"
    ).text == "Completed"
)
```

This is useful when Selenium does not provide a suitable built-in expected condition.

## 6. Polling

`WebDriverWait` does not continuously execute the condition without pauses.

It repeatedly evaluates the condition until:

```text
Condition succeeds
        OR
Timeout expires
```

The polling interval can be configured.

```python
wait = WebDriverWait(
    driver,
    timeout=10,
    poll_frequency=0.5
)
```

This means Selenium checks approximately every 0.5 seconds.

## 7. Ignoring Exceptions

You can configure specific exceptions to be ignored while polling.

```python
from selenium.common.exceptions import NoSuchElementException

wait = WebDriverWait(
    driver,
    10,
    ignored_exceptions=[NoSuchElementException]
)
```

However, use this carefully. Blindly ignoring exceptions can hide real synchronization problems.

## 8. Explicit Wait vs Implicit Wait

| Feature          | Implicit Wait        | Explicit Wait           |
| ---------------- | -------------------- | ----------------------- |
| Scope            | Global session       | Specific operation      |
| Condition        | Element location     | Any supported condition |
| Visibility       | No                   | Yes                     |
| Clickability     | No                   | Yes                     |
| Custom condition | No                   | Yes                     |
| Flexibility      | Low                  | High                    |
| Typical usage    | Basic element lookup | Dynamic applications    |

## 9. Explicit Wait vs `time.sleep()`

### `time.sleep()`

```python
import time

time.sleep(5)

driver.find_element(By.ID, "login").click()
```

Problem:

```text
Element ready after 1 second
        |
        v
Still waits 4 unnecessary seconds
```

### Explicit Wait

```python
wait.until(
    EC.element_to_be_clickable(
        (By.ID, "login")
    )
)
```

If the element becomes clickable after 1 second:

```text
Condition satisfied
        |
        v
Continue immediately
```

Therefore, explicit waits are generally better for synchronization than hard-coded sleeps.

## 10. Important Exception

If the condition is not satisfied within the timeout:

```text
TimeoutException
```

Example:

```python
wait.until(
    EC.visibility_of_element_located(
        (By.ID, "missing")
    )
)
```

If the element never becomes visible within the timeout, Selenium raises `TimeoutException`.

## 11. Best Practices

- Prefer explicit waits for dynamic UI synchronization.
- Wait for the condition that actually matters.
- Avoid unnecessary `time.sleep()`.
- Use meaningful timeout values.
- Keep waits close to the operation that needs synchronization.
- Create reusable wait utilities if your framework has common synchronization patterns.
- Avoid mixing implicit and explicit waits because their interaction can produce unpredictable wait durations.

## 12. Automation Framework Example

A reusable wait wrapper can keep synchronization logic out of Page Objects:

```python
class WaitHelper:

    def __init__(self, driver, timeout=10):
        self.wait = WebDriverWait(driver, timeout)

    def clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )
```

Then:

```python
class LoginPage:

    LOGIN_BUTTON = (By.ID, "login")

    def __init__(self, driver):
        self.wait = WaitHelper(driver)

    def click_login(self):
        self.wait.clickable(
            self.LOGIN_BUTTON
        ).click()
```

This separates:

```text
Page Object
    |
    v
What to interact with

Wait Helper
    |
    v
How to synchronize
```

## 13. Interview Questions

**Q1. What is an explicit wait?**

An explicit wait waits for a specific condition to become true, up to a maximum timeout.

**Q2. What is `WebDriverWait`?**

`WebDriverWait` is Selenium's explicit wait utility used to repeatedly evaluate a condition until it succeeds or the timeout expires.

**Q3. What happens when the timeout expires?**

Selenium raises `TimeoutException`.

**Q4. Why use explicit wait instead of `sleep()`?**

Explicit wait is condition-based. It continues as soon as the required condition is satisfied, whereas `sleep()` always waits for the entire specified duration.

**Q5. What is the difference between presence and visibility?**

Presence means the element exists in the DOM. Visibility means the element exists and is visible to the user.

## 14. Interview Answer

"Explicit wait is a condition-based synchronization mechanism in Selenium. Using `WebDriverWait`, I can wait for a specific condition such as element visibility, clickability, text, URL or an alert, up to a defined timeout. Unlike `sleep()`, it stops as soon as the condition is satisfied, which makes it more reliable and efficient for dynamic web applications."