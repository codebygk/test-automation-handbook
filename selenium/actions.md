# Actions

Selenium's **Actions** is used to perform advanced user interactions such as:

- Mouse actions
- Keyboard actions
- Drag and drop
- Hover
- Right click
- Double click
- Click and hold
- Keyboard shortcuts
- Composite action sequences

In Python, it is provided through:

```python
from selenium.webdriver.common.action_chains import ActionChains
```

## Basic Syntax

```python
actions = ActionChains(driver)

actions.move_to_element(element).click().perform()
```

`ActionChains` builds a sequence of actions.

`perform()` executes the action sequence.

---

# Mouse Actions

## Click

For a normal click, you usually don't need Actions API:

```python
element.click()
```

But you can use:

```python
ActionChains(driver) \
    .click(element) \
    .perform()
```

## Double Click

```python
ActionChains(driver) \
    .double_click(element) \
    .perform()
```

## Right Click

```python
ActionChains(driver) \
    .context_click(element) \
    .perform()
```

## Mouse Hover

```python
ActionChains(driver) \
    .move_to_element(element) \
    .perform()
```

Useful for:

- Menus
- Tooltips
- Hover-based dropdowns
- Dynamic UI elements

## Click and Hold

```python
ActionChains(driver) \
    .click_and_hold(element) \
    .perform()
```

Release:

```python
ActionChains(driver).release().perform()
```

---

# Drag and Drop

### Using Elements

```python
source = driver.find_element(By.ID, "source")
target = driver.find_element(By.ID, "target")

ActionChains(driver) \
    .drag_and_drop(source, target) \
    .perform()
```

### Using Coordinates

```python
ActionChains(driver) \
    .click_and_hold(source) \
    .move_to_element(target) \
    .release() \
    .perform()
```

The second approach can sometimes be useful when the application's drag-and-drop implementation does not respond correctly to the higher-level `drag_and_drop()` method.

---

# Keyboard Actions

You can use keyboard keys through `Keys`.

```python
from selenium.webdriver.common.keys import Keys
```

Example:

```python
ActionChains(driver) \
    .key_down(Keys.CONTROL) \
    .send_keys("a") \
    .key_up(Keys.CONTROL) \
    .perform()
```

This performs:

```text
Ctrl + A
```

## Copy and Paste

```python
ActionChains(driver) \
    .key_down(Keys.CONTROL) \
    .send_keys("a") \
    .send_keys("c") \
    .key_up(Keys.CONTROL) \
    .perform()
```

For Mac, use:

```python
Keys.COMMAND
```

instead of:

```python
Keys.CONTROL
```

---

# Send Keys to an Element

For normal text entry:

```python
element.send_keys("Gopalakrishnan")
```

You generally don't need `ActionChains`.

But Actions API is useful when the interaction involves keyboard combinations or a sequence of keyboard and mouse operations.

Example:

```python
ActionChains(driver) \
    .click(element) \
    .key_down(Keys.CONTROL) \
    .send_keys("a") \
    .key_up(Keys.CONTROL) \
    .send_keys("Hello") \
    .perform()
```

---

# Chaining Actions

One important feature is that actions can be chained.

```python
ActionChains(driver) \
    .move_to_element(menu) \
    .click() \
    .move_to_element(submenu) \
    .click() \
    .perform()
```

Conceptually:

```text
Move -> Click -> Move -> Click -> Perform
```

---

# `perform()` Is Important

This:

```python
ActionChains(driver).move_to_element(element)
```

builds the action sequence.

It does not necessarily execute the sequence immediately.

You normally finish with:

```python
.perform()
```

Example:

```python
actions = ActionChains(driver)

actions.move_to_element(element)
actions.click()

actions.perform()
```

---

# `click()` vs `ActionChains.click()`

Normal Selenium click:

```python
element.click()
```

Actions API:

```python
ActionChains(driver).click(element).perform()
```

Use normal `.click()` for ordinary element clicks.

Use Actions API when you need a more complex user interaction.

---

# Common Actions

| Action | Syntax |
|---|---|
| Click | `click()` |
| Double click | `double_click()` |
| Right click | `context_click()` |
| Hover | `move_to_element()` |
| Click and hold | `click_and_hold()` |
| Release | `release()` |
| Drag and drop | `drag_and_drop()` |
| Move by offset | `move_by_offset()` |
| Keyboard key down | `key_down()` |
| Keyboard key up | `key_up()` |
| Send keys | `send_keys()` |
| Execute sequence | `perform()` |

---

# Move by Offset

You can move the mouse relative to its current position:

```python
ActionChains(driver) \
    .move_by_offset(100, 50) \
    .perform()
```

This moves:

```text
X + 100
Y + 50
```

Coordinate-based interactions are generally more fragile than element-based interactions.

Prefer:

```python
move_to_element(element)
```

when possible.

---

# Example: Hover Menu

HTML:

```html
<div id="products">Products</div>
<div id="automation">Automation</div>
```

Automation:

```python
products = driver.find_element(By.ID, "products")
automation = driver.find_element(By.ID, "automation")

ActionChains(driver) \
    .move_to_element(products) \
    .move_to_element(automation) \
    .click() \
    .perform()
```

---

# Actions API vs Element API

| Requirement | Prefer |
|---|---|
| Enter text | `element.send_keys()` |
| Normal click | `element.click()` |
| Hover | `ActionChains` |
| Double click | `ActionChains` |
| Right click | `ActionChains` |
| Drag and drop | `ActionChains` |
| Ctrl+A | `ActionChains` |
| Complex mouse + keyboard sequence | `ActionChains` |

---

# Important Interview Concept

Selenium's Actions API is based on the **W3C WebDriver Actions specification**.

It allows automation of low-level user input such as:

```text
Mouse
Keyboard
Wheel
```

`ActionChains` provides a convenient Python API for constructing these interactions.

---

# Interview Answer

> "Selenium's Actions API is used for advanced user interactions that go beyond simple element operations. In Python, I use `ActionChains` for actions such as mouse hover, double click, right click, drag and drop, click and hold, and keyboard combinations. I build the action sequence using methods such as `move_to_element()`, `click()`, and `key_down()`, and execute it using `perform()`."

## Quick Revision

```text
ActionChains(driver)
        |
        +-- move_to_element()
        +-- click()
        +-- double_click()
        +-- context_click()
        +-- click_and_hold()
        +-- release()
        +-- drag_and_drop()
        +-- key_down()
        +-- key_up()
        +-- send_keys()
        +-- perform()
```

### Most important for interviews

```python
ActionChains(driver).move_to_element(element).perform()
```

```python
ActionChains(driver).double_click(element).perform()
```

```python
ActionChains(driver).context_click(element).perform()
```

```python
ActionChains(driver).drag_and_drop(source, target).perform()
```

```python
ActionChains(driver) \
    .key_down(Keys.CONTROL) \
    .send_keys("a") \
    .key_up(Keys.CONTROL) \
    .perform()
```