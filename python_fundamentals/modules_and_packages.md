# Modules and Packages

A **module** is a Python file containing reusable code, such as functions, classes and variables.

A **package** is a collection of related modules organized under a directory.

## 1. Modules

A module allows code to be organized into separate files and reused across multiple programs.

### Creating a Module

Create a file named `calculator.py`.

```python
# calculator.py

PI = 3.14159

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

Import the module into another Python file.

```python
# main.py

import calculator

print(calculator.add(10, 20))
# 30

print(calculator.PI)
# 3.14159
```

## 2. Different Ways to Import Modules

### Import the Entire Module

```python
import math

print(math.sqrt(16))
# 4.0
```

### Import Specific Members

```python
from math import sqrt, pi

print(sqrt(25))
# 5.0

print(pi)
# 3.141592653589793
```

### Import with an Alias

```python
import math as m

print(m.sqrt(36))
# 6.0
```

### Import Specific Members with Aliases

```python
from math import sqrt as square_root

print(square_root(49))
# 7.0
```

### Import Everything

```python
from math import *

print(sqrt(64))
# 8.0
```

Avoid wildcard imports because they can cause naming conflicts and make code harder to maintain.

## 3. Packages

A package organizes related modules into directories.

### Example Package Structure

```text
project/
    main.py
    calculator/
        __init__.py
        addition.py
        subtraction.py
```

`addition.py`

```python
def add(a, b):
    return a + b
```

`subtraction.py`

```python
def subtract(a, b):
    return a - b
```

`main.py`

```python
from calculator.addition import add
from calculator.subtraction import subtract

print(add(10, 20))
# 30

print(subtract(20, 10))
# 10
```

## 4. The `__init__.py` File

The `__init__.py` file identifies a directory as a regular Python package.

It can also initialize the package and expose selected functions or classes.

Example:

```text
calculator/
    __init__.py
    addition.py
    subtraction.py
```

`__init__.py`

```python
from .addition import add
from .subtraction import subtract
```

Now the functions can be imported directly from the package.

```python
from calculator import add, subtract

print(add(10, 20))
# 30

print(subtract(20, 10))
# 10
```

**Important:** Since Python 3.3, namespace packages can exist without `__init__.py`. However, regular packages typically include it.

## 5. Absolute vs Relative Imports

### Absolute Import

Uses the complete package path.

```python
from calculator.addition import add
```

### Relative Import

Uses dots to reference modules relative to the current package.

```python
from .addition import add
```

For a parent package:

```python
from ..utils import helper
```

Relative imports are intended for modules within packages. They generally do not work when a module is executed directly as a standalone script without package context.

## 6. The `__name__` Variable

Python automatically assigns a `__name__` variable to every module.

- When a file is executed directly, `__name__` is `"__main__"`.
- When a file is imported, `__name__` contains its module name.

Example:

```python
# calculator.py

def add(a, b):
    return a + b


if __name__ == "__main__":
    print(add(10, 20))
```

Running the file directly:

```bash
python calculator.py
```

Output:

```text
30
```

Importing it:

```python
import calculator
```

The code inside the `if __name__ == "__main__"` block does not execute during a normal import.

This pattern is useful for writing modules that can also run independently.

## 7. Python Module Search Path

When importing a module, Python searches locations listed in `sys.path`.

```python
import sys

for path in sys.path:
    print(path)
```

The search path generally includes:

- The script directory or current working directory, depending on execution mode.
- Directories specified in `PYTHONPATH`.
- Standard library directories.
- Installed third-party package directories.

### ModuleNotFoundError

```python
import nonexistent_module
```

Output:

```text
ModuleNotFoundError: No module named 'nonexistent_module'
```

This occurs when Python cannot locate the requested module.

## 8. Built-in, Standard Library and Third-Party Modules

| Type                     | Description                          | Examples                         |
| ------------------------ | ------------------------------------ | -------------------------------- |
| Built-in modules         | Compiled into the Python interpreter | `sys`, `builtins`                |
| Standard library modules | Included with Python                 | `math`, `json`, `os`, `datetime` |
| Third-party modules      | Installed separately                 | `requests`, `numpy`, `pytest`    |
| Custom modules           | Created by developers                | `calculator.py`, `utils.py`      |

### Standard Library Example

```python
import json

data = {
    "name": "John",
    "age": 30
}

result = json.dumps(data)

