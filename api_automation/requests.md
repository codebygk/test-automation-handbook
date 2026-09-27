# Requests

`requests` is a popular Python library for making HTTP requests and testing or consuming REST APIs.

```python
import requests

response = requests.get("https://api.example.com/users")
```

## Why use Requests?

- Send HTTP requests
- Work with REST APIs
- Send query parameters, headers, cookies, and request bodies
- Handle authentication
- Validate status codes and responses
- Upload/download files
- Set timeouts
- Build API automation tests

---

# Basic Request

```python
import requests

response = requests.get("https://api.example.com/users")

print(response.status_code)
print(response.text)
```

Common methods:

```python
requests.get(url)
requests.post(url)
requests.put(url)
requests.patch(url)
requests.delete(url)
requests.head(url)
requests.options(url)
```

---

# Response Object

A request returns a `Response` object.

```python
response = requests.get(url)
```

Common properties:

```python
response.status_code
response.text
response.content
response.json()
response.headers
response.cookies
response.url
response.request
```

Example:

```python
response = requests.get("https://api.example.com/users/1")

print(response.status_code)
print(response.json())
print(response.headers)
```

## Important distinction

```python
response.text
```

Returns the response body as decoded text.

```python
response.content
```

Returns raw bytes.

```python
response.json()
```

Parses a JSON response into Python objects.

For example:

```json
{
    "id": 101,
    "name": "John"
}
```

becomes:

```python
{
    "id": 101,
    "name": "John"
}
```

---

# Query Parameters

Use `params`.

```python
params = {
    "page": 2,
    "limit": 10
}

response = requests.get(
    "https://api.example.com/users",
    params=params
)
```

Requests generates:

```text
/users?page=2&limit=10
```

Prefer `params` over manually constructing query strings.

---

# Headers

Use `headers`.

```python
headers = {
    "Authorization": "Bearer <token>",
    "Accept": "application/json"
}

response = requests.get(
    "https://api.example.com/users",
    headers=headers
)
```

Common headers:

```text
Authorization
Content-Type
Accept
User-Agent
Cookie
```

---

# JSON Request Body

Use `json`.

```python
payload = {
    "name": "John",
    "email": "john@example.com"
}

response = requests.post(
    "https://api.example.com/users",
    json=payload
)
```

Requests serializes the Python dictionary to JSON.

This is preferable to manually doing:

```python
data=json.dumps(payload)
```

when the API expects JSON.

---

# Form Data

Use `data`.

```python
payload = {
    "username": "admin",
    "password": "secret"
}

response = requests.post(
    "https://example.com/login",
    data=payload
)
```

The distinction is important:

| Parameter | Typical Use                   |
| --------- | ----------------------------- |
| `params`  | URL query parameters          |
| `json`    | JSON request body             |
| `data`    | Form data or raw request body |
| `headers` | HTTP headers                  |
| `cookies` | Cookies                       |
| `files`   | File upload                   |

---

# Authentication

## Basic Authentication

```python
from requests.auth import HTTPBasicAuth

response = requests.get(
    "https://api.example.com/users",
    auth=HTTPBasicAuth("admin", "password")
)
```

Short form:

```python
response = requests.get(
    url,
    auth=("admin", "password")
)
```

## Bearer Token

```python
headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(url, headers=headers)
```

## API Key

Depending on the API:

```python
headers = {
    "X-API-Key": api_key
}

response = requests.get(url, headers=headers)
```

---

# Status Code Validation

You can manually check:

```python
if response.status_code == 200:
    print("Success")
```

Better:

```python
response.raise_for_status()
```

Example:

```python
response = requests.get(url)

response.raise_for_status()

data = response.json()
```

`raise_for_status()` raises:

- `HTTPError` for 4xx and 5xx responses
- Nothing for successful responses

Important:

```python
response.raise_for_status()
```

does not validate whether the response body contains the expected business data.

You still need assertions.

```python
response.raise_for_status()

assert response.json()["status"] == "active"
```

---

# Timeout

Always consider specifying a timeout.

```python
response = requests.get(
    url,
    timeout=10
)
```

You can specify connection and read timeouts separately:

```python
response = requests.get(
    url,
    timeout=(5, 30)
)
```

Meaning:

