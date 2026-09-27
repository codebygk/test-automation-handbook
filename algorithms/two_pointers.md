# Two Pointers

## Definition

**Two Pointers** is a problem-solving technique where two indices or references are used to traverse a data structure, usually an array or string.

Instead of repeatedly scanning the same elements, the pointers move according to specific conditions.

```text
[1, 2, 3, 4, 6, 8]
 ^              ^
left           right
```

It can often reduce a solution from O(n²) to O(n).

---

# Common Patterns

## 1. Opposite Direction

One pointer starts from the beginning and another from the end.

```python
def two_sum_sorted(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]

        if total == target:
            return left, right

        if total < target:
            left += 1
        else:
            right -= 1

    return -1
```

Example:

```python
numbers = [1, 2, 3, 4, 6, 8]

print(two_sum_sorted(numbers, 10))
# (1, 5)
```

```text
1  2  3  4  6  8
^              ^

2 + 8 = 10
```

### Complexity

- Time: O(n)
- Space: O(1)

### Common Problems

- Two Sum in sorted array
- Pair with target sum
- Container With Most Water
- Valid Palindrome
- 3Sum

---

# 2. Same Direction

Both pointers move from left to right.

```text
[1, 2, 3, 4, 5]
 ^  ^
slow
fast
```

Example: remove duplicates from a sorted array.

```python
def remove_duplicates(numbers):
    if not numbers:
        return 0

    slow = 0

    for fast in range(1, len(numbers)):
        if numbers[fast] != numbers[slow]:
            slow += 1
            numbers[slow] = numbers[fast]

    return slow + 1
```

Example:

```python
numbers = [1, 1, 2, 2, 3]

length = remove_duplicates(numbers)

print(numbers[:length])
# [1, 2, 3]
```

Here:

- `fast` scans the array
- `slow` tracks the position where the next unique element should go

---

# 3. Fast and Slow Pointers

Two pointers move at different speeds.

```text
slow -> one step
fast -> two steps
```

Commonly used with linked lists.

### Detect Cycle

```python
def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False
```

This is known as **Floyd's Cycle Detection Algorithm**.

### Complexity

- Time: O(n)
- Space: O(1)

### Common Problems

- Detect cycle in linked list
- Find middle of linked list
- Find cycle starting point
- Find nth node from the end

---

# Two Pointers vs Sliding Window

These techniques are related but not identical.

| Feature    | Two Pointers                     | Sliding Window              |
| ---------- | -------------------------------- | --------------------------- |
| Main idea  | Two positions/references         | Maintain a contiguous range |
| Pointers   | Often two                        | Usually left + right        |
| Direction  | Same or opposite                 | Usually same direction      |
| Common use | Pairs, linked lists, comparisons | Subarrays/substrings        |
| Example    | Two Sum                          | Longest substring           |

Example:

```text
Two Pointers:

[1, 2, 3, 4, 6]
 ^           ^
left        right
```

```text
Sliding Window:

[1, 2, 3, 4, 6]
    [-------]
     left  right
```

---

# When to Recognize Two Pointers

Look for these clues:

- Sorted array
- Find a pair
- Find a triplet
- Compare elements from both ends
- Remove duplicates in-place
- Palindrome
- Linked list cycle
- Find middle of linked list
- Need O(1) extra space

---

# Complexity

Typical two-pointer solution:

```text
Time  -> O(n)
Space -> O(1)
```

Why?

Each pointer generally moves through the collection at most once.

---

# Common Interview Problems

### P1

- Two Sum II
- Valid Palindrome
- Remove Duplicates from Sorted Array
- Move Zeroes
- Reverse String
- Merge Sorted Arrays
- Linked List Cycle
- Middle of Linked List

### P2

- Container With Most Water
- 3Sum
- Remove Nth Node From End
- Sort Colors

### P3

- Trapping Rain Water
- Four Sum
- Palindrome Linked List

---

# Interview Answer

**What is the Two Pointers technique?**

> "Two Pointers is a technique where I maintain two indices or references and move them according to the problem's conditions. It is commonly used with sorted arrays, strings, and linked lists. It can reduce nested-loop solutions from O(n²) to O(n), often with O(1) extra space."

## Key Rule

```text
Pair / comparison from both ends
        -> Two Pointers

Contiguous subarray / substring
        -> Sliding Window

Linked list cycle / middle
        -> Fast and Slow Pointers
```