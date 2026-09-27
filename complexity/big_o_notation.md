# Big-O Notation

## Definition

**Big-O notation** describes how an algorithm's **time or space requirements grow as the input size increases**.

It focuses on the **growth rate**, not the exact execution time.

```text
Input size = n

How does the algorithm scale as n grows?
```

---

# Common Complexities

| Complexity | Name | Example |
|---|---|---|
| O(1) | Constant | List index access |
| O(log n) | Logarithmic | Binary Search |
| O(n) | Linear | Linear Search |
| O(n log n) | Linearithmic | Merge Sort |
| O(n²) | Quadratic | Nested loops |
| O(n³) | Cubic | 3 nested loops |
| O(2ⁿ) | Exponential | Some recursive subsets |
| O(n!) | Factorial | Permutations |

From generally better to worse:

```text
O(1)
O(log n)
O(n)
O(n log n)
O(n²)
O(n³)
O(2ⁿ)
O(n!)
```

---

# O(1) - Constant

Execution does not depend on input size.

```python
def get_first(numbers):
    return numbers[0]
```

Whether the list contains 10 or 10 million elements, accessing an index is typically O(1).

---

# O(log n) - Logarithmic

The problem size is repeatedly reduced, usually by half.

Binary Search:

```text
n
n/2
n/4
n/8
...
1
```

```python
def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

Time:

```text
O(log n)
```

---

# O(n) - Linear

Work grows proportionally with input size.

```python
def find_value(numbers, target):
    for number in numbers:
        if number == target:
            return True

    return False
```

For `n` elements, we may inspect up to `n` elements.

```text
O(n)
```

---

# O(n log n) - Linearithmic

Common in efficient comparison-based sorting algorithms.

Examples:

- Merge Sort
- Heap Sort
- Average-case Quick Sort
- Python Timsort

```text
O(n log n)
```

---

# O(n²) - Quadratic

Usually occurs with nested loops over the same input.

```python
def print_pairs(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            print(numbers[i], numbers[j])
```

If there are `n` elements:

```text
n * n = n²

O(n²)
```

Common examples:

- Bubble Sort
- Selection Sort
- Insertion Sort worst case
- Brute-force pair comparisons

---

# O(n³) - Cubic

Three nested loops:

```python
for i in range(n):
    for j in range(n):
        for k in range(n):
            pass
```

```text
n * n * n = n³

O(n³)
```

---

# O(2ⁿ) - Exponential

The amount of work roughly doubles as input size increases.

A common example is naive recursive Fibonacci:

```python
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
```

Complexity is approximately:

```text
O(2ⁿ)
```

---

# O(n!) - Factorial

Extremely expensive growth.

A common example is generating all permutations.

```text
n elements

Number of permutations = n!
```

For example:

```text
3! = 6
5! = 120
10! = 3,628,800
```

---

# Time vs Space Complexity

Big-O can describe both.

### Time Complexity

How execution time grows with input size.

```python
for number in numbers:
    print(number)
```

```text
Time = O(n)
```

### Space Complexity

How additional memory usage grows.

```python
def create_copy(numbers):
    result = []

    for number in numbers:
        result.append(number)

    return result
```

```text
Space = O(n)
```

---

# How to Calculate Big-O

## Rule 1 - Drop Constants

```python
for i in range(n):
    print(i)

for i in range(n):
    print(i)
```

This is:

```text
O(n + n)
= O(2n)
= O(n)
```

We ignore constant factors.

---

## Rule 2 - Drop Lower-Order Terms

```text
O(n² + n + 10)
```

The dominant term is `n²`.

Therefore:

```text
O(n²)
```

---

## Rule 3 - Sequential Operations Add

```python
for i in range(n):
    pass

for i in range(n):
    pass
```

```text
O(n) + O(n)
= O(2n)
= O(n)
```

---

## Rule 4 - Nested Operations Multiply

```python
for i in range(n):
    for j in range(n):
        pass
```

```text
O(n) * O(n)
= O(n²)
```

---

## Rule 5 - Different Input Sizes

If two independent inputs are involved:

```python
for x in list_a:
    pass

for y in list_b:
    pass
```

Complexity:

```text
O(a + b)
```

Nested:

```python
for x in list_a:
    for y in list_b:
        pass
```

Complexity:

```text
O(a * b)
```

---

# Best, Average and Worst Case

An algorithm can have different complexities depending on the input.

Example: Linear Search

```text
[10, 20, 30, 40, 50]
```

Searching for `10`:

```text
Best Case = O(1)
```

Searching for `30`:

```text
Average Case = O(n)
```

Searching for `100`:

```text
Worst Case = O(n)
```

---

# Common Data Structures

| Operation | List | Dictionary | Set |
|---|---:|---:|---:|
| Access | O(1) | O(1) avg by key | N/A |
| Search | O(n) | O(1) avg | O(1) avg |
| Insert | O(1) avg at end | O(1) avg | O(1) avg |
| Delete | O(n) | O(1) avg | O(1) avg |

---

# Common Algorithms

| Algorithm | Time |
|---|---:|
| Linear Search | O(n) |
| Binary Search | O(log n) |
| Bubble Sort | O(n²) |
| Selection Sort | O(n²) |
| Insertion Sort | O(n²) |
| Merge Sort | O(n log n) |
| Quick Sort | O(n log n) average |
| Heap Sort | O(n log n) |
| Hash lookup | O(1) average |
| Two Pointers | O(n) |
| Sliding Window | O(n) |

---

# Important Interview Concepts

## Amortized Complexity

Some operations are occasionally expensive but cheap on average.

Python list:

```python
numbers.append(value)
```

`append()` is **O(1) amortized**.

Occasionally Python must resize the underlying array, which costs O(n), but across many appends the average cost remains O(1).

---

## Recursion and Space

Recursive calls consume the call stack.

```python
def countdown(n):
    if n == 0:
        return

    countdown(n - 1)
```

For `n` recursive calls:

```text
Space = O(n)
```

---

# Interview Rules

```text
Single loop
    -> O(n)

Nested loops
    -> Usually O(n²)

Loop that halves the input
    -> O(log n)

Loop + binary division
    -> Often O(n log n)

Two independent loops
    -> Add

Nested independent loops
    -> Multiply

Ignore constants
    -> O(2n) becomes O(n)

Keep dominant term
    -> O(n² + n) becomes O(n²)
```

# Interview Answer

**What is Big-O notation?**

> "Big-O notation describes how an algorithm's time or space requirements grow as the input size increases. It focuses on the algorithm's growth rate and usually considers the worst-case complexity. For example, linear search is O(n), binary search is O(log n), and merge sort is O(n log n)."

## Most Important for Interviews

```text
Must Know:
- O(1)
- O(log n)
- O(n)
- O(n log n)
- O(n²)
- Time vs space complexity
- Best / average / worst case
- Nested loops
- Recursion
- Amortized complexity
```