```text
5 seconds  -> connection timeout
30 seconds -> read timeout
```

Without an appropriate timeout, a request can potentially wait indefinitely.

---

# Exception Handling

Common exceptions:

```python
import requests

try:
    response = requests.get(
        url,
        timeout=10
    )

    response.raise_for_status()

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.ConnectionError:
    print("Connection failed")

except requests.exceptions.HTTPError:
    print("HTTP error")

except requests.exceptions.RequestException:
    print("Request failed")
```

Hierarchy:

```text
RequestException
|
+-- ConnectionError
|
+-- Timeout
|
+-- HTTPError
|
+-- ...
```

---

# POST Example

```python
import requests

payload = {
    "username": "admin",
    "email": "admin@example.com"
}

response = requests.post(
    "https://api.example.com/users",
    json=payload,
    timeout=10
)

response.raise_for_status()

print(response.status_code)
print(response.json())
```

---

# PUT Example

```python
payload = {
    "name": "John",
    "email": "john@example.com"
}

response = requests.put(
    "https://api.example.com/users/101",
    json=payload,
    timeout=10
)

response.raise_for_status()
```

---

# PATCH Example

```python
payload = {
    "email": "new@example.com"
}

response = requests.patch(
    "https://api.example.com/users/101",
    json=payload,
    timeout=10
)
```

---

# DELETE Example

```python
response = requests.delete(
    "https://api.example.com/users/101",
    timeout=10
)

response.raise_for_status()
```

A successful DELETE might return:

```text
204 No Content
```

So don't blindly call:

```python
response.json()
```

when there may be no response body.

---

# Cookies

Send cookies:

```python
cookies = {
    "session_id": "abc123"
}

response = requests.get(
    url,
    cookies=cookies
)
```

Read cookies:

```python
print(response.cookies)
```

---

# Sessions

`requests.Session()` allows you to maintain state across multiple requests.

```python
session = requests.Session()

session.headers.update({
    "Authorization": f"Bearer {token}"
})

response1 = session.get(url1)
response2 = session.get(url2)
```

A session can persist:

- Cookies
- Headers
- Authentication configuration
- Connection pooling

For API automation, sessions are useful when multiple requests belong to the same user/session.

---

# Session Example

```python
import requests

session = requests.Session()

login_response = session.post(
    "https://api.example.com/login",
    json={
        "username": "admin",
        "password": "secret"
    },
    timeout=10
)

login_response.raise_for_status()

response = session.get(
    "https://api.example.com/profile",
    timeout=10
)

print(response.json())
```

If the server sets a session cookie during login, the session can automatically send it on subsequent requests.

---

# File Upload

```python
files = {
    "file": open("report.pdf", "rb")
}

response = requests.post(
    upload_url,
    files=files,
    timeout=30
)
```

Better resource handling:

```python
with open("report.pdf", "rb") as file:
    response = requests.post(
        upload_url,
        files={"file": file},
        timeout=30
    )
```

---

# File Download

```python
response = requests.get(
    download_url,
    timeout=30
)

response.raise_for_status()

with open("report.pdf", "wb") as file:
    file.write(response.content)
```

For large files, use streaming:

```python
with requests.get(
    download_url,
    stream=True,
    timeout=30
) as response:

    response.raise_for_status()

    with open("report.pdf", "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
```

---

# Request vs Response

A useful interview distinction:

```text
Request
|
+-- Method
+-- URL
+-- Headers
+-- Query parameters
+-- Body
+-- Cookies

Response
|
+-- Status code
+-- Headers
+-- Body
+-- Cookies
```

Example:

```python
response = requests.post(
    url,
    params={"source": "test"},
    headers={"Authorization": "Bearer token"},
    json={"name": "John"},
    cookies={"session": "abc"},
    timeout=10
)
```

---

# Inspecting the Request

The `Response` object contains the prepared request:

```python
response.request.method
response.request.url
response.request.headers
response.request.body
```

Useful for API debugging.

Example:

```python
print(response.request.method)
print(response.request.url)
print(response.request.headers)
print(response.request.body)
```

---

# Requests + Pytest

A typical API automation test:

```python
import requests

def test_get_user():
    response = requests.get(
        "https://api.example.com/users/101",
        timeout=10
    )

    assert response.status_code == 200

    body = response.json()

    assert body["id"] == 101
    assert body["name"] == "John"
```

