# Stack

## Definition

A **stack** is a linear data structure that follows **LIFO**:

**Last In, First Out**

The element added last is removed first.

```text
Push 10
Push 20
Push 30

Stack:
    30 <- Top
    20
    10

Pop -> 30
```

## Key Operations

| Operation | Meaning | Complexity |
|---|---|---:|
| `push` | Add element to top | O(1) |
| `pop` | Remove top element | O(1) |
| `peek` | View top element | O(1) |
| `is_empty` | Check whether empty | O(1) |

## Using List

Python does not have a dedicated built-in Stack type. A `list` can be used as a stack.

```python
stack = []

stack.append(10)  # Push
stack.append(20)
stack.append(30)

print(stack[-1])  # Peek -> 30

print(stack.pop())  # Pop -> 30
print(stack.pop())  # Pop -> 20
```

## Using Deque

`collections.deque` is also commonly used when you want efficient operations at both ends.

```python
from collections import deque

stack = deque()

stack.append(10)
stack.append(20)
stack.append(30)

print(stack[-1])  # Peek
print(stack.pop())  # Pop
```

## Common Applications

- Function call stack
- Undo/redo operations
- Browser history
- Expression evaluation
- Parentheses matching
- Backtracking
- Depth-First Search (DFS)
- Recursion simulation

## Example: Balanced Parentheses

```python
def is_balanced(expression):
    stack = []

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in expression:
        if char in "([{":
            stack.append(char)

        elif char in ")]}":
            if not stack or stack.pop() != pairs[char]:
                return False

    return not stack
```

```python
print(is_balanced("({[]})"))  # True
print(is_balanced("([)]"))    # False
```

## Stack vs Queue

| Feature | Stack | Queue |
|---|---|---|
| Principle | LIFO | FIFO |
| Add | Top | Rear |
| Remove | Top | Front |
| Python | `list` / `deque` | `deque` |
| Common use | DFS, undo | BFS, scheduling |

## Interview Points

- Stack follows **LIFO**.
- `push` adds an element.
- `pop` removes the most recently added element.
- `peek` returns the top element without removing it.
- Python `list.append()` and `list.pop()` provide efficient stack operations.
- `deque` is useful when efficient operations at both ends are required.
- Stack is commonly used in recursion, DFS, backtracking, and expression parsing.

## Common Interview Question

**How would you implement a stack in Python?**

```python
stack = []

stack.append(10)  # Push
stack.append(20)

top = stack[-1]   # Peek
value = stack.pop()  # Pop
```

**Why shouldn't we use `pop(0)` for a stack?**

Because removing the first element from a list requires shifting the remaining elements, making it O(n). For a stack, `append()` and `pop()` at the end are O(1).