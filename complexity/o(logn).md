# O(log n) - Logarithmic Time

## Definition

**O(log n)** means the amount of work grows very slowly as the input size increases.

The key idea is that the algorithm **reduces the problem size significantly at each step**, commonly by half.

```text
n = 1,000,000

1,000,000
500,000
250,000
125,000
...
1
```

Only about **20 steps** are needed because:

```text
log₂(1,000,000) ≈ 20
```

## Example - Binary Search

```python
def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle

        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1
```

For a sorted list:

```text
[10, 20, 30, 40, 50, 60, 70, 80]

             40
          /      \
       left      right
```

Each step eliminates roughly half of the remaining elements.

```text
n
n/2
n/4
n/8
n/16
...
```

Therefore:

```text
Time: O(log n)
Space: O(1)
```

## Why Is It So Efficient?

Compare the number of steps:

| Input Size | O(n) | O(log₂ n) |
|---:|---:|---:|
| 10 | 10 | ~4 |
| 100 | 100 | ~7 |
| 1,000 | 1,000 | ~10 |
| 1,000,000 | 1,000,000 | ~20 |
| 1,000,000,000 | 1,000,000,000 | ~30 |

This is why logarithmic algorithms scale very well.

## Common Examples

```text
Binary Search                 -> O(log n)
Balanced BST search            -> O(log n)
Balanced BST insertion         -> O(log n)
Balanced BST deletion          -> O(log n)
Heap insertion                 -> O(log n)
Heap deletion                  -> O(log n)
```

## Important Pattern

When you see an algorithm that repeatedly:

```text
Divides the problem by 2
Divides by 2 again
Divides by 2 again
...
```

Think:

```text
O(log n)
```

More generally, repeatedly reducing the problem by a constant factor gives logarithmic complexity.

## O(log n) vs O(n)

```text
O(log n)
    |
    | grows very slowly
    v
O(n)
    |
    | grows proportionally
    v
```

For example, binary search is much more efficient than linear search for a large **sorted** collection.

## Important Interview Point

Binary search requires a **sorted collection** and is most effective when the data structure provides efficient random access, such as a Python list.

## Interview Answer

> "O(log n) means logarithmic time. The algorithm reduces the problem size by a constant factor at each step, often by half. Binary search is the classic example because it eliminates half of the search space after every comparison."

## Key Rule

```text
Repeatedly reduce the problem by a constant factor
                    |
                    v
                 O(log n)
```