# JSON Handling

JSON stands for **JavaScript Object Notation**.

It is a lightweight text format commonly used for:

- REST APIs
- Configuration files
- Data exchange
- Test automation
- Storing structured data

Python provides the built-in `json` module for working with JSON.

## 1. Import the JSON Module

```python
import json
```

## 2. Python Object to JSON

Use `json.dumps()` to convert a Python object into a JSON string.

```python
import json

data = {
    "name": "John",
    "age": 30,
    "skills": ["Python", "Selenium"]
}

json_string = json.dumps(data)

print(json_string)
```

Output:

```text
{"name": "John", "age": 30, "skills": ["Python", "Selenium"]}
```

### `dumps()` Meaning

`dumps` means **dump to string**.

```python
json_string = json.dumps(data)
```

The result is a Python `str`.

```python
print(type(json_string))
# <class 'str'>
```

## 3. JSON to Python Object

Use `json.loads()` to convert a JSON string into a Python object.

```python
import json

json_string = '''
{
    "name": "John",
    "age": 30,
    "skills": ["Python", "Selenium"]
}
'''

data = json.loads(json_string)

print(data)
print(data["name"])
print(data["skills"])
```

Output:

```text
{'name': 'John', 'age': 30, 'skills': ['Python', 'Selenium']}
```

### `loads()` Meaning

`loads` means **load from string**.

```python
data = json.loads(json_string)
```

## 4. `dump()` and `load()`

The difference between `dumps()` and `dump()` is that `dump()` writes JSON to a file.

### Write JSON to a File

```python
import json

data = {
    "name": "John",
    "age": 30,
    "skills": ["Python", "Selenium"]
}

with open("user.json", "w") as file:
    json.dump(data, file, indent=4)
```

`user.json`:

```json
{
    "name": "John",
    "age": 30,
    "skills": [
        "Python",
        "Selenium"
    ]
}
```

### Read JSON from a File

```python
import json

with open("user.json", "r") as file:
    data = json.load(file)

print(data["name"])
# John
```

## 5. `dump()` vs `dumps()`

| Function       | Purpose                | Input                | Output         |
| -------------- | ---------------------- | -------------------- | -------------- |
| `json.dump()`  | Write JSON to a file   | Python object + file | Writes to file |
| `json.dumps()` | Convert to JSON string | Python object        | JSON string    |
| `json.load()`  | Read JSON from a file  | File                 | Python object  |
| `json.loads()` | Convert JSON string    | JSON string          | Python object  |

### Easy Memory Trick

```text
dump  - File
dumps - String

load  - File
loads - String
```

## 6. Python to JSON Data Type Mapping

| Python  | JSON    |
| ------- | ------- |
| `dict`  | Object  |
| `list`  | Array   |
| `tuple` | Array   |
| `str`   | String  |
| `int`   | Number  |
| `float` | Number  |
| `True`  | `true`  |
| `False` | `false` |
| `None`  | `null`  |

Example:

```python
import json

data = {
    "name": "John",
    "age": 30,
    "active": True,
    "address": None,
    "skills": ("Python", "Java")
}

json_string = json.dumps(data)

print(json_string)
```

Output:

```text
{"name": "John", "age": 30, "active": true, "address": null, "skills": ["Python", "Java"]}
```

Notice:

```text
True  -> true
False -> false
None  -> null
tuple -> array
```

## 7. Formatting JSON

### `indent`

Use `indent` to make JSON easier to read.

```python
import json

data = {
    "name": "John",
    "age": 30,
    "skills": ["Python", "Selenium"]
}

print(json.dumps(data, indent=4))
```

Output:

```json
{
    "name": "John",
    "age": 30,
    "skills": [
        "Python",
        "Selenium"
    ]
}
```

### `sort_keys`

Sort dictionary keys alphabetically.

```python
print(json.dumps(data, indent=4, sort_keys=True))
```

## 8. Handling JSON from REST APIs

JSON is very common when working with REST APIs.

Example response:

