# Selenium WebDriver Architecture

## 1. Definition

Selenium WebDriver is a browser automation framework that allows test scripts to interact with web browsers programmatically.

It follows a **client-server architecture** and uses the **W3C WebDriver protocol** to communicate between Selenium client libraries and browser drivers.

## 2. Architecture Diagram

```text
+--------------------------------+
|          Test Script           |
|      Python / Java / C#        |
+--------------------------------+
               |
               | WebDriver API
               v
+--------------------------------+
|      Selenium Client Library   |
|                                |
|  Converts API calls into       |
|  WebDriver commands            |
+--------------------------------+
               |
               | HTTP + JSON
               | W3C WebDriver Protocol
               v
+--------------------------------+
|         Browser Driver         |
|                                |
| ChromeDriver / GeckoDriver     |
| EdgeDriver                     |
+--------------------------------+
               |
               | Browser-specific
               | automation commands
               v
+--------------------------------+
|            Browser             |
|                                |
| Chrome / Firefox / Edge        |
+--------------------------------+
               |
               v
+--------------------------------+
|        Web Application         |
+--------------------------------+
```

## 3. Main Components

| Component | Responsibility |
|---|---|
| Test Script | Contains automation steps and assertions |
| Selenium Client Library | Provides language-specific WebDriver APIs |
| W3C WebDriver Protocol | Standardizes communication using HTTP and JSON |
| Browser Driver | Translates WebDriver commands into browser-specific operations |
| Browser | Executes automation commands |
| Web Application | Application being tested |

### 1. Test Script

Contains the automation logic written in Python, Java, C# or another supported language.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://example.com")

heading = driver.find_element(By.TAG_NAME, "h1")

print(heading.text)

driver.quit()
```

### 2. Selenium Client Library

Provides APIs such as:

```python
driver.get(url)
driver.find_element(...)
element.click()
element.send_keys(...)
driver.quit()
```

It converts these method calls into standardized WebDriver commands and sends them to the browser driver.

### 3. W3C WebDriver Protocol

Defines standardized HTTP endpoints and JSON request/response formats for browser automation.

Examples:

| Operation | HTTP Method | Endpoint |
|---|---|---|
| Create session | POST | `/session` |
| Navigate | POST | `/session/{id}/url` |
| Find element | POST | `/session/{id}/element` |
| Click element | POST | `/session/{id}/element/{elementId}/click` |
| Delete session | DELETE | `/session/{id}` |

This standard allows different Selenium client libraries to communicate with different browser drivers.

### 4. Browser Driver

Acts as an intermediary between Selenium and the browser.

Examples:

- ChromeDriver - Google Chrome
- GeckoDriver - Mozilla Firefox
- EdgeDriver - Microsoft Edge

Its responsibilities include receiving WebDriver commands, controlling the browser and returning results or errors.

Modern Selenium includes Selenium Manager, which can automatically manage browser drivers when required.

## 4. How WebDriver Works

Consider:

```python
driver.get("https://example.com")
```

The execution flow is:

1. The test script calls `driver.get()`.
2. The Selenium client library creates a navigation command.
3. The command is sent as an HTTP request to the browser driver.
4. The browser driver instructs the browser to navigate to the URL.
5. The browser loads the page.
6. The browser driver returns the command result.
7. Selenium processes the response and returns control to the test script.

The same general request-response mechanism applies to element interactions and other traditional WebDriver commands.

## 5. Local vs Remote WebDriver

### Local Execution

```text
Test Script
    |
    v
Selenium Client
    |
    v
Browser Driver
    |
    v
Local Browser
```

Example:

```python
driver = webdriver.Chrome()
```

The browser and browser driver run on the local machine.

### Remote Execution

```text
Test Script
    |
    v
Selenium Client
    |
    v
Selenium Grid
    |
    v
Remote Node
    |
    v
Browser Driver
    |
    v
Remote Browser
```

Example:

```python
from selenium import webdriver

options = webdriver.ChromeOptions()

driver = webdriver.Remote(
    command_executor="http://localhost:4444",
    options=options
)
```

Selenium Grid allows tests to execute on remote machines, different browsers and different operating systems.

## 6. Selenium Grid Architecture

Selenium Grid 4 supports distributed browser execution.

```text
               Test Scripts
                    |
                    v
               +----------+
               |  Router  |
               +----------+
                    |
          +---------+---------+
          |                   |
          v                   v
    Session Queue        Session Map
          |
          v
     Distributor
          |
          v
       Event Bus
          |
    +-----+-----+
    |           |
    v           v
  Node 1      Node 2
    |           |
    v           v
  Chrome      Firefox
```

| Component | Responsibility |
|---|---|
| Router | Entry point for incoming WebDriver requests |
| Session Queue | Holds new session requests |
| Distributor | Assigns sessions to available Nodes |
| Session Map | Tracks which Node owns each session |
| Event Bus | Facilitates internal component communication |
| Node | Hosts browser instances and executes commands |

## 7. WebDriver BiDi

Traditional WebDriver primarily uses HTTP request-response communication.

WebDriver BiDi introduces bidirectional communication over WebSocket.

```text
Traditional WebDriver:

Client -- HTTP Request --> Browser
Client <-- HTTP Response -- Browser


WebDriver BiDi:

Client <==== WebSocket ====> Browser

Commands and browser events
```

WebDriver BiDi supports event-driven automation capabilities, including browser console messages and network events.

## 8. Common Interview Questions

**Q1. Does Selenium communicate directly with the browser?**

Traditional WebDriver commands are sent through a browser driver or remote WebDriver server rather than directly from the test script to the browser.

**Q2. What protocol does Selenium WebDriver use?**

The W3C WebDriver protocol, primarily using HTTP requests and JSON responses. WebDriver BiDi additionally uses WebSocket.

**Q3. What is the role of ChromeDriver?**

ChromeDriver implements the WebDriver protocol and translates automation commands into operations supported by Chrome.

**Q4. What happens when `driver.find_element()` is called?**

Selenium sends a Find Element command to the browser driver. The driver searches the current browsing context and returns an element reference or an error.

**Q5. What is the difference between Selenium WebDriver and Selenium Grid?**

WebDriver provides browser automation APIs and communication with browsers. Grid enables remote and distributed execution across multiple machines and browser configurations.

## 9. Interview Answer

"Selenium WebDriver follows a client-server architecture. A test script uses a language-specific Selenium client library, which converts WebDriver API calls into W3C WebDriver commands and sends them over HTTP to a browser driver.

The browser driver executes the commands in the browser and returns responses to the client library.

For remote and parallel execution, Selenium Grid routes commands to browser instances running on different Nodes. Modern Selenium also supports WebDriver BiDi for bidirectional, event-driven browser communication."