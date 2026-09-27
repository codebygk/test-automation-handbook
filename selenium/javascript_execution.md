# JavaScript Execution

Selenium provides `execute_script()` to execute JavaScript inside the browser.

```python
driver.execute_script("javascript_code")
```

It is useful when normal Selenium operations are not sufficient or when you need to interact with the browser DOM directly.

## Basic Example

```python
driver.execute_script("alert('Hello')")
```

This executes JavaScript in the current page.

## Execute JavaScript on an Element

Pass a Selenium WebElement as an argument:

```python
element = driver.find_element(By.ID, "username")

driver.execute_script(
    "arguments[0].value = 'Gopalakrishnan';",
    element
)
```

Here:

```text
arguments[0] -> first argument passed to execute_script()
```

Multiple arguments are also possible:

```python
driver.execute_script(
    "arguments[0].value = arguments[1];",
    element,
    "Gopalakrishnan"
)
```

## Scroll

Scroll to an element:

```python
driver.execute_script(
    "arguments[0].scrollIntoView();",
    element
)
```

Scroll to the bottom:

```python
driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);"
)
```

Scroll by a specific amount:

```python
driver.execute_script(
    "window.scrollBy(0, 500);"
)
```

## Get Page Information

Get the page title:

```python
title = driver.execute_script("return document.title;")
```

Get the current URL:

```python
url = driver.execute_script("return window.location.href;")
```

Get document height:

```python
height = driver.execute_script(
    "return document.body.scrollHeight;"
)
```

## Return Values

JavaScript executed through Selenium can return a value.

```python
result = driver.execute_script(
    "return 10 + 20;"
)

print(result)
```

Output:

```text
30
```

Example:

```python
text = driver.execute_script(
    "return arguments[0].innerText;",
    element
)
```

## Click Using JavaScript

You can trigger a click:

```python
driver.execute_script(
    "arguments[0].click();",
    element
)
```

However, don't use JavaScript click as the default replacement for:

```python
element.click()
```

Prefer the normal Selenium interaction first.

JavaScript click bypasses some of the normal user-interaction behavior and can hide real UI problems.

## Modify CSS

Example:

```python
driver.execute_script(
    "arguments[0].style.border='3px solid red';",
    element
)
```

Useful for debugging or highlighting elements.

## Modify DOM

JavaScript can directly manipulate the DOM:

```python
driver.execute_script(
    "arguments[0].setAttribute('data-test', 'value');",
    element
)
```

This can be useful for debugging, but modifying application state through JavaScript can make a test less representative of a real user's interaction.

## JavaScriptExecutor vs Selenium API

Python Selenium does not have a separate `JavaScriptExecutor` class like some Java examples.

You use:

```python
driver.execute_script()
```

Example:

```python
driver.execute_script(
    "arguments[0].click();",
    element
)
```

## `execute_script()` vs `execute_async_script()`

### execute_script()

For synchronous JavaScript:

```python
result = driver.execute_script(
    "return document.title;"
)
```

The script completes before Selenium continues.

### execute_async_script()

For asynchronous JavaScript:

```python
result = driver.execute_async_script("""
    const callback = arguments[arguments.length - 1];

    setTimeout(() => {
        callback("Done");
    }, 1000);
""")
```

The last argument supplied by Selenium is a callback.

Selenium waits for that callback to be invoked.

## Common Use Cases

```text
execute_script()
    |
    +-- Scroll
    +-- Read DOM properties
    +-- Execute JavaScript events
    +-- Interact with difficult elements
    +-- Retrieve browser/page information
    +-- Debug/highlight elements
    +-- Perform browser-side operations
```

## When Should You Use It?

Prefer normal Selenium APIs first:

```python
element.click()
element.send_keys("Hello")
driver.execute_script(...)
```

Use JavaScript when:

- Selenium's normal API cannot perform the required operation
- You need browser/DOM information
- You need custom browser-side logic
- You need a specific DOM operation

Avoid using JavaScript to bypass every Selenium interaction problem.

For example, if an element cannot be clicked because another element is covering it, blindly doing:

```python
driver.execute_script(
    "arguments[0].click();",
    element
)
```

may hide a genuine application or synchronization problem.

Instead, investigate the actual issue and use appropriate waits or scrolling.

## Important Interview Question

### Can JavaScriptExecutor interact with elements?

Yes.

In Python Selenium:

```python
driver.execute_script(
    "arguments[0].click();",
    element
)
```

The Selenium WebElement is passed into JavaScript as an argument.

### Why do we use `arguments[0]`?

Because Selenium passes the WebElement as a JavaScript argument:

```python
driver.execute_script(
    "arguments[0].click();",
    element
)
```

Conceptually:

```text
Python element
      |
      v
arguments[0]
      |
      v
JavaScript element
```

## Framework Helper

You can encapsulate common JavaScript operations:

```python
class JavaScriptHelper:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_element(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            element
        )

    def click(self, element):
        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def get_page_height(self):
        return self.driver.execute_script(
            "return document.body.scrollHeight;"
        )
```

## Interview Answer

> "Selenium Python provides `execute_script()` to execute JavaScript in the context of the current browser page. I use it when the standard Selenium API is not sufficient, for example for scrolling, retrieving DOM information, or performing specific browser-side operations. I prefer normal Selenium interactions such as `click()` and `send_keys()` whenever possible because they better represent real user interactions."

## Quick Revision

```text
execute_script()       -> synchronous JavaScript
execute_async_script() -> asynchronous JavaScript
arguments[0]           -> first argument passed to JavaScript
return                 -> sends JavaScript result back to Python
```

Most important examples:

```python
driver.execute_script("return document.title;")
```

```python
driver.execute_script(
    "arguments[0].scrollIntoView();",
    element
)
```

```python
driver.execute_script(
    "arguments[0].click();",
    element
)
```