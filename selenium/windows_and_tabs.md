# Windows and Tabs

Selenium handles browser windows and tabs using **window handles**.

A window handle is a unique string that identifies a browser window or tab.

## Basic Concept

```python
driver.current_window_handle
```

Returns the handle of the currently active window.

```python
driver.window_handles
```

Returns a list of handles for all currently open windows/tabs.

Example:

```python
print(driver.current_window_handle)
print(driver.window_handles)
```

Output might look like:

```text
CDwindow-123
['CDwindow-123', 'CDwindow-456']
```

## Switching Windows/Tabs

Use:

```python
driver.switch_to.window(handle)
```

Example:

```python
handles = driver.window_handles

driver.switch_to.window(handles[1])
```

After switching, Selenium commands operate on that window/tab.

## Common Scenario

Suppose clicking a button opens a new tab:

```python
driver.get("https://example.com")

original_window = driver.current_window_handle

driver.find_element(By.ID, "open-tab").click()

WebDriverWait(driver, 10).until(
    lambda d: len(d.window_handles) > 1
)

for handle in driver.window_handles:
    if handle != original_window:
        driver.switch_to.window(handle)
        break
```

Now Selenium is controlling the new tab.

## Switch Back

Store the original handle:

```python
original_window = driver.current_window_handle
```

Then switch back:

```python
driver.switch_to.window(original_window)
```

## Close vs Quit

```python
driver.close()
```

Closes the **currently active window/tab**.

```python
driver.quit()
```

Closes **all browser windows/tabs** and ends the WebDriver session.

Example:

```python
original_window = driver.current_window_handle

driver.find_element(By.ID, "open-tab").click()

WebDriverWait(driver, 10).until(
    lambda d: len(d.window_handles) > 1
)

for handle in driver.window_handles:
    if handle != original_window:
        driver.switch_to.window(handle)
        break

# Work with new tab
print(driver.title)

# Close new tab
driver.close()

# Switch back to original
driver.switch_to.window(original_window)
```

## Important Interview Point

A Selenium window handle identifies both:

- Browser windows
- Browser tabs

Selenium does not fundamentally treat them as separate concepts when switching.

```python
driver.switch_to.window(handle)
```

works for both.

## Opening a New Tab

Selenium 4 provides:

```python
driver.switch_to.new_window("tab")
```

Example:

```python
driver.switch_to.new_window("tab")
driver.get("https://example.com")
```

## Opening a New Window

```python
driver.switch_to.new_window("window")
```

Example:

```python
driver.switch_to.new_window("window")
driver.get("https://example.com")
```

These methods create the new browsing context and switch Selenium to it.

## Window vs Tab

| Operation | Syntax |
|---|---|
| Current window/tab | `driver.current_window_handle` |
| All windows/tabs | `driver.window_handles` |
| Switch | `driver.switch_to.window(handle)` |
| New tab | `driver.switch_to.new_window("tab")` |
| New window | `driver.switch_to.new_window("window")` |
| Close current | `driver.close()` |
| Close everything | `driver.quit()` |

## Common Mistake

Do not assume:

```python
driver.window_handles[1]
```

will always be the newly opened tab.

Better:

```python
original = driver.current_window_handle

# Trigger new tab

WebDriverWait(driver, 10).until(
    lambda d: len(d.window_handles) > 1
)

new_window = next(
    handle for handle in driver.window_handles
    if handle != original
)

driver.switch_to.window(new_window)
```

This is more reliable.

## Multiple Windows

For multiple windows:

```python
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    print(driver.title)
```

If you need to identify a specific window, check something meaningful:

```python
for handle in driver.window_handles:
    driver.switch_to.window(handle)

    if "Payment" in driver.title:
        break
```

## Window Handle vs Window Size

Do not confuse:

```python
driver.window_handles
```

with window size operations.

Window handles identify browser contexts.

Window size is controlled using:

```python
driver.set_window_size(1200, 800)
```

## Framework Helper

In an automation framework, you can encapsulate this:

```python
class WindowHelper:

    def __init__(self, driver):
        self.driver = driver

    def get_current_window(self):
        return self.driver.current_window_handle

    def get_all_windows(self):
        return self.driver.window_handles

    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    def switch_to_new_window(self):
        current = self.driver.current_window_handle

        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.window_handles) > 1
        )

        new_window = next(
            handle for handle in self.driver.window_handles
            if handle != current
        )

        self.driver.switch_to.window(new_window)
```

## Interview Answer

> "Selenium identifies browser windows and tabs using unique window handles. `current_window_handle` returns the active handle, while `window_handles` returns all open handles. We use `driver.switch_to.window(handle)` to switch between them. `close()` closes the current tab or window, while `quit()` terminates the entire WebDriver session. Selenium 4 also provides `new_window('tab')` and `new_window('window')` for creating new browsing contexts."

## Key Things to Remember

```text
current_window_handle -> current window/tab
window_handles        -> all windows/tabs
switch_to.window()    -> switch
new_window("tab")     -> create tab
new_window("window")  -> create window
close()               -> close current
quit()                -> close everything
```

For interviews, the most important concepts are **window handles, switching, waiting for a new window, and close vs quit**.