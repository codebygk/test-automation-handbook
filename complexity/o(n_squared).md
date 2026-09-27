# O(n²) - Quadratic Time

## Definition

**O(n²)** means the amount of work grows roughly with the **square of the input size**.

If the input doubles, the work becomes roughly **4 times larger**.

```text
n = 10      -> ~100 operations
n = 100     -> ~10,000 operations
n = 1,000   -> ~1,000,000 operations
```

## Example

```python
def print_pairs(numbers):
    for i in numbers:
        for j in numbers:
            print(i, j)
```

The outer loop runs `n` times.

For each outer iteration, the inner loop also runs `n` times.

```text
n * n = n²

Time: O(n²)
Space: O(1)
```

## Common Example - Nested Loops

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

Execution:

```text
Outer loop -> n times
Inner loop -> n times per outer iteration

Total -> n * n
      -> n²
      -> O(n²)
```

## Example - Comparing All Pairs

```python
def find_duplicates(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                return True

    return False
```

Each element may be compared with many other elements.

```text
Time: O(n²)
Space: O(1)
```

## O(n²) vs O(n)

| Complexity | Growth | Example |
|---|---|---|
| O(1) | Constant | List index access |
| O(n) | Linear | Linear search |
| O(n²) | Quadratic | Nested loops |
| O(n³) | Cubic | Three nested loops |

## Important Point

Not every nested loop is automatically O(n²).

```python
j = 0

for i in range(n):
    while j < n:
        j += 1
```

Here, `j` does not reset for every `i`.

Both `i` and `j` move forward at most `n` times.

```text
Time: O(n)
```

So analyze **how many times the operations actually execute**, not just the number of loops.

## Common O(n²) Algorithms

```text
Bubble Sort          -> O(n²) average/worst
Selection Sort       -> O(n²)
Insertion Sort       -> O(n²) average/worst
Comparing all pairs  -> O(n²)
Nested loops         -> Often O(n²)
```

## When n Gets Large

```text
n       O(n)       O(n²)
10      10         100
100     100        10,000
1,000   1,000      1,000,000
10,000  10,000     100,000,000
```

This is why quadratic algorithms can become expensive as input size increases.

## Interview Question

**What is O(n²) time complexity?**

> "O(n²) means quadratic time. The amount of work grows approximately with the square of the input size. A common example is two independent nested loops, where each loop runs n times, resulting in n multiplied by n, or O(n²)."

## Key Rule

```text
Two independent full passes nested inside each other
                    |
                    v
                  O(n²)
```