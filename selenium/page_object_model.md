# Page Object Model

**Page Object Model (POM)** is a Selenium design pattern where each application page or major UI component is represented by a class.

The Page Object contains:

- Locators
- Page-specific actions
- Synchronization/waits
- Page-related behavior

Test cases contain the **test flow and assertions**, not the UI implementation details.

## Without POM

```python
def test_login(driver):
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("password")
    driver.find_element(By.ID, "login").click()

    assert "Dashboard" in driver.title
```

If the login button locator changes, many tests may need modification.

## With POM

```python
class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")

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

Test:

```python
def test_login(driver):
    login_page = LoginPage(driver)

    login_page.login("admin", "password")

    assert "Dashboard" in driver.title
```

The test now focuses on **what** it is testing rather than **how** the UI is implemented.

# Typical Structure

```text
tests/
    test_login.py
    test_checkout.py

pages/
    login_page.py
    dashboard_page.py
    checkout_page.py

components/
    header.py
    navigation.py

utils/
    wait_helper.py

conftest.py
```

Example:

```text
Test
  |
  v
LoginPage
  |
  v
Browser / WebDriver
  |
  v
Application
```

# What Belongs in a Page Object?

### Locators

```python
USERNAME = (By.ID, "username")
PASSWORD = (By.ID, "password")
LOGIN_BUTTON = (By.ID, "login")
```

### Page actions

```python
def login(self, username, password):
    ...
```

### Page-specific waits

```python
def wait_until_loaded(self):
    ...
```

### Page-specific behavior

```python
def is_logged_in(self):
    ...
```

The Page Object should expose meaningful actions rather than forcing tests to know individual UI implementation details.

# What Should Stay in Tests?

Tests should generally contain:

- Test data
- Test flow
- Assertions
- Business scenario

Example:

```python
def test_valid_login(driver):
    login_page = LoginPage(driver)

    login_page.login("admin", "password")

    dashboard = DashboardPage(driver)

    assert dashboard.is_displayed()
```

The test describes the business scenario:

```text
Login -> Dashboard -> Verify
```

rather than:

```text
Find input -> type -> find button -> click -> find element
```

# Page Object with Dependency Injection

Instead of creating the driver inside the Page Object:

```python
class LoginPage:

    def __init__(self):
        self.driver = webdriver.Chrome()
```

inject it:

```python
class LoginPage:

    def __init__(self, driver):
        self.driver = driver
```

Then:

```python
login_page = LoginPage(driver)
```

This provides:

- Lower coupling
- Easier testing
- Easier driver replacement
- Better support for Selenium Grid
- Better support for different browsers

This also follows the **Dependency Inversion Principle** more closely.

# Page Object with Explicit Wait

Avoid putting arbitrary:

```python
time.sleep(5)
```

inside Page Objects.

Use explicit waits:

```python
class LoginPage:

    LOGIN_BUTTON = (By.ID, "login")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, username, password):
        self.wait.until(
            EC.visibility_of_element_located(self.USERNAME)
        ).send_keys(username)

        self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        ).send_keys(password)

        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()
```

In a larger framework, you would normally centralize this behavior in a reusable wait/helper layer rather than repeating it throughout every Page Object.

# Page Object vs Base Page

These are different concepts.

### Base Page

Contains genuinely common browser/page behavior:

```python
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def get_title(self):
        return self.driver.title
```

### Login Page

Contains login-specific behavior:

```python
class LoginPage(BasePage):

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")

    def login(self, username, password):
        self.click(self.USERNAME)
        ...
```

However, don't turn `BasePage` into a giant utility class containing every possible framework function.

# POM and Composition

A modern automation framework can use composition:

```python
class LoginPage:

    def __init__(self, browser, wait):
        self.browser = browser
        self.wait = wait
```

Architecture:

```text
Test
 |
 v
LoginPage
 |
 +-- Browser
 |
 +-- WaitHelper
 |
 +-- Logger
```

This often provides more flexibility than creating a deep Page Object inheritance hierarchy.

# POM vs Page Factory

These are often confused.

| Concept | Page Object Model | Page Factory |
|---|---|---|
| What is it? | Design pattern | Page initialization approach |
| Purpose | Organize page behavior | Initialize/manage page elements |
| Main idea | Page represented as object | Elements represented/initialized conveniently |
| Python Selenium | Commonly implemented manually | No special built-in PageFactory equivalent |

For Python Selenium, you typically implement POM using normal classes and Selenium locators.

# POM vs Test Code

| Responsibility | Page Object | Test |
|---|---|---|
| Locators | Yes | No |
| UI interaction | Yes | Usually no |
| Page-specific waits | Yes | Usually no |
| Business flow | Partially | Yes |
| Assertions | Usually no | Yes |
| Test data | No | Yes |
| Test scenario | No | Yes |

A useful rule:

```text
Page Object -> How to interact with the page
Test        -> What behavior to verify
```

# POM and Component Objects

Not every reusable UI element needs to become a full page.

For example:

```text
DashboardPage
    |
    +-- Header
    +-- Sidebar
    +-- UserMenu
```

You can model reusable components separately:

```python
class Header:

    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        ...
```

Then:

```python
class DashboardPage:

    def __init__(self, driver):
        self.driver = driver
        self.header = Header(driver)
```

This is **composition** and works well for large applications with reusable UI components.

# Common POM Mistakes

### 1. Putting assertions everywhere

Avoid:

```python
class LoginPage:

    def login(self):
        ...
        assert self.driver.title == "Dashboard"
```

Prefer:

```python
login_page.login(...)
assert dashboard_page.is_displayed()
```

The Page Object can expose state/behavior; the test generally decides what should be asserted.

### 2. Creating WebDriver inside every Page Object

Avoid:

```python
class LoginPage:

    def __init__(self):
        self.driver = webdriver.Chrome()
```

Prefer dependency injection:

```python
class LoginPage:

    def __init__(self, driver):
        self.driver = driver
```

### 3. Hard-coded sleeps

Avoid:

```python
time.sleep(5)
```

Prefer condition-based explicit waits.

### 4. Giant BasePage

Avoid putting everything into:

```python
BasePage
```

Keep common functionality genuinely common.

### 5. Page Object becoming a test

Avoid methods such as:

```python
def test_valid_login(self):
    ...
```

The Page Object should model application behavior, not contain the test suite.

# Interview Answer

> "Page Object Model is a design pattern where application pages or reusable UI components are represented as classes. Locators and page-specific interactions are encapsulated inside those classes, while tests focus on business scenarios and assertions. This reduces duplication, improves maintainability, and isolates tests from UI implementation changes. I typically inject the WebDriver into Page Objects rather than creating it internally, and use explicit waits for dynamic interactions."

# Key Benefits

```text
POM
 |
 +-- Encapsulation
 +-- Maintainability
 +-- Reusability
 +-- Less locator duplication
 +-- Separation of test and UI logic
 +-- Easier UI changes
 +-- Better framework structure
```

# Quick Revision

```text
Page Object
    |
    +-- Locators
    +-- Page actions
    +-- Page-specific behavior
    +-- Synchronization

Test
    |
    +-- Scenario
    +-- Test data
    +-- Assertions
```

Most important interview points:

```text
POM is a design pattern
Page = class
Locators = encapsulated
Actions = encapsulated
Tests = scenarios + assertions
Driver = preferably injected
Waits = explicit/condition-based
Reusable components = composition
```