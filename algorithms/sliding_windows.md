# Sliding Window

## Definition

**Sliding Window** is a technique for solving problems involving **contiguous subarrays or substrings**.

Instead of repeatedly calculating the same elements, maintain a window using two pointers:

```text
[1, 2, 3, 4, 5, 6]
 ^        ^
left     right
```

The window expands or shrinks based on a condition.

It often reduces O(n²) solutions to **O(n)**.

---

# 1. Fixed-Size Window

The window size remains constant.

### Example

Find the maximum sum of a subarray of size `k`.

```python
def max_sum(numbers, k):
    window_sum = sum(numbers[:k])
    maximum = window_sum

    for right in range(k, len(numbers)):
        window_sum += numbers[right]
        window_sum -= numbers[right - k]

        maximum = max(maximum, window_sum)

    return maximum
```

Example:

```python
numbers = [2, 1, 5, 1, 3, 2]

print(max_sum(numbers, 3))
# 9
```

The windows are:

```text
[2, 1, 5]  -> 8
[1, 5, 1]  -> 7
[5, 1, 3]  -> 9
[1, 3, 2]  -> 6
```

### Complexity

```text
Time  -> O(n)
Space -> O(1)
```

---

# 2. Variable-Size Window

The window expands and shrinks depending on a condition.

### Example

Longest substring without repeating characters.

```python
def longest_unique_substring(s):
    seen = set()

    left = 0
    maximum = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        maximum = max(maximum, right - left + 1)

    return maximum
```

Example:

```python
s = "abcabcbb"

print(longest_unique_substring(s))
# 3
```

The longest substring is:

```text
abc
```

---

# How Variable Window Works

```text
"abcabcbb"

left
 ^
 a b c
     ^
    right
```

When a constraint is violated:

```text
Expand
   |
   v
[ a b c a ]
^         ^
left     right

Duplicate "a"

Shrink
   |
   v

[ b c a ]
    ^   ^
   left right
```

The window keeps moving forward instead of restarting from every position.

---

# General Template

```python
def sliding_window(data):
    left = 0

    for right in range(len(data)):

        # Add data[right] to window

        while window_is_invalid():
            # Remove data[left]
            left += 1

        # Process current window
```

The exact condition depends on the problem.

---

# Fixed vs Variable Window

| Feature            | Fixed Window                   | Variable Window          |
| ------------------ | ------------------------------ | ------------------------ |
| Window size        | Constant                       | Changes                  |
| Right pointer      | Moves                          | Moves                    |
| Left pointer       | Usually follows fixed distance | Moves based on condition |
| Common problem     | Max sum of K elements          | Longest substring        |
| Typical complexity | O(n)                           | O(n)                     |

---

# When to Recognize Sliding Window

Look for:

- Contiguous subarray
- Contiguous substring
- Longest substring
- Shortest subarray
- Maximum/minimum sum
- At most K distinct elements
- Exactly K elements
- Window of size K
- Longest/shortest sequence satisfying a condition

---

# Common Interview Problems

## P1

- Maximum sum subarray of size K
- Longest substring without repeating characters
- Maximum number of vowels in a substring of size K
- Minimum size subarray sum
- Longest substring with at most K distinct characters

## P2

- Permutation in String
- Find All Anagrams in a String
- Longest Repeating Character Replacement
- Fruit Into Baskets

## P3

- Minimum Window Substring
- Sliding Window Maximum

---

# Sliding Window vs Two Pointers

Sliding Window is essentially a **specialized use of two pointers** for maintaining a contiguous range.

| Two Pointers                | Sliding Window                |
| --------------------------- | ----------------------------- |
| General technique           | Specialized technique         |
| Can use opposite directions | Usually same direction        |
| Can work on linked lists    | Usually arrays/strings        |
| Pair comparison is common   | Contiguous range is essential |
| Example: Two Sum            | Example: Longest Substring    |

```text
Two Pointers:

[1, 2, 3, 4, 5]
 ^           ^
left       right
```

```text
Sliding Window:

[1, 2, 3, 4, 5]
    [-------]
     window
```

---

# Why O(n)?

Although there may be a nested `while` loop:

```python
for right in range(n):
    while condition:
        left += 1
```

it is still typically O(n) because:

- `right` moves forward at most `n` times
- `left` also moves forward at most `n` times

Therefore:

```text
O(n) + O(n) = O(n)
```

---

# Interview Answer

**What is the Sliding Window technique?**

> "Sliding Window is a technique used mainly for contiguous subarray or substring problems. I maintain a window using left and right pointers, expand the window as I scan the data, and shrink it when the constraint is violated. This avoids repeatedly processing overlapping elements and often reduces an O(n²) solution to O(n)."

## Key Rule

```text
Contiguous subarray / substring
        +
Need longest / shortest / maximum / minimum
        |
        v
Sliding Window

Pair from both ends
        |
        v
Two Pointers
```
```