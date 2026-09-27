# Searching Algorithm

## Quick Comparison

| Algorithm            | Data Requirement              | Best |      Average |      Worst | Space |
| -------------------- | ----------------------------- | ---: | -----------: | ---------: | ----: |
| Linear Search        | Any                           | O(1) |         O(n) |       O(n) |  O(1) |
| Binary Search        | Sorted                        | O(1) |     O(log n) |   O(log n) |  O(1) |
| Jump Search          | Sorted                        | O(1) |   O(sqrt(n)) | O(sqrt(n)) |  O(1) |
| Interpolation Search | Sorted, uniformly distributed | O(1) | O(log log n) |       O(n) |  O(1) |
| Exponential Search   | Sorted                        | O(1) |     O(log n) |   O(log n) |  O(1) |

For interviews, focus primarily on **Linear Search** and **Binary Search**.

---

## 1. Linear Search

Checks every element sequentially until the target is found.

```python
def linear_search(numbers, target):
    for i, value in enumerate(numbers):
        if value == target:
            return i

    return -1
```

```python
numbers = [10, 20, 30, 40, 50]

print(linear_search(numbers, 30))  # 2
```

### Complexity

- Best: O(1)
- Average: O(n)
- Worst: O(n)
- Space: O(1)

### Use When

- Data is unsorted
- Dataset is small
- Simplicity is important

---

## 2. Binary Search

Binary Search repeatedly divides a **sorted** collection into two halves.

```text
[10, 20, 30, 40, 50, 60, 70]
              |
             40

Target < 40
Search left half

Target > 40
Search right half
```

### Implementation

```python
def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if numbers[mid] == target:
            return mid

        if numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

```python
numbers = [10, 20, 30, 40, 50, 60, 70]

print(binary_search(numbers, 50))  # 4
```

### Complexity

- Best: O(1)
- Average: O(log n)
- Worst: O(log n)
- Space: O(1) for iterative implementation

### Key Requirement

The data must be **sorted**.

---

## 3. Jump Search

Jump Search works on sorted data by jumping ahead by fixed blocks instead of checking every element.

Typical jump size:

```text
sqrt(n)
```

Complexity:

- Best: O(1)
- Average: O(sqrt(n))
- Worst: O(sqrt(n))
- Space: O(1)

It is less commonly used in interviews than Binary Search.

---

## 4. Interpolation Search

Interpolation Search estimates where the target might be located based on its value.

It works best when sorted values are **uniformly distributed**.

Example:

```text
10 20 30 40 50 60 70
```

It can estimate that 60 should be near the end instead of always checking the middle.

Complexity:

- Best: O(1)
- Average: O(log log n)
- Worst: O(n)
- Space: O(1)

---

## 5. Exponential Search

Exponential Search first finds a range containing the target and then applies Binary Search.

```text
1
2
4
8
16
...
```

Useful when:

- Data is sorted
- Size is unknown or effectively unbounded
- Target may be near the beginning

Complexity:

- Best: O(1)
- Average: O(log n)
- Worst: O(log n)

---

# Binary Search Variations

These are very important for coding interviews.

## Find First Occurrence

```python
def first_occurrence(numbers, target):
    left = 0
    right = len(numbers) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if numbers[mid] == target:
            result = mid
            right = mid - 1
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result
```

For:

```python
numbers = [1, 2, 2, 2, 3]
```

```text
first_occurrence(numbers, 2) -> 1
```

## Find Last Occurrence

Same idea, but when the target is found, continue searching to the right.

```text
[1, 2, 2, 2, 3]
    ^     ^
 first   last
```

## Search Insert Position

Find the position where a target should be inserted while maintaining sorted order.

```python
numbers = [10, 20, 30, 40]

target = 25

# Insert position = 2
```

This is commonly solved using Binary Search.

---

# Searching in Different Data Structures

| Data Structure          | Typical Search |
| ----------------------- | -------------- |
| Array / List            | Linear Search  |
| Sorted Array            | Binary Search  |
| Hash Table / Dictionary | Hash lookup    |
| Set                     | Hash lookup    |
| Linked List             | Linear Search  |
| Binary Search Tree      | Tree traversal |
| Graph                   | BFS / DFS      |

## Important Interview Rule

```text
Unsorted data
    -> Linear Search

Sorted data + random access
    -> Binary Search

Need very fast repeated lookup
    -> Hash Table / Set

Graph
    -> BFS / DFS
```

## Common Interview Questions

**Why is Binary Search O(log n)?**

Because each comparison eliminates approximately half of the remaining search space.

```text
n
n/2
n/4
n/8
...
1
```

**Can Binary Search work on a linked list?**

It can theoretically be implemented, but it is generally inefficient because finding the middle element requires traversal. Binary Search is most effective with structures that provide O(1) random access, such as arrays.

**Which searching algorithm should you use for an unsorted array?**

Usually Linear Search unless you can justify sorting first.

**Why not always sort and use Binary Search?**

Sorting itself costs O(n log n). If you only need one search, Linear Search may be cheaper. Binary Search becomes more attractive when you perform many searches on the same data.