Better framework structure:

```text
tests/
    test_users.py

api/
    users_api.py

utils/
    auth.py
    config.py
```

API client:

```python
class UsersAPI:

    def __init__(self, session):
        self.session = session

    def get_user(self, user_id):
        return self.session.get(
            f"/users/{user_id}",
            timeout=10
        )

    def create_user(self, payload):
        return self.session.post(
            "/users",
            json=payload,
            timeout=10
        )
```

Test:

```python
def test_get_user(users_api):
    response = users_api.get_user(101)

    assert response.status_code == 200
```

This separates:

```text
Test
  |
  v
API Client
  |
  v
Requests
  |
  v
HTTP API
```

---

# Requests vs Selenium

| Requests                         | Selenium                          |
| -------------------------------- | --------------------------------- |
| API testing                      | UI/browser testing                |
| HTTP level                       | Browser level                     |
| No browser required              | Requires browser                  |
| Faster                           | Slower                            |
| Tests endpoints directly         | Tests user interactions           |
| Can validate JSON/status/headers | Can validate rendered UI          |
| Good for API automation          | Good for end-to-end UI automation |

A strong automation framework often uses both.

```text
API layer
    |
    +-- requests

UI layer
    |
    +-- Selenium / Playwright
```

---

# Requests vs urllib

| Requests                 | urllib                            |
| ------------------------ | --------------------------------- |
| Third-party library      | Python standard library           |
| Simple API               | More verbose                      |
| Convenient JSON support  | More manual handling              |
| Easy sessions/auth       | More manual                       |
| Common in API automation | Useful when avoiding dependencies |

Interview answer:

> "Requests is a third-party Python HTTP library that provides a simple interface for sending HTTP requests and handling responses."

---

# Common Interview Questions

### 1. What is the Requests library?

> Requests is a Python HTTP client library used to send HTTP requests and consume APIs. It simplifies handling methods, headers, parameters, authentication, JSON, cookies, sessions, and responses.

### 2. Difference between `params`, `data`, and `json`?

```text
params -> URL query parameters
data   -> form data or raw request body
json   -> JSON request body
```

### 3. What does `raise_for_status()` do?

> It raises an HTTPError when the response status code represents a 4xx or 5xx error.

### 4. Why use `timeout`?

> To prevent a request from waiting indefinitely for a connection or response.

### 5. What is `requests.Session()`?

> A Session maintains state such as cookies and common headers across multiple requests and can reuse connections.

### 6. How do you send a JWT?

```python
headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(
    url,
    headers=headers,
    timeout=10
)
```

### 7. How do you send JSON?

```python
requests.post(
    url,
    json=payload
)
```

### 8. How do you validate an API response?

```python
response.raise_for_status()

assert response.status_code == 200

body = response.json()

assert body["status"] == "success"
```

### 9. How do you handle API failures?

> Use status code validation, `raise_for_status()`, appropriate timeouts, exception handling, logging, and controlled retries where retrying is safe.

### 10. Why shouldn't you use `time.sleep()` for API synchronization?

> API automation should generally wait based on actual conditions or retry policies rather than blindly sleeping for a fixed duration.

# Quick Revision

```text
requests.get()       -> GET
requests.post()      -> POST
requests.put()       -> PUT
requests.patch()     -> PATCH
requests.delete()    -> DELETE

params=              -> Query parameters
json=                -> JSON body
data=                -> Form/raw body
headers=             -> HTTP headers
cookies=             -> Cookies
files=               -> File upload
auth=                -> Authentication
timeout=             -> Request timeout

response.status_code -> Status
response.text        -> Text body
response.content     -> Bytes
response.json()      -> Parsed JSON
response.headers     -> Response headers
response.cookies     -> Response cookies

raise_for_status()   -> Raise HTTP error
Session()            -> Maintain state/reuse connections
```

## Most important for an API automation interview

1. HTTP methods
2. Status codes
3. `params` vs `data` vs `json`
4. Headers and authentication
5. JWT/Bearer authentication
6. `raise_for_status()`
7. Timeouts and exception handling
8. Sessions
9. Request/response validation
10. Building an API client with Requests + Pytest