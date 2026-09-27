# Selenium Locators

## 1. Definition

Locators are used to identify HTML elements on a web page so Selenium WebDriver can interact with them.

Common operations include clicking buttons, entering text, reading values and verifying element properties.

```python
from selenium.webdriver.common.by import By

element = driver.find_element(By.ID, "username")
element.send_keys("admin")
```

## 2. Types of Locators

Selenium supports **8 locator strategies**.

| Locator           | Syntax                 | Example                     |
| ----------------- | ---------------------- | --------------------------- |
| ID                | `By.ID`                | `"username"`                |
| Name              | `By.NAME`              | `"email"`                   |
| Class Name        | `By.CLASS_NAME`        | `"login-btn"`               |
| Tag Name          | `By.TAG_NAME`          | `"input"`                   |
| Link Text         | `By.LINK_TEXT`         | `"Forgot Password?"`        |
| Partial Link Text | `By.PARTIAL_LINK_TEXT` | `"Forgot"`                  |
| CSS Selector      | `By.CSS_SELECTOR`      | `"#username"`               |
| XPath             | `By.XPATH`             | `"//input[@id='username']"` |

## 3. Locator Examples

Consider the following HTML:

```html
<input id="username" name="user" class="form-input"
       type="text" placeholder="Username">

<input id="password" name="password" type="password">

<button id="login" class="btn primary" type="submit">
    Login
</button>

<a href="/forgot-password">Forgot Password?</a>
```

### ID

Identifies an element using its `id` attribute.

```python
driver.find_element(By.ID, "username")
```

Use when the ID is unique and stable.

### Name

Identifies an element using its `name` attribute.

```python
driver.find_element(By.NAME, "user")
```

Useful for form elements.

### Class Name

Identifies elements using a single CSS class.

```python
driver.find_element(By.CLASS_NAME, "form-input")
```

For elements with multiple classes, use one class name or a CSS selector.

```python
# Correct
driver.find_element(By.CLASS_NAME, "btn")

# Correct
driver.find_element(By.CSS_SELECTOR, ".btn.primary")

# Incorrect
driver.find_element(By.CLASS_NAME, "btn primary")
```

### Tag Name

Identifies elements by HTML tag.

```python
driver.find_elements(By.TAG_NAME, "input")
```

Useful when working with collections of elements.

### Link Text

Identifies an anchor element using its exact visible text.

```python
driver.find_element(
    By.LINK_TEXT,
    "Forgot Password?"
)
```

### Partial Link Text

Identifies an anchor element using part of its visible text.

```python
driver.find_element(
    By.PARTIAL_LINK_TEXT,
    "Forgot"
)
```

Partial matches can be ambiguous if several links contain the same text.

### CSS Selector

Identifies elements using CSS selector expressions.

```python
driver.find_element(
    By.CSS_SELECTOR,
    "#username"
)
```

Supports IDs, classes, attributes, relationships and structural selectors.

### XPath

Identifies elements using XPath expressions.

```python
driver.find_element(
    By.XPATH,
    "//input[@id='username']"
)
```

Supports attributes, text, relationships, ancestors and complex conditions.

## 4. CSS Selectors

| Selector         | Meaning                 | Example           |
| ---------------- | ----------------------- | ----------------- |
| `#id`            | ID                      | `#username`       |
| `.class`         | Class                   | `.login-btn`      |
| `tag`            | Tag                     | `input`           |
| `[attr='value']` | Attribute               | `[name='email']`  |
| `tag.class`      | Tag and class           | `button.primary`  |
| `A B`            | Descendant              | `form input`      |
| `A > B`          | Direct child            | `form > input`    |
| `A + B`          | Adjacent sibling        | `label + input`   |
| `A ~ B`          | General sibling         | `label ~ input`   |
| `:nth-child(n)`  | Position among siblings | `li:nth-child(2)` |

### Attribute Selectors

```python
# Exact match
driver.find_element(
    By.CSS_SELECTOR,
    "input[name='email']"
)

# Starts with
driver.find_element(
    By.CSS_SELECTOR,
    "input[id^='user']"
)

# Ends with
driver.find_element(
    By.CSS_SELECTOR,
    "input[id$='name']"
)

# Contains
driver.find_element(
    By.CSS_SELECTOR,
    "input[id*='serna']"
)
```

## 5. XPath

XPath is useful for complex DOM relationships and text-based element identification.

### Absolute vs Relative XPath

```python
# Absolute XPath
"/html/body/div/form/input[1]"

# Relative XPath
"//input[@id='username']"
```

Prefer relative XPath because absolute XPath is highly dependent on the DOM structure.

### Common XPath Expressions

| Expression                               | Purpose                |
| ---------------------------------------- | ---------------------- |
| `//input[@id='username']`                | Attribute match        |
| `//button[text()='Login']`               | Exact text             |
| `//button[contains(text(),'Login')]`     | Partial text           |
| `//input[contains(@id,'user')]`          | Attribute contains     |
| `//input[starts-with(@id,'user')]`       | Attribute starts with  |
| `//input[@type='text' and @name='user']` | Multiple conditions    |
| `//input[@type='text' or @type='email']` | Alternative conditions |
| `(//input)[1]`                           | First matching input   |
| `//div[@id='form']//input`               | Descendant input       |

### XPath Axes

XPath axes navigate relationships between elements.

