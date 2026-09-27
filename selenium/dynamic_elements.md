# Dynamic Elements

A **dynamic element** is a web element whose properties, location, state, or presence can change during page execution.

Examples:

- Dynamic IDs
- Elements loaded asynchronously
- Changing text
- Elements appearing/disappearing
- Dynamic lists/tables
- Elements whose position changes
- AJAX/API-loaded content

## Example

Suppose the HTML changes every time:

```html
<button id="login_48392">Login</button>
```

Next execution:

```html
<button id="login_72941">Login</button>
```

This locator is fragile:

```python
(By.ID, "login_48392")
```

Instead, identify the stable part:

```python
(By.CSS_SELECTOR, "button[id^='login_']")
```

or:

```python
(By.XPATH, "//button[starts-with(@id, 'login_')]")
```

# Strategies

## 1. Prefer Stable Attributes

Best option:

```html
<button data-testid="login-button">Login</button>
```

Use:

```python
(By.CSS_SELECTOR, "[data-testid='login-button']")
```

Prefer stable attributes such as:

```text
data-testid
data-test
data-qa
stable id
stable name
```

over dynamically generated attributes.

## 2. Partial Attribute Matching

### CSS

Starts with:

```python
(By.CSS_SELECTOR, "[id^='login_']")
```

Ends with:

```python
(By.CSS_SELECTOR, "[id$='_button']")
```

Contains:

```python
(By.CSS_SELECTOR, "[id*='login']")
```

### XPath

Starts with:

```python
(By.XPATH, "//button[starts-with(@id, 'login_')]")
```

Contains:

```python
(By.XPATH, "//button[contains(@id, 'login')]")
```

## 3. Use Multiple Stable Attributes

Instead of:

```python
(By.XPATH, "//input[@id='abc123']")
```

use:

```python
(By.XPATH, "//input[@name='username' and @type='text']")
```

Multiple stable attributes can make a locator more reliable.

## 4. Use Relative XPath

Avoid fragile absolute XPath:

```python
/html/body/div[2]/div[1]/form/div[3]/input
```

Prefer:

```python
//input[@name='username']
```

or:

```python
//form[@id='login-form']//input[@name='username']
```

## 5. Locate Based on Stable Relationships

Sometimes the element itself has no stable attribute.

Example:

```html
<div class="user-row">
    <span class="username">Gopal</span>
    <button class="delete">Delete</button>
</div>
```

You can locate the button relative to the username:

```python
locator = (
    By.XPATH,
    "//span[text()='Gopal']/following-sibling::button"
)
```

This is useful for dynamic tables and lists.

# Dynamic Content

An element can have a stable locator but still not exist immediately.

Example:

```python
driver.find_element(By.ID, "result")
```

may fail because the element is loaded asynchronously.

Use an explicit wait:

```python
wait = WebDriverWait(driver, 10)

element = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "result")
    )
)
```

The important distinction is:

```text
Dynamic locator
    -> element's identifying properties change

Dynamic loading
    -> element appears later
```

They can occur together.

# Dynamic Text

Suppose the text changes:

```text
Welcome, Gopal
Welcome, Arun
Welcome, Priya
```

Instead of:

```python
(By.XPATH, "//h1[text()='Welcome, Gopal']")
```

use:

```python
(By.XPATH, "//h1[starts-with(text(), 'Welcome')]")
```

or:

```python
(By.XPATH, "//h1[contains(text(), 'Welcome')]")
```

Be careful with overly broad `contains()` expressions.

# Dynamic Tables

Suppose a table contains:

```text
User       Action
Gopal      Delete
Arun       Delete
Priya      Delete
```

You want to delete Gopal.

Instead of relying on row position:

```python
//table/tbody/tr[1]/td[3]/button
```

locate the row using stable data:

```python
locator = (
    By.XPATH,
    "//tr[td[normalize-space()='Gopal']]//button[normalize-space()='Delete']"
)
```

This remains useful even if row ordering changes.

# Dynamic Lists

Example:

```html
<div class="product">
    <span class="name">Laptop</span>
    <button>Add to Cart</button>
</div>
```

Locate the button based on the product:

```python
locator = (
    By.XPATH,
    "//div[contains(@class, 'product')][.//span[normalize-space()='Laptop']]"
    "//button[normalize-space()='Add to Cart']"
)
```

This is generally more reliable than assuming the product is at a particular index.

# Dynamic Element + Wait

A good pattern is:

```python
locator = (
    By.CSS_SELECTOR,
    "[data-testid='login-button']"
)

button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(locator)
)

button.click()
```

Notice the separation:

```text
Locator -> identifies the element
Wait    -> waits for the required state
Action  -> interacts with it
```

# Avoid `time.sleep()`

Avoid:

```python
time.sleep(5)

driver.find_element(
    By.ID, "dynamic-element"
).click()
```

Prefer:

```python
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.ID, "dynamic-element")
    )
)

button.click()
```

The explicit wait stops as soon as the condition is satisfied.

# Dynamic Elements vs Stale Elements

These concepts are related but different.

### Dynamic element

The DOM/property/state changes:

```text
id changes
element appears later
list updates
text changes
```

### Stale element

You already have a WebElement reference, but the underlying DOM element was removed or replaced.

Example:

```python
element = driver.find_element(By.ID, "username")

# Page updates and replaces the element

element.click()
```

This can produce:

```text
StaleElementReferenceException
```

A common solution is to locate the element again after the DOM update.

# Best Locator Priority

For dynamic applications, a practical preference is:

```text
1. Dedicated test attribute
2. Stable unique ID
3. Stable name
4. Stable CSS attributes
5. Relative XPath using stable relationships
6. Partial attribute matching
7. Index-based locators
8. Absolute XPath
```

The exact order can depend on the application, but the principle is:

> Prefer stable, meaningful, application-independent locators over positional or implementation-fragile locators.

# Common Mistakes

### Fragile ID

```python
(By.ID, "input_839472")
```

when the ID changes every run.

### Index-based locator

```python
(By.XPATH, "(//button)[7]")
```

If the DOM changes, button 7 may no longer be the intended button.

### Absolute XPath

```python
/html/body/div[2]/div[3]/div[1]/button
```

Very sensitive to DOM structure changes.

### Excessive `contains()`

```python
//div[contains(@class, 'button')]
```

may match multiple unrelated elements.

Make the locator specific:

```python
//button[contains(@class, 'primary') and @type='submit']
```

# Framework Approach

Centralize dynamic locators:

```python
class LoginPage:

    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        "[data-testid='login-button']"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_login(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                self.LOGIN_BUTTON
            )
        )
        button.click()
```

This keeps:

```text
Locator
   |
   v
Page Object
   |
   v
Wait
   |
   v
Test
```

# Interview Answer

> "For dynamic elements, I first identify which part is actually changing. If the locator attributes are dynamic, I use stable attributes, dedicated test IDs, partial attribute matching, or stable relationships instead of indexes or absolute XPath. If the element is dynamically loaded, I use explicit waits for the required state such as presence, visibility, or clickability. I also avoid hard-coded sleeps and positional locators wherever possible."

# Quick Revision

```text
Dynamic ID
    -> CSS ^ / $ / *
    -> XPath starts-with() / contains()

Dynamic text
    -> contains() / starts-with()
    -> stable surrounding element

Dynamic list/table
    -> locate row/item using stable data
    -> locate child element relative to it

Dynamic loading
    -> WebDriverWait + ExpectedCondition

Avoid
    -> absolute XPath
    -> unnecessary indexes
    -> hard-coded sleeps
    -> overly broad locators
```

The key interview question is usually:

**"How would you handle a dynamic element?"**

A strong answer is:

> "I would first look for a stable attribute such as a test ID or stable ID. If that's unavailable, I'd construct a relative CSS or XPath locator using stable attributes or relationships. If the element is dynamically loaded, I'd combine that locator with an explicit wait for the appropriate condition."