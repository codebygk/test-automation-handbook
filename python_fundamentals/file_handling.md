# File Handling in Python

File handling allows Python programs to create, read, write, append and modify files.

Python primarily uses the built in `open()` function for file operations.

## 1. Opening a File

```python
file = open("example.txt", "r")

content = file.read()

file.close()
```

Syntax:

```python
open(file, mode)
```

Example:

```python
file = open("example.txt", "r")
```

## 2. File Modes

| Mode | Meaning           |
| ---- | ----------------- |
| `r`  | Read              |
| `w`  | Write             |
| `a`  | Append            |
| `x`  | Create a new file |
| `b`  | Binary mode       |
| `t`  | Text mode         |
| `r+` | Read and write    |
| `w+` | Write and read    |
| `a+` | Append and read   |

### `r` - Read

```python
file = open("example.txt", "r")
```

The file must already exist.

If the file does not exist:

```text
FileNotFoundError
```

### `w` - Write

```python
file = open("example.txt", "w")
file.write("Hello Python")
file.close()
```

If the file exists, its existing content is overwritten.

If the file does not exist, Python creates it.

### `a` - Append

```python
file = open("example.txt", "a")
file.write("\nHello again")
file.close()
```

Adds content to the end of the file.

Existing content is preserved.

### `x` - Create

```python
file = open("example.txt", "x")
```

Creates a new file.

If the file already exists:

```text
FileExistsError
```

## 3. Reading a File

### `read()`

Reads the entire file.

```python
with open("example.txt", "r") as file:
    content = file.read()

print(content)
```

You can also specify the number of characters:

```python
with open("example.txt", "r") as file:
    content = file.read(10)

print(content)
```

### `readline()`

Reads one line.

```python
with open("example.txt", "r") as file:
    line = file.readline()

print(line)
```

Read multiple lines:

```python
with open("example.txt", "r") as file:
    print(file.readline())
    print(file.readline())
```

### `readlines()`

Reads all lines and returns a list.

```python
with open("example.txt", "r") as file:
    lines = file.readlines()

print(lines)
```

Example output:

```python
[
    "Line 1\n",
    "Line 2\n",
    "Line 3\n"
]
```

## 4. Reading a File Line by Line

This is usually preferable for large files because it processes one line at a time.

```python
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
```

## 5. Writing to a File

```python
with open("example.txt", "w") as file:
    file.write("Hello Python")
```

Multiple lines:

```python
with open("example.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")
```

Using `writelines()`:

```python
lines = [
    "Line 1\n",
    "Line 2\n",
    "Line 3\n"
]

with open("example.txt", "w") as file:
    file.writelines(lines)
```

`writelines()` does not automatically add newline characters.

## 6. Using `with`

The recommended way to work with files is using a context manager.

```python
with open("example.txt", "r") as file:
    content = file.read()
```

Python automatically closes the file after the `with` block.

This is better than manually doing:

```python
file = open("example.txt", "r")

try:
    content = file.read()
finally:
    file.close()
```

## 7. Checking Whether a File Is Closed

```python
with open("example.txt", "r") as file:
    print(file.closed)
    # False

print(file.closed)
# True
```

## 8. File Pointer

When reading or writing, Python maintains a file position.

```python
with open("example.txt", "r") as file:
    print(file.tell())
```

`tell()` returns the current position.

Use `seek()` to move the file pointer.

```python
with open("example.txt", "r") as file:
    file.seek(5)

    content = file.read()

print(content)
```

## 9. File Encoding

Specify encoding explicitly when working with text files.

```python
with open(
    "example.txt",
    "r",
    encoding="utf-8"
) as file:
    content = file.read()
```

Writing:

```python
with open(
    "example.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write("Hello Python")
```

UTF-8 is a common choice for text files.

## 10. Handling File Exceptions

```python
try:
    with open("example.txt", "r", encoding="utf-8") as file:
        content = file.read()

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("Permission denied")
```

Common file related exceptions:

| Exception            | Meaning                                             |
| -------------------- | --------------------------------------------------- |
| `FileNotFoundError`  | File does not exist                                 |
| `FileExistsError`    | File already exists when using `x`                  |
| `PermissionError`    | Insufficient permissions                            |
| `IsADirectoryError`  | Expected a file but found a directory               |
| `NotADirectoryError` | Expected a directory but found a file               |
| `UnicodeDecodeError` | File cannot be decoded using the specified encoding |

## 11. Working with Binary Files

Use `b` mode for binary files such as images, PDFs and other binary data.

```python
with open("image.png", "rb") as file:
    data = file.read()
```

Writing binary data:

```python
with open("copy.png", "wb") as file:
    file.write(data)
```

Common binary modes:

```text
rb  - Read binary
wb  - Write binary
ab  - Append binary
```

## 12. Text Mode vs Binary Mode

