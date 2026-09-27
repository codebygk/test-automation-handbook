# Handling Alerts

## 1. Definition

Browser alerts are JavaScript dialogs that appear on a web page.

Selenium handles them using the `Alert` interface through:

```python
driver.switch_to.alert
```

It can also handled by explicit construction.

```python
from selenium.webdriver.common.alert import Alert

alert = Alert(driver)
alert.accept()
```

Common JavaScript dialogs:

- Alert
- Confirmation
- Prompt

## 2. Simple Alert

An alert displays a message and usually has an **OK** button.

```javascript
alert("Login successful");
```

Handle it:

```python
alert = driver.switch_to.alert

print(alert.text)

alert.accept()
```

### Flow

```text
Web Page
   |
   v
JavaScript Alert
   |
   v
switch_to.alert
   |
   +-- text
   |
   +-- accept()
   |
   +-- dismiss()
```

## 3. Accept Alert

Click the OK button:

```python
driver.switch_to.alert.accept()
```

Equivalent:

```python
alert = driver.switch_to.alert
alert.accept()
```

## 4. Dismiss Alert

Click the Cancel button:

```python
driver.switch_to.alert.dismiss()
```

This is commonly used with confirmation dialogs.

## 5. Get Alert Text

```python
alert = driver.switch_to.alert

message = alert.text

print(message)
```

Useful for validating the message displayed by the application.

## 6. Confirmation Alert

A confirmation dialog usually has:

```text
Are you sure you want to delete this record?

[OK]    [Cancel]
```

### Accept

```python
driver.switch_to.alert.accept()
```

### Cancel

```python
driver.switch_to.alert.dismiss()
```

## 7. Prompt Alert

A prompt allows the user to enter text.

```javascript
prompt("Enter your name:");
```

Handle it:

```python
alert = driver.switch_to.alert

alert.send_keys("Gopalakrishnan")
alert.accept()
```

To cancel:

```python
alert.dismiss()
```

## 8. Alert Methods

| Method / Property   | Purpose                |
| ------------------- | ---------------------- |
| `switch_to.alert`   | Switch to active alert |
| `alert.text`        | Get alert message      |
| `alert.accept()`    | Click OK               |
| `alert.dismiss()`   | Click Cancel           |
| `alert.send_keys()` | Enter text into prompt |

## 9. Waiting for an Alert

If the alert appears asynchronously, use an explicit wait.

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)

alert = wait.until(
    EC.alert_is_present()
)

print(alert.text)

alert.accept()
```

This is preferable to:

```python
time.sleep(5)
```

because Selenium continues as soon as the alert appears.

## 10. Handling No Alert

If you try:

```python
driver.switch_to.alert
```

when no alert is present, Selenium raises:

```text
NoAlertPresentException
```

You can handle it when necessary:

```python
from selenium.common.exceptions import NoAlertPresentException

try:
    alert = driver.switch_to.alert
    alert.accept()
except NoAlertPresentException:
    print("No alert present")
```

However, if the alert is expected, an explicit wait is usually better than catching the exception immediately.

## 11. Important Distinction

JavaScript alerts are different from HTML modal dialogs.

### JavaScript Alert

```text
+----------------------+
| Are you sure?        |
|                      |
|     [OK] [Cancel]    |
+----------------------+
```

Use:

```python
driver.switch_to.alert
```

### HTML Modal

```html
<div class="modal">
    <button>Confirm</button>
</div>
```

This is a normal DOM element.

Use a normal locator:

```python
driver.find_element(
    By.CSS_SELECTOR,
    ".modal button"
).click()
```

Do **not** use `switch_to.alert` for HTML modals.

## 12. Alert vs Window vs Frame

| Object           | Selenium handling      |
| ---------------- | ---------------------- |
| JavaScript Alert | `switch_to.alert`      |
| New Window/Tab   | `switch_to.window()`   |
| iframe           | `switch_to.frame()`    |
| HTML Modal       | Normal element locator |

This distinction is commonly asked in interviews.

## 13. Framework Example

A reusable alert helper can centralize alert handling:

```python
class AlertHelper:

    def __init__(self, driver):
        self.driver = driver

    def accept(self):
        self.driver.switch_to.alert.accept()

    def dismiss(self):
        self.driver.switch_to.alert.dismiss()

    def get_text(self):
        return self.driver.switch_to.alert.text

    def enter_text(self, text):
        self.driver.switch_to.alert.send_keys(text)
```

Usage:

```python
alerts = AlertHelper(driver)

message = alerts.get_text()

assert message == "Are you sure?"

alerts.accept()
```

## 14. Common Interview Questions

**Q1. How do you handle a JavaScript alert?**

```python
alert = driver.switch_to.alert
alert.accept()
```

**Q2. How do you get alert text?**

```python
driver.switch_to.alert.text
```

**Q3. How do you click Cancel?**

```python
driver.switch_to.alert.dismiss()
```

**Q4. How do you enter text into a prompt?**

```python
alert = driver.switch_to.alert
alert.send_keys("Hello")
alert.accept()
```

**Q5. How do you wait for an alert?**

```python
wait.until(EC.alert_is_present())
```

**Q6. What exception occurs when there is no alert?**

```text
NoAlertPresentException
```

**Q7. Can you use `find_element()` to handle a JavaScript alert?**

No. A JavaScript alert is not a DOM element. Use:

```python
driver.switch_to.alert
```

## 15. Interview Answer

"JavaScript alerts in Selenium are handled using `driver.switch_to.alert`. I can use `alert.text` to retrieve the message, `accept()` to click OK, `dismiss()` to click Cancel, and `send_keys()` for prompt dialogs. If the alert appears asynchronously, I use an explicit wait with `EC.alert_is_present()`. HTML modals are different because they are DOM elements and should be handled using normal locators."