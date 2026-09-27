# Sorting Algorithms

## Quick Comparison

| Algorithm | Best | Average | Worst | Space | Stable |
|---|---:|---:|---:|---:|---|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) avg | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Tim Sort | O(n) | O(n log n) | O(n log n) | O(n) | Yes |

For interviews, focus primarily on:

1. Bubble Sort
2. Selection Sort
3. Insertion Sort
4. Merge Sort
5. Quick Sort
6. Heap Sort

---

# 1. Bubble Sort

Repeatedly compares adjacent elements and swaps them if they are in the wrong order.

```text
[5, 3, 4, 1]

5 > 3 -> swap
[3, 5, 4, 1]

5 > 4 -> swap
[3, 4, 5, 1]

5 > 1 -> swap
[3, 4, 1, 5]
```

### Implementation

```python
def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True

        if not swapped:
            break

    return numbers
```

### Complexity

- Best: O(n)
- Average: O(n²)
- Worst: O(n²)
- Space: O(1)
- Stable: Yes

### Interview Use

Mostly useful for understanding sorting fundamentals. Rarely used in production.

---

# 2. Selection Sort

Finds the smallest element and places it at the correct position.

```text
[5, 3, 4, 1]

Find minimum -> 1
Swap with first

[1, 3, 4, 5]
```

### Implementation

```python
def selection_sort(numbers):
    n = len(numbers)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j

        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    return numbers
```

### Complexity

- Best: O(n²)
- Average: O(n²)
- Worst: O(n²)
- Space: O(1)
- Stable: Usually no

---

# 3. Insertion Sort

Builds the sorted portion one element at a time.

```text
[5, 3, 4, 1]

5
3 -> insert before 5

[3, 5]

4 -> insert between 3 and 5

[3, 4, 5]
```

### Implementation

```python
def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = key

    return numbers
```

### Complexity

- Best: O(n)
- Average: O(n²)
- Worst: O(n²)
- Space: O(1)
- Stable: Yes

### When Useful

Insertion Sort performs well when:

- Data is small
- Data is already nearly sorted
- Elements arrive incrementally

---

# 4. Merge Sort

Uses **divide and conquer**.

```text
[8, 3, 5, 1]

       Divide
         |
    [8,3] [5,1]
      |      |
   [8][3]  [5][1]
      |      |
    [3,8]  [1,5]
         |
    [1,3,5,8]
```

### Complexity

- Best: O(n log n)
- Average: O(n log n)
- Worst: O(n log n)
- Space: O(n)
- Stable: Yes

### Key Idea

```text
Divide
  ->
Sort
  ->
Merge
```

### Interview Point

Merge Sort provides guaranteed O(n log n) time but requires additional memory for the typical array implementation.

---

# 5. Quick Sort

Also uses **divide and conquer**.

It selects a **pivot**, partitions the array around the pivot, and recursively sorts the partitions.

```text
[6, 3, 8, 2, 5]

Pivot = 5

[3, 2]  5  [6, 8]
```

Then recursively sort both sides.

### Complexity

- Best: O(n log n)
- Average: O(n log n)
- Worst: O(n²)
- Space: O(log n) average for recursion
- Stable: No

### Worst Case

Poor pivot selection can produce highly unbalanced partitions.

```text
[1, 2, 3, 4, 5]

Pivot = 1

[] 1 [2, 3, 4, 5]
```

This can lead to O(n²).

### Interview Point

Randomized pivot selection or a good pivot strategy can reduce the likelihood of the worst case.

---

# 6. Heap Sort

Uses a **heap** data structure.

For ascending order, a max heap can repeatedly move the largest element to the end.

### Complexity

- Best: O(n log n)
- Average: O(n log n)
- Worst: O(n log n)
- Space: O(1)
- Stable: No

### Key Advantage

It provides guaranteed O(n log n) time with O(1) auxiliary space.

---

# Python's Built-in Sorting

In real Python applications, use:

```python
numbers.sort()
```

or:

```python
sorted_numbers = sorted(numbers)
```

Python uses **Timsort**, which combines ideas from Merge Sort and Insertion Sort.

```python
numbers = [5, 2, 8, 1, 3]

print(sorted(numbers))
# [1, 2, 3, 5, 8]
```

### `sort()` vs `sorted()`

| Feature | `list.sort()` | `sorted()` |
|---|---|---|
| Modifies original | Yes | No |
| Returns | `None` | New sorted object |
| Works with | Lists | Any iterable |
| Stable | Yes | Yes |

---

# Stable Sorting

A sorting algorithm is **stable** if equal elements maintain their original relative order.

Example:

```text
Before:

(A, 90)
(B, 80)
(C, 90)

Sort by score:

(B, 80)
(A, 90)
(C, 90)
```

A stable sort keeps `A` before `C` because both have the same score.

Stable algorithms:

- Bubble Sort
- Insertion Sort
- Merge Sort
- Timsort

---

# In-place Sorting

An in-place algorithm uses very little additional memory.

Examples:

- Bubble Sort
- Selection Sort
- Insertion Sort
- Heap Sort

Merge Sort typically requires O(n) additional memory for arrays.

---

# Important Interview Comparison

| Algorithm | Main Idea | Best Use |
|---|---|---|
| Bubble | Swap adjacent elements | Learning fundamentals |
| Selection | Select minimum | Simple implementation |
| Insertion | Insert into sorted portion | Small/nearly sorted data |
| Merge | Divide and merge | Guaranteed O(n log n), stability |
| Quick | Pivot and partition | Fast general-purpose sorting |
| Heap | Heap-based selection | O(n log n) with low extra space |
| Timsort | Merge + insertion techniques | Python's built-in sorting |

## Important Interview Questions

**Which sorting algorithm has O(n log n) worst-case complexity?**

- Merge Sort
- Heap Sort
- Timsort

Quick Sort has O(n log n) average complexity but O(n²) worst case.

**Which sorting algorithm is good for nearly sorted data?**

Insertion Sort.

**Which sorting algorithm is stable?**

Merge Sort and Insertion Sort are common examples. Python's Timsort is also stable.

**What sorting algorithm does Python use?**

Python's built-in sorting uses **Timsort**.

**What is the difference between `sort()` and `sorted()`?**

`sort()` modifies the existing list and returns `None`. `sorted()` creates and returns a new sorted object.

**Which sorting algorithm should you use in production Python code?**

Usually Python's built-in `sorted()` or `list.sort()` rather than implementing a sorting algorithm manually.

# Interview Priority

```text
P1:
- Bubble Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Time and space complexity
- Stable vs unstable
- In-place vs out-of-place
- sort() vs sorted()

P2:
- Selection Sort
- Heap Sort
- Timsort internals

P3:
- Counting Sort
- Radix Sort
- Bucket Sort
```