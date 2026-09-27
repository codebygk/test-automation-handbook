# Frames / iFrames

A frame is a separate browsing context embedded inside a web page.

An `<iframe>` is commonly used to embed another HTML document inside the current page.

Selenium cannot directly interact with elements inside a frame while it is still in the parent document.

You must first **switch into the frame**.

## Basic Syntax

```python
driver.switch_to.frame(frame_reference)
```

The frame can be identified in 3 ways:

1. Frame WebElement
2. Frame name or ID
3. Frame index

---

## 1. Using WebElement

This is generally the most flexible approach.

```python
frame = driver.find_element(By.ID, "payment-frame")

driver.switch_to.frame(frame)

driver.find_element(By.ID, "card-number").send_keys("1234")
```

---

## 2. Using Name or ID

If the iframe has a `name` or `id`:

```html
<iframe id="payment-frame" name="payment"></iframe>
```

You can do:

```python
driver.switch_to.frame("payment-frame")
```

or:

```python
driver.switch_to.frame("payment")
```

---

## 3. Using Index

You can switch using its position:

```python
driver.switch_to.frame(0)
```

This means the first frame.

However, index-based switching is generally fragile because adding or removing frames can change the index.

Prefer a stable ID, name, or WebElement.

---

# Switch Back

After working inside the frame, you can return to the parent document:

```python
driver.switch_to.parent_frame()
```

Example:

```python
driver.switch_to.frame("payment-frame")

driver.find_element(By.ID, "card-number").send_keys("1234")

driver.switch_to.parent_frame()
```

---

# Return to Main Document

If frames are nested, `parent_frame()` only moves up one level.

To return directly to the top-level page:

```python
driver.switch_to.default_content()
```

Example:

```text
Main Page
   |
   +-- Frame A
          |
          +-- Frame B
```

If currently inside Frame B:

```python
driver.switch_to.parent_frame()
```

moves to Frame A.

```python
driver.switch_to.default_content()
```

moves directly to the Main Page.

---

# Nested Frames

Frames can contain other frames.

Example:

```html
<iframe id="outer-frame">
    <iframe id="inner-frame"></iframe>
</iframe>
```

You must switch into them level by level:

```python
driver.switch_to.frame("outer-frame")
driver.switch_to.frame("inner-frame")

driver.find_element(By.ID, "username").send_keys("admin")
```

To move back one level:

```python
driver.switch_to.parent_frame()
```

To return to the main page:

```python
driver.switch_to.default_content()
```

---

# Waiting for a Frame

If the frame loads dynamically, use an explicit wait:

```python
wait = WebDriverWait(driver, 10)

wait.until(
    EC.frame_to_be_available_and_switch_to_it(
        (By.ID, "payment-frame")
    )
)

driver.find_element(By.ID, "card-number").send_keys("1234")
```

This is particularly useful in dynamic applications.

---

# Important Concept

Consider:

```text
Main Page
    |
    +-- iframe
          |
          +-- Login Form
```

This will not work directly:

```python
driver.find_element(By.ID, "username")
```

because Selenium is currently operating in the **main document**.

You need:

```python
driver.switch_to.frame("login-frame")

driver.find_element(By.ID, "username")
```

---

# Frame vs Window

This is a very common interview question.

| Concept | Frame / iframe | Window / Tab |
|---|---|---|
| Context | Embedded inside page | Separate browser context |
| Switch using | `switch_to.frame()` | `switch_to.window()` |
| Switch back | `parent_frame()` | `switch_to.window(handle)` |
| Return to main | `default_content()` | Switch to original handle |
| Identifier | Element, ID/name, index | Window handle |

### Easy way to remember

```text
iframe  -> switch_to.frame()
tab     -> switch_to.window()
```

---

# Common Mistake

This is wrong:

```python
driver.switch_to.frame("payment")
driver.switch_to.frame("payment")
```

unless there are actually nested frames with that reference.

Once you switch into a frame, Selenium's current context is that frame.

---

# Frame and WebElement Context

Suppose:

```html
<iframe id="login-frame">
    <input id="username">
</iframe>
```

Correct:

```python
frame = driver.find_element(By.ID, "login-frame")

driver.switch_to.frame(frame)

username = driver.find_element(By.ID, "username")
username.send_keys("admin")
```

Notice that the frame itself is located from the **parent document**.

Then the elements inside the frame are located after switching into it.

---

# Framework Helper

In an automation framework, you can encapsulate frame handling:

```python
class FrameHelper:

    def __init__(self, driver):
        self.driver = driver

    def switch_to_frame(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(locator)
        )

    def switch_to_parent(self):
        self.driver.switch_to.parent_frame()

    def switch_to_main(self):
        self.driver.switch_to.default_content()
```

Usage:

```python
frame_helper.switch_to_frame(
    (By.ID, "payment-frame")
)

driver.find_element(By.ID, "card-number").send_keys("1234")

frame_helper.switch_to_main()
```

---

# Common Exceptions

If you try to switch to a frame that does not exist:

```python
driver.switch_to.frame("invalid-frame")
```

you may get:

```text
NoSuchFrameException
```

If the frame exists but the content is not ready yet, an explicit wait is often appropriate:

```python
EC.frame_to_be_available_and_switch_to_it(...)
```

---

# Interview Questions

### How do you handle an iframe?

> "I first locate the iframe and switch into it using `driver.switch_to.frame()`. After interacting with its elements, I use `parent_frame()` to move to the immediate parent or `default_content()` to return to the main document."

### How many ways can you switch to a frame?

```python
driver.switch_to.frame(WebElement)
driver.switch_to.frame("frame_id_or_name")
driver.switch_to.frame(0)
```

### How do you return to the main page?

```python
driver.switch_to.default_content()
```

### Difference between `parent_frame()` and `default_content()`?

```text
parent_frame()     -> moves one level up
default_content()  -> moves directly to the main document
```

### Can Selenium interact with an iframe without switching to it?

Normally, no. You need to switch the driver's browsing context into that frame before locating and interacting with elements inside it.

# Quick Revision

```text
switch_to.frame()       -> enter frame
parent_frame()          -> go one level up
default_content()       -> go to main document
frame_to_be_available... -> wait + switch
NoSuchFrameException    -> frame cannot be found/accessed
```

The key interview concept is **browsing context**: Selenium must be in the correct document context before it can locate elements inside that context.