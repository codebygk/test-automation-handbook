
# Pytest Fixtures

A **fixture** is a reusable function in Pytest that provides setup, teardown, test data, or dependencies to test cases.

Fixtures are commonly used in automation frameworks to manage WebDriver instances, API clients, database connections, and test configuration.

## 1. Basic Fixture

Use the `@pytest.fixture` decorator to define a fixture.

```python
import pytest

@pytest.fixture
def test_data():
    return {
        "username": "admin",
        "password": "secret"
    }

def test_login(test_data):
    assert test_data["username"] == "admin"
```

Pytest automatically executes the fixture and injects its return value into the test through the matching parameter name.

## 2. Setup and Teardown

Use `yield` when a fixture needs to release resources after test execution.

```python
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Setup
    driver = webdriver.Chrome()

    yield driver

    # Teardown
    driver.quit()

def test_homepage(driver):
    driver.get("https://example.com")
    assert driver.title
```

Execution flow:

```text
Fixture setup
    |
    v
yield driver
    |
    v
Test execution
    |
    v
Fixture teardown
```

The teardown code runs even if the test fails, provided the fixture successfully reaches `yield`.

## 3. Fixture Scopes

Scope determines how frequently a fixture is created and destroyed.

| Scope | Lifetime |
|---|---|
| function | Each test function (default) |
| class | Each test class |
| module | Each test module |
| package | Each test package |
| session | Entire test session |

Example:

```python
@pytest.fixture(scope="session")
def config():
    return {
        "base_url": "https://example.com"
    }
```

For Selenium, `function` scope generally provides better test isolation. Session scope is useful for configuration or expensive resources that can be safely shared.

## 4. Fixture Dependencies

Fixtures can depend on other fixtures.

```python
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

def test_login(login_page):
    login_page.login("admin", "secret")
```

Dependency flow:

```text
driver
   |
   v
login_page
   |
   v
test_login
```

Pytest automatically resolves fixture dependencies.

## 5. conftest.py

`conftest.py` is used to share fixtures across multiple test files without importing them individually.

Project structure:

```text
project/
    conftest.py
    tests/
        test_login.py
        test_search.py
        test_checkout.py
```

`conftest.py`:

```python
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
```

`test_login.py`:

```python
def test_login(driver):
    driver.get("https://example.com/login")
```

## 6. Fixture Parametrization

Use `params` to execute tests with different fixture values.

```python
@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    return request.param

def test_browser(browser):
    print(browser)
```

The test executes twice:

```text
test_browser[chrome]
test_browser[firefox]
```

For cross-browser automation, the fixture can create the appropriate WebDriver based on `request.param`.

## 7. Autouse Fixtures

An `autouse` fixture runs automatically without being explicitly requested by a test.

```python
@pytest.fixture(autouse=True)
def setup():
    print("Before test")

    yield

    print("After test")
```

Use `autouse=True` for setup that genuinely applies to every relevant test. Avoid overusing it because it creates implicit dependencies.

## 8. return vs yield

| return | yield |
|---|---|
| Provides a fixture value | Provides a fixture value |
| No teardown afterward | Supports teardown |
| Suitable for simple test data | Suitable for resource management |
| Simple configuration | Browser and database connections |

Example using `return`:

```python
@pytest.fixture
def user():
    return {"name": "John"}
```

Example using `yield`:

```python
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
```

## 9. Fixture vs @pytest.mark.parametrize

| Fixture Parametrization | Test Parametrization |
|---|---|
| Parametrizes dependencies | Parametrizes test inputs |
| Uses `@pytest.fixture(params=...)` | Uses `@pytest.mark.parametrize(...)` |
| Access values using `request.param` | Receives values as test arguments |
| Useful for browsers and environments | Useful for input/output combinations |

Example:

```python
@pytest.mark.parametrize(
    "username, expected",
    [
        ("admin", True),
        ("invalid", False)
    ]
)
def test_login(username, expected):
    assert validate_user(username) == expected
```

Both approaches can be combined.

## 10. Practical Selenium Framework

A reusable browser fixture with command-line configuration:

```python
# conftest.py

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        choices=["chrome", "firefox"]
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    driver.maximize_window()

    yield driver

    driver.quit()
```

Test:

```python
def test_homepage(driver):
    driver.get("https://example.com")
    assert driver.title
```

Execution:

```bash
pytest --browser=chrome
pytest --browser=firefox
```

## 11. Common Interview Questions

**What is a fixture?**

A reusable Pytest function that manages setup, teardown, test data, or dependencies.

**What is the default fixture scope?**

`function`. A new fixture instance is created for each test function that requires it.

**What is the purpose of conftest.py?**

To share fixtures and hooks across tests without explicit imports.

**Can one fixture depend on another?**

Yes. Pytest automatically resolves dependencies using fixture parameter names.

**What is autouse?**

It automatically executes a fixture for tests within its applicable scope.

**What happens if a test fails after yield?**

The fixture's teardown code still executes.

**What is the difference between fixtures and setup/teardown methods?**

Fixtures support dependency injection, multiple scopes, parametrization, composition, and reusable resource management.

## Quick Revision

```text
@pytest.fixture          Define a fixture
return                   Provide a value
yield                    Provide a value and teardown

scope="function"         Once per test
scope="class"            Once per class
scope="module"           Once per module
scope="package"          Once per package
scope="session"          Once per session

autouse=True             Execute automatically
params=[...]             Parametrize fixture
request.param            Access fixture parameter
conftest.py              Share fixtures
```

**Interview answer:** Pytest fixtures provide reusable setup, teardown, and test dependencies. They support different scopes, parametrization, dependency injection, and resource cleanup using `yield`.