# Implicit Wait

## 1. Definition

An implicit wait tells Selenium WebDriver to wait for a specified maximum duration when trying to locate an element that is not immediately available.

It is configured once and applies to subsequent element searches throughout the WebDriver session.

## 2. Syntax

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("https://example.com")

element = driver.find_element(By.ID, "username")
```

Selenium waits for up to 10 seconds to locate the element.

- If the element is found immediately, execution continues immediately.
- If it appears after 3 seconds, execution continues after approximately 3 seconds.
- If it is not found within 10 seconds, Selenium raises `NoSuchElementException`.

## 3. How It Works

```text
find_element()
      |
      v
Element found?
      |
      +-- Yes --> Return element
      |
      +-- No --> Wait and retry
                       |
                       v
                Timeout reached?
                       |
                +------+------+
                |             |
                No           Yes
                |             |
                v             v
              Retry     NoSuchElementException
```

The wait is handled by the WebDriver implementation, which repeatedly attempts to locate the element until it succeeds or the timeout expires.

## 4. Important Characteristics

| Feature                     | Implicit Wait                                 |
| --------------------------- | --------------------------------------------- |
| Scope                       | Entire WebDriver session                      |
| Default timeout             | 0 seconds                                     |
| Maximum wait                | Configurable                                  |
| Stops when element is found | Yes                                           |
| Applies to                  | Element searches                              |
| Waits for visibility        | No                                            |
| Waits for clickability      | No                                            |
| Exception on timeout        | `NoSuchElementException` for `find_element()` |

## 5. find_element vs find_elements

```python
driver.implicitly_wait(10)

# Waits up to 10 seconds
element = driver.find_element(By.ID, "username")

# Waits up to 10 seconds
elements = driver.find_elements(By.CLASS_NAME, "item")
```

If no matching element appears before the timeout:

- `find_element()` raises `NoSuchElementException`.
- `find_elements()` returns an empty list.

For `find_elements()`, the search succeeds as soon as one or more matching elements are found. It does not wait for a particular number of elements.

## 6. Limitations

Implicit waits only help with locating elements.

They do not guarantee that an element is:

- Visible
- Clickable
- Enabled
- Fully loaded
- Ready for interaction

For these conditions, use explicit waits.

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)

button = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "login")
    )
)

button.click()
```

## 7. Implicit vs Explicit Wait

| Feature              | Implicit Wait    | Explicit Wait      |
| -------------------- | ---------------- | ------------------ |
| Scope                | Global           | Specific condition |
| Configuration        | Once per session | Per wait           |
| Element presence     | Yes              | Yes                |
| Element visibility   | No               | Yes                |
| Element clickability | No               | Yes                |
| Custom conditions    | No               | Yes                |
| Flexibility          | Limited          | High               |

**Important:** Avoid mixing implicit and explicit waits because their interaction can produce unpredictable timeout durations.

## 8. Interview Questions

**Q1. What is the default implicit wait?**

Zero seconds. Selenium attempts to locate the element without an implicit waiting period.

**Q2. Does implicit wait pause execution for the entire configured duration?**

No. It stops waiting as soon as the element is found.

**Q3. Does implicit wait apply to every WebDriver command?**

No. It applies to element-location operations, not commands such as `click()` or `get()`.

**Q4. Can implicit wait be changed during execution?**

Yes.

```python
driver.implicitly_wait(5)

# Change the timeout
driver.implicitly_wait(10)

# Disable implicit wait
driver.implicitly_wait(0)
```

**Q5. Which exception occurs when an element is not found?**

`NoSuchElementException` when using `find_element()`.

## 9. Interview Answer

"Implicit wait is a global timeout configured for a WebDriver session. It tells Selenium to repeatedly search for an element until it is found or the timeout expires. It only applies to element-location operations and does not guarantee visibility or clickability. I generally prefer explicit waits for dynamic applications because they allow me to wait for specific conditions."