| Feature   | Text Mode     | Binary Mode                       |
| --------- | ------------- | --------------------------------- |
| Mode      | `r`, `w`, `a` | `rb`, `wb`, `ab`                  |
| Data type | `str`         | `bytes`                           |
| Used for  | Text files    | Images, PDFs, executables         |
| Encoding  | Applies       | Not used for decoding binary data |

Example:

```python
with open("example.txt", "r", encoding="utf-8") as file:
    data = file.read()

print(type(data))
# <class 'str'>
```

Binary:

```python
with open("image.png", "rb") as file:
    data = file.read()

print(type(data))
# <class 'bytes'>
```

## 13. `pathlib`

`pathlib` provides an object oriented way to work with file paths.

```python
from pathlib import Path

file_path = Path("example.txt")

if file_path.exists():
    print(file_path.read_text(encoding="utf-8"))
```

Writing:

```python
from pathlib import Path

file_path = Path("example.txt")

file_path.write_text(
    "Hello Python",
    encoding="utf-8"
)
```

Checking properties:

```python
from pathlib import Path

path = Path("example.txt")

print(path.exists())
print(path.is_file())
print(path.name)
print(path.suffix)
print(path.parent)
```

Example:

```text
True
True
example.txt
.txt
.
```

## 14. Creating Directories with `pathlib`

```python
from pathlib import Path

directory = Path("data")

directory.mkdir(exist_ok=True)
```

Create nested directories:

```python
directory = Path("data/reports/2026")

directory.mkdir(
    parents=True,
    exist_ok=True
)
```

## 15. Listing Files in a Directory

```python
from pathlib import Path

directory = Path("data")

for file in directory.iterdir():
    print(file)
```

Find only `.txt` files:

```python
for file in directory.glob("*.txt"):
    print(file)
```

Recursive search:

```python
for file in directory.rglob("*.txt"):
    print(file)
```

## 16. Rename and Delete Files

```python
from pathlib import Path

old_file = Path("old.txt")
new_file = Path("new.txt")

old_file.rename(new_file)
```

Delete a file:

```python
new_file.unlink()
```

Check before deleting:

```python
if new_file.exists():
    new_file.unlink()
```

## 17. File Copying

Use `shutil` for copying files.

```python
import shutil

shutil.copy(
    "source.txt",
    "destination.txt"
)
```

Copy while preserving metadata:

```python
shutil.copy2(
    "source.txt",
    "destination.txt"
)
```

## 18. File Moving

```python
import shutil

shutil.move(
    "source.txt",
    "data/source.txt"
)
```

## 19. JSON File Handling

JSON files can be handled using the `json` module.

```python
import json

data = {
    "name": "John",
    "age": 30
}

with open("user.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)
```

Read JSON:

```python
with open("user.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print(data["name"])
```

## 20. CSV File Handling

Python provides the `csv` module for CSV files.

```python
import csv

with open(
    "users.csv",
    "r",
    newline="",
    encoding="utf-8"
) as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"])
```

Writing:

```python
import csv

users = [
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25}
]

with open(
    "users.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["name", "age"]
    )

    writer.writeheader()
    writer.writerows(users)
```

## 21. Common Interview Questions

### Q1. What is the difference between `w` and `a`?

```text
w - Overwrites existing content
a - Preserves existing content and adds new content
```

### Q2. Why should we use `with open()`?

It automatically closes the file after the block finishes, including when an exception occurs.

```python
with open("example.txt", "r") as file:
    data = file.read()
```

### Q3. What is the difference between `read()`, `readline()` and `readlines()`?

| Method        | Result                                                  |
| ------------- | ------------------------------------------------------- |
| `read()`      | Reads the entire file or specified number of characters |
| `readline()`  | Reads one line                                          |
| `readlines()` | Reads all lines into a list                             |

### Q4. What is the difference between `r` and `rb`?

```text
r  - Reads text and returns str
rb - Reads binary data and returns bytes
```

### Q5. What happens if you open an existing file using `w`?

Its existing contents are truncated before writing.

```python
with open("example.txt", "w") as file:
    file.write("New content")
```

### Q6. How do you efficiently read a large file?

Read it line by line instead of loading the entire file into memory.

```python
with open("large.log", "r", encoding="utf-8") as file:
    for line in file:
        process(line)
```

### Q7. What is the difference between `os` and `pathlib`?

Both can work with files and directories.

```python
from pathlib import Path

path = Path("data/example.txt")
```

`pathlib` provides an object oriented API and is generally preferred for modern Python code.

The `os` and `os.path` modules are still widely used and provide lower level operating system functionality.

## Interview Shortcut

```text
open()       - Opens a file
r            - Read
w            - Write and overwrite
a            - Append
x            - Create exclusively
b            - Binary mode
t            - Text mode

read()       - Read entire file
readline()   - Read one line
readlines()  - Read all lines
write()      - Write text
writelines() - Write multiple strings
tell()       - Get current file position
seek()       - Move file position

with open()  - Recommended file handling pattern
pathlib      - Modern path and file handling
shutil       - Copy and move files
json         - JSON file handling
csv          - CSV file handling
```