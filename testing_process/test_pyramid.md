# Test Pyramid

The **Test Pyramid** is a testing strategy that recommends having:

- Many fast, low-level tests
- Fewer medium-level tests
- Very few slow, expensive end-to-end tests

```text
              /\
             /  \
            / UI \
           / E2E  \
          /--------\
         /          \
        / Integration\
       /   API tests  \
      /----------------\
     /                  \
    /    Unit Tests      \
   /______________________\
```

The idea is to get **fast feedback with good coverage while minimizing expensive UI tests**.

# Three Main Layers

## 1. Unit Tests

Test individual functions, methods, or small components in isolation.

```python
def calculate_discount(price, discount):
    return price - (price * discount / 100)
```

Test:

```python
def test_calculate_discount():
    assert calculate_discount(1000, 10) == 900
```

Characteristics:

- Fast
- Large number of tests
- Usually isolated
- Easy to debug
- Usually run on every commit

Example:

```text
1000 unit tests
```

---

## 2. Integration / API Tests

Test interaction between components.

Examples:

```text
Application -> Database
Application -> Service
Client -> REST API
Service A -> Service B
```

API example:

```python
response = requests.get(
    "/users/101",
    timeout=10
)

assert response.status_code == 200
assert response.json()["id"] == 101
```

Characteristics:

- Slower than unit tests
- More realistic
- Validate component interactions
- Usually fewer than unit tests

Example:

```text
200 API/integration tests
```

---

## 3. UI / End-to-End Tests

Test the complete application through the user interface.

Example:

```text
Open browser
    |
Login
    |
Search product
    |
Add product to cart
    |
Checkout
    |
Verify order
```

Using Selenium:

```python
driver.get("/login")

driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("password")
driver.find_element(By.ID, "login").click()
```

Characteristics:

- Slow
- More expensive
- More fragile
- More dependencies
- Harder to debug
- Should generally be limited to critical user journeys

Example:

```text
20 UI/E2E tests
```

# Typical Distribution

There is **no mandatory percentage**.

A common conceptual distribution might look like:

```text
        UI / E2E
           10%
        Integration
           20%
           Unit
           70%
```

The important principle is the **shape**, not exact numbers.

```text
Many       -> Unit
Moderate   -> Integration/API
Few        -> UI/E2E
```

# Why Not Have More UI Tests?

Suppose you have:

```text
1000 UI tests
```

Problems can include:

- Long execution time
- Browser startup overhead
- Flaky tests
- Environment dependencies
- Difficult debugging
- Expensive parallel execution
- Slow CI feedback

Instead, many business rules can be tested faster at lower layers.

```text
Business Rule

Unit Test       -> milliseconds
API Test        -> seconds
UI Test         -> potentially much slower
```

So the same behavior should generally be tested at the **lowest practical layer**.

# Example

Suppose an application has:

```text
Login
Search
Cart
Payment
```

Instead of testing every validation through Selenium:

```text
1000 UI tests
```

You could have:

```text
Unit:
- Password validation
- Price calculation
- Discount calculation
- Cart calculation

API:
- Login API
- Product API
- Cart API
- Payment API

UI:
- Successful login
- Search product
- Add product to cart
- Complete checkout
```

This gives faster feedback while still testing critical end-to-end flows.

# Test Pyramid vs Test Automation Pyramid

They are often used interchangeably in interviews, but conceptually:

```text
Test Pyramid
    =
Testing strategy

Automation Pyramid
    =
Applying the same distribution specifically to automated tests
```

# Test Pyramid and Shift-Left

They complement each other.

```text
Shift-Left
    |
    v
Test earlier
    |
    v
Test at lower levels
    |
    v
Test Pyramid
```

Unit and API tests provide earlier and faster feedback than UI tests.

# Test Pyramid vs Testing Trophy

Another model is the **Testing Trophy**:

```text
        E2E
         /\
        /  \
       /Integration\
      /______________\
      /    Unit       \
     /_________________\
```

The Testing Trophy places strong emphasis on **integration testing**.

The Test Pyramid traditionally emphasizes a large base of unit tests.

The practical lesson is not to blindly follow a fixed diagram. Choose the test level based on:

- Risk
- Cost
- Feedback speed
- Maintainability
- System architecture
- Business criticality

# Common Interview Questions

### What is the Test Pyramid?

> "The Test Pyramid is a testing strategy where we have many fast unit tests at the bottom, fewer integration or API tests in the middle, and a small number of end-to-end UI tests at the top."

### Why should UI tests be fewer?

> "UI tests are generally slower, more expensive, and more prone to environmental and synchronization issues. Lower-level tests can provide faster and more stable feedback."

### Does the pyramid require 70/20/10?

> "No. Those percentages are only an example. The important principle is having more fast lower-level tests and fewer expensive end-to-end tests."

### Where would API tests fit?

> "Usually in the integration or service layer, between unit tests and UI tests."

### Should everything be tested at the UI level?

> "No. We should test behavior at the lowest practical layer and reserve UI tests for important end-to-end user journeys."

# SDET Interview Answer

> "In an automation framework, I would keep most business logic coverage at the unit and API levels because they are faster and easier to maintain. I would use Selenium or Playwright primarily for critical end-to-end workflows. This gives the CI pipeline fast feedback while still validating important real user journeys."

# Quick Revision

```text
Test Pyramid

Bottom -> Many Unit Tests
Middle -> Fewer Integration/API Tests
Top    -> Few UI/E2E Tests

Goal:
Fast feedback
Good coverage
Lower maintenance
Less flakiness
Lower execution cost

Key principle:
Test behavior at the lowest practical level.
```