```json
{
    "id": 101,
    "name": "John",
    "email": "john@example.com"
}
```

Using `requests`:

```python
import requests

response = requests.get(
    "https://api.example.com/users/101",
    timeout=10
)

data = response.json()

print(data["name"])
print(data["email"])
```

`response.json()` parses the JSON response into a Python object.

## 9. JSON Validation and Exception Handling

Invalid JSON raises `json.JSONDecodeError`.

```python
import json

json_string = '{"name": "John",}'

try:
    data = json.loads(json_string)

except json.JSONDecodeError as e:
    print("Invalid JSON")
    print(e)
```

## 10. Accessing Nested JSON

Example:

```python
data = {
    "user": {
        "name": "John",
        "address": {
            "city": "Chennai",
            "country": "India"
        }
    }
}
```

Access nested values:

```python
city = data["user"]["address"]["city"]

print(city)
# Chennai
```

## 11. JSON Arrays

JSON arrays become Python lists.

```python
json_string = '''
{
    "users": [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"}
    ]
}
'''

data = json.loads(json_string)

for user in data["users"]:
    print(user["name"])
```

Output:

```text
John
Jane
```

## 12. JSON and Dictionary Are Not the Same

A Python dictionary:

```python
data = {
    "name": "John",
    "age": 30
}
```

A JSON string:

```python
data = '{"name": "John", "age": 30}'
```

The first is a Python `dict`.

The second is a Python `str` containing JSON data.

```python
print(type(data))
# <class 'str'>
```

Convert JSON string to dictionary:

```python
data = json.loads(data)

print(type(data))
# <class 'dict'>
```

## 13. Custom Python Objects

By default, `json.dumps()` cannot directly serialize arbitrary custom objects.

```python
import json

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("John", 30)

json.dumps(user)
```

This raises:

```text
TypeError
```

One simple approach is to provide a serialization function.

```python
import json

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("John", 30)

json_string = json.dumps(
    user,
    default=lambda obj: obj.__dict__
)

print(json_string)
# {"name": "John", "age": 30}
```

## 14. JSON in Test Automation

JSON is commonly used for:

- API request payloads
- API response validation
- Test data
- Configuration
- Authentication data
- Parameterized tests
- Mock responses

Example API payload:

```python
payload = {
    "username": "john",
    "password": "secret"
}
```

Send it using `requests`:

```python
import requests

response = requests.post(
    "https://api.example.com/login",
    json=payload,
    timeout=10
)

data = response.json()

assert data["status"] == "success"
```

Using the `json` parameter allows `requests` to serialize the Python dictionary as JSON.

## 15. Common Interview Questions

### Q1. What is the difference between `json.loads()` and `json.load()`?

```text
json.loads() - JSON string to Python object
json.load()  - JSON file to Python object
```

### Q2. What is the difference between `json.dumps()` and `json.dump()`?

```text
json.dumps() - Python object to JSON string
json.dump()  - Python object to JSON file
```

### Q3. What exception is raised for invalid JSON?

```python
json.JSONDecodeError
```

Example:

```python
try:
    data = json.loads(invalid_json)

except json.JSONDecodeError:
    print("Invalid JSON")
```

### Q4. Is JSON a Python dictionary?

No.

JSON is a text-based data interchange format.

```python
data = {"name": "John"}

print(type(data))
# <class 'dict'>

json_data = json.dumps(data)

print(type(json_data))
# <class 'str'>
```

### Q5. What is the difference between `response.json()` and `json.loads()`?

```python
response.json()
```

Parses JSON content from an HTTP response.

```python
json.loads(json_string)
```

Parses a JSON string.

### Q6. How do you pretty-print JSON?

```python
print(json.dumps(data, indent=4))
```

## Interview Shortcut

```text
json.dumps() - Python object to JSON string
json.loads() - JSON string to Python object

json.dump()  - Python object to JSON file
json.load()  - JSON file to Python object

dict         - JSON object
list         - JSON array
str          - JSON string
True         - true
False        - false
None         - null

JSON parsing error - json.JSONDecodeError
```