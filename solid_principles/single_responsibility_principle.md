# Single Responsibility Principle (SRP)

## Definition

The **Single Responsibility Principle** states that a class should have only one reason to change.

Each class should have one clearly defined responsibility.

SRP is the first principle of **SOLID**.

## 1. Example: Violating SRP

```python
class TestAutomation:

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(
            "id", "username"
        ).send_keys(username)

        self.driver.find_element(
            "id", "password"
        ).send_keys(password)

    def save_result(self, result):
        with open("results.txt", "a") as file:
            file.write(result)

    def send_email(self, result):
        print(f"Sending email: {result}")
```

### Problems

This class has three unrelated responsibilities:

- UI automation
- Saving test results
- Sending email notifications

Changes to the UI, reporting format or email service could all require modifying the same class.

This violates SRP.

---

## 2. Applying SRP

Separate the responsibilities into dedicated classes.

```python
class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(
            "id", "username"
        ).send_keys(username)

        self.driver.find_element(
            "id", "password"
        ).send_keys(password)


class ResultRepository:

    def save(self, result):
        with open("results.txt", "a") as file:
            file.write(result)


class EmailNotifier:

    def send(self, result):
        print(f"Sending email: {result}")
```

Each class now has one primary responsibility.

```python
login_page = LoginPage(driver)
repository = ResultRepository()
notifier = EmailNotifier()

login_page.login("admin", "password")

repository.save("PASS\n")
notifier.send("Test completed")
```

### Benefits

- Easier maintenance
- Better testability
- Reduced coupling
- Improved reusability
- Easier debugging
- Smaller, more focused classes

---

## 3. SRP in Automation Frameworks

A typical automation framework can separate responsibilities as follows:

| Class | Responsibility |
|---|---|
| DriverFactory | Create browser drivers |
| BrowserActions | Perform browser interactions |
| WaitHelper | Handle synchronization |
| LoginPage | Handle login page interactions |
| APIClient | Handle API requests |
| ConfigManager | Manage configuration |
| ResultRepository | Store test results |
| EmailNotifier | Send notifications |

For example, `LoginPage` should not be responsible for generating reports or sending emails.

Similarly, `BrowserActions` should not contain application-specific business workflows.

---

## 4. One Responsibility vs One Method

SRP does not mean that a class should contain only one method.

A class can have multiple methods if they all serve the same responsibility.

```python
class BrowserActions:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def type(self, locator, text):
        self.driver.find_element(
            *locator
        ).send_keys(text)

    def get_text(self, locator):
        return self.driver.find_element(
            *locator
        ).text
```

All three methods serve the same responsibility: browser interactions.

This is consistent with SRP.

---

## 5. How to Identify SRP Violations

Ask these questions:

- Does this class handle multiple unrelated responsibilities?
- Can different requirements cause independent changes to this class?
- Does the class contain unrelated groups of methods?
- Does it depend on too many unrelated services?
- Is it difficult to test one behavior without setting up unrelated dependencies?

If several independent reasons to change exist, consider extracting separate classes.

However, avoid splitting closely related functionality into unnecessary tiny classes.

---

## 6. SRP vs Separation of Concerns

| SRP | Separation of Concerns |
|---|---|
| Focuses on one reason to change | Separates distinct concerns |
| Primarily a class/module design principle | Applies across the entire system |
| Promotes cohesive classes | Promotes clear architectural boundaries |
| Example: separate reporting from browser actions | Example: separate tests, pages and infrastructure |

SRP is one way to achieve separation of concerns.

---

## 7. Common Interview Questions

### What is SRP?

SRP states that a class or module should have only one reason to change.

### Does SRP mean one method per class?

No. A class can have multiple methods as long as they support one cohesive responsibility.

### How do you apply SRP in automation?

I separate driver management, browser interactions, Page Objects, API operations, reporting and configuration into dedicated components.

### What happens when SRP is violated?

Classes become harder to maintain, test and reuse. Changes to one responsibility may unintentionally affect unrelated functionality.

### Can SRP lead to too many classes?

Yes. Excessive splitting can introduce unnecessary complexity. Classes should be separated according to meaningful responsibilities, not simply their number of methods.

### How is SRP related to cohesion?

SRP encourages high cohesion because the methods and data within a class serve one clearly defined purpose.

---

## Interview Answer

> "The Single Responsibility Principle states that a class should have only one reason to change. In an automation framework, I apply SRP by separating driver management, browser interactions, Page Objects, reporting and configuration into dedicated classes. For example, a LoginPage should handle login-related interactions, not generate reports or manage browser initialization. This improves maintainability, testability and reusability while reducing the risk of unrelated changes affecting each other."

**Key takeaway:** One class, one cohesive responsibility, one reason to change.