print(result)
# {"name": "John", "age": 30}
```

### Third-Party Module Example

Install `requests`:

```bash
python -m pip install requests
```

Use it:

```python
import requests

response = requests.get(
    "https://example.com",
    timeout=10
)

print(response.status_code)
```

## 9. Installing and Managing Packages

Python uses `pip` to install third-party packages.

### Install a Package

```bash
python -m pip install requests
```

### Install a Specific Version

```bash
python -m pip install requests==2.32.3
```

### Upgrade a Package

```bash
python -m pip install --upgrade requests
```

### Uninstall a Package

```bash
python -m pip uninstall requests
```

### List Installed Packages

```bash
python -m pip list
```

### Generate requirements.txt

```bash
python -m pip freeze > requirements.txt
```

### Install from requirements.txt

```bash
python -m pip install -r requirements.txt
```

## 10. Virtual Environments

A virtual environment isolates project dependencies from other Python projects.

### Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate on Linux or macOS

```bash
source .venv/bin/activate
```

### Activate on Windows

```powershell
.venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
python -m pip install pytest requests
```

### Deactivate

```bash
deactivate
```

Virtual environments help avoid dependency conflicts between projects.

## 11. Module vs Package vs Library

| Feature    | Module                 | Package                                | Library                                   |
| ---------- | ---------------------- | -------------------------------------- | ----------------------------------------- |
| Definition | A Python file          | A collection of modules or subpackages | Reusable code providing functionality     |
| Structure  | Usually one `.py` file | Directory-based organization           | May contain multiple packages and modules |
| Example    | `calculator.py`        | `calculator/`                          | NumPy, Requests                           |
| Purpose    | Organize reusable code | Group related modules                  | Provide reusable functionality            |

A library is a broader concept rather than a specific Python filesystem structure.

## 12. Common Interview Questions

### Q1. What happens when a module is imported?

Python generally performs the following operations:

1. Checks whether the module is already loaded in `sys.modules`.
2. Searches for the module if it is not already loaded.
3. Creates and initializes the module object.
4. Executes the module's top-level code.
5. Makes the module available to the importing code.

A successfully imported module is normally cached in `sys.modules`, so subsequent imports do not execute its top-level code again.

### Q2. What is the difference between `import module` and `from module import function`?

```python
import math

math.sqrt(16)
```

```python
from math import sqrt

sqrt(16)
```

The first imports the module and accesses its members through the module name.

The second binds the selected member directly to a name in the current namespace.

### Q3. What is the purpose of `__init__.py`?

- Identifies a directory as a regular package.
- Can execute package initialization code.
- Can expose selected functions and classes.
- Can define the package's public interface.

### Q4. What is a circular import?

A circular import occurs when two or more modules depend on each other during import.

Example:

```python
# a.py

from b import function_b

def function_a():
    pass
```

```python
# b.py

from a import function_a

def function_b():
    pass
```

This can produce an import error if a required name has not yet been initialized.

Common solutions include restructuring shared code into a separate module or moving an import inside a function when appropriate.

### Q5. What is the difference between a module and a script?

A module is a Python file intended to be imported and reused.

A script is a Python file intended to be executed directly.

The same file can serve both purposes using:

```python
if __name__ == "__main__":
    main()
```

### Q6. How do you reload an imported module?

```python
import importlib
import calculator

importlib.reload(calculator)
```

This re-executes the module's code. However, references imported elsewhere using `from module import name` are not automatically rebound.

### Q7. What is `__all__`?

`__all__` specifies which names are exported when using a wildcard import.

```python
# calculator.py

__all__ = ["add"]

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

```python
from calculator import *
```

Only `add` is imported through the wildcard import.

`__all__` does not prevent explicit imports of other members.

## Interview Shortcut

- Module - A Python file containing reusable code.
- Package - A collection of related modules and subpackages.
- `__init__.py` - Initializes a regular package.
- `import` - Imports a module or selected members.
- Absolute import - Uses the complete package path.
- Relative import - Uses dots to reference package-relative locations.
- `__name__` - Identifies how a module is being executed.
- `__main__` - Name assigned to the directly executed module.
- `sys.path` - Locations Python searches for modules.
- `sys.modules` - Cache of loaded modules.
- `pip` - Installs and manages Python packages.
- `venv` - Creates isolated Python environments.
- `__all__` - Defines names exported by wildcard imports.
- Best practice - Organize related functionality into modules and packages, use explicit imports and isolate project dependencies.