| Axis                | Purpose                    |
| ------------------- | -------------------------- |
| `parent`            | Parent element             |
| `child`             | Direct children            |
| `ancestor`          | All matching ancestors     |
| `descendant`        | All matching descendants   |
| `following-sibling` | Following siblings         |
| `preceding-sibling` | Previous siblings          |
| `following`         | Elements appearing later   |
| `preceding`         | Elements appearing earlier |

Examples:

```python
# Parent
"//input[@id='username']/parent::div"

# Ancestor
"//input[@id='username']/ancestor::form"

# Following sibling
"//label[@for='username']/following-sibling::input"

# Preceding sibling
"//input[@id='username']/preceding-sibling::label"

# Descendant
"//form[@id='login']//input"
```

## 6. CSS vs XPath

| Feature                     | CSS Selector              | XPath                 |
| --------------------------- | ------------------------- | --------------------- |
| ID and class                | Yes                       | Yes                   |
| Attribute matching          | Yes                       | Yes                   |
| Parent navigation           | Limited with `:has()`     | Yes                   |
| Text matching               | No standard text selector | Yes                   |
| Sibling navigation          | Yes                       | Yes                   |
| Complex DOM relationships   | Yes                       | Yes                   |
| Readability                 | Often simpler             | Depends on expression |
| Browser support in Selenium | Yes                       | Yes                   |

**When to use CSS:**

- IDs, classes and attributes.
- Simple parent-child relationships.
- Straightforward, readable selectors.

**When to use XPath:**

- Locating elements using visible text.
- Navigating ancestors.
- Complex relationships between elements.

Neither strategy is universally faster. Locator stability and clarity are generally more important than small performance differences.

## 7. Dynamic Elements

Dynamic elements may have IDs or attributes that change between page loads.

Example:

```html
<input id="username_12345">
```

Instead of relying on the complete ID:

```python
driver.find_element(
    By.CSS_SELECTOR,
    "input[id^='username_']"
)
```

Or:

```python
driver.find_element(
    By.XPATH,
    "//input[starts-with(@id,'username_')]"
)
```

Prefer stable attributes such as `data-testid` when available.

```html
<button data-testid="submit-login">Login</button>
```

```python
driver.find_element(
    By.CSS_SELECTOR,
    "[data-testid='submit-login']"
)
```

## 8. find_element vs find_elements

| Feature          | `find_element()`       | `find_elements()`         |
| ---------------- | ---------------------- | ------------------------- |
| Returns          | First matching element | List of matching elements |
| No match         | Raises exception       | Returns empty list        |
| Multiple matches | Returns first          | Returns all               |
| Use case         | Single element         | Collection of elements    |

```python
# Single element
button = driver.find_element(
    By.ID,
    "login"
)

# Multiple elements
buttons = driver.find_elements(
    By.TAG_NAME,
    "button"
)
```

## 9. Locators and Explicit Waits

Locators identify elements, but they do not guarantee that an element is ready for interaction.

Use explicit waits for dynamic pages.

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

Common expected conditions:

- `presence_of_element_located`
- `visibility_of_element_located`
- `element_to_be_clickable`
- `invisibility_of_element_located`
- `presence_of_all_elements_located`

## 10. Locator Best Practices

1. Prefer unique, stable IDs or dedicated test attributes.
2. Use readable CSS selectors for straightforward relationships.
3. Use XPath when text matching or complex DOM navigation is necessary.
4. Avoid absolute XPath and fragile positional selectors.
5. Avoid dynamically generated attributes unless their stable portions are reliable.
6. Use explicit waits instead of hard-coded sleeps.
7. Centralize locators in Page Object classes.
8. Avoid selectors dependent on styling classes that frequently change.

### Page Object Example

```python
from selenium.webdriver.common.by import By

class LoginPage:

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-testid='submit-login']")

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(
            *self.USERNAME
        ).send_keys(username)

        self.driver.find_element(
            *self.PASSWORD
        ).send_keys(password)

        self.driver.find_element(
            *self.LOGIN_BUTTON
        ).click()
```

## 11. Common Interview Questions

**Q1. How many locator strategies does Selenium support?**

Eight: ID, Name, Class Name, Tag Name, Link Text, Partial Link Text, CSS Selector and XPath.

**Q2. Which locator should you prefer?**

A unique and stable ID or dedicated test attribute is generally a good choice. Otherwise, use a readable CSS selector or XPath based on the element's structure and available attributes.

**Q3. Can CSS selectors locate elements using visible text?**

No. Standard CSS selectors cannot directly match an element based on its text content. XPath supports text matching.

**Q4. How do you handle dynamic IDs?**

Use stable attributes, CSS attribute selectors or XPath functions such as `contains()` and `starts-with()`.

**Q5. What is the difference between absolute and relative XPath?**

Absolute XPath starts from the document root and is highly sensitive to structural changes. Relative XPath can locate elements from anywhere in the document.

**Q6. Can Selenium locate elements inside an iframe?**

Yes, but WebDriver must first switch to the appropriate frame using `switch_to.frame()`.

**Q7. Can Selenium locate elements inside Shadow DOM?**

Yes. Selenium 4 supports accessing a shadow root through `element.shadow_root`, provided the shadow root is accessible.

## 12. Interview Answer

"Selenium supports eight locator strategies, including ID, Name, CSS Selector and XPath. I generally prefer unique and stable IDs or dedicated test attributes, use CSS selectors for straightforward element relationships, and XPath when text matching or more complex DOM navigation is required. I centralize locators in Page Objects and combine them with explicit waits to make automation more maintainable and reliable."