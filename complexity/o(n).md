# O(n) - Linear Time

## Definition

**O(n)** means the amount of work grows **linearly** with the input size.

If the input doubles, the work roughly doubles.

```text
n = 10       -> ~10 operations
n = 100      -> ~100 operations
n = 1,000    -> ~1,000 operations
```

## Example

```python
def print_numbers(numbers):
    for number in numbers:
        print(number)
```

If there are `n` elements, the loop runs `n` times.

```text
Time: O(n)
Space: O(1)
```

## Common Examples

### Linear Search

```python
def search(numbers, target):
    for number in numbers:
        if number == target:
            return True

    return False
```

Worst case:

```text
[10, 20, 30, 40, 50]
                ^
              target
```

Every element may need to be checked.

```text
Time: O(n)
```

### Finding Maximum

```python
def find_max(numbers):
    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum
```

Every element must be examined.

```text
Time: O(n)
```

## O(n) Visualization


::contentReference[oaicite:0]{index=0}


## O(n) vs O(1)

| O(1) | O(n) |
|---|---|
| Constant | Linear |
| Does not depend on input size | Grows with input size |
| `numbers[0]` | Loop through list |
| Dictionary lookup, average | Linear search |

```text
O(1)

Input grows
     |
     v
Work stays constant


O(n)

Input grows
     |
     v
Work grows proportionally
```

## O(n) vs O(n²)

```python
# O(n)
for i in range(n):
    pass
```

```python
# O(n²)
for i in range(n):
    for j in range(n):
        pass
```

The second loop executes `n` times for every iteration of the first loop.

```text
O(n)  -> n
O(n²) -> n * n
```

## Multiple O(n) Operations

```python
for x in numbers:
    pass

for x in numbers:
    pass
```

Technically:

```text
O(n + n)
= O(2n)
= O(n)
```

We drop constant factors.

## Important Interview Examples

```text
Linear Search          -> O(n)
Find minimum           -> O(n)
Find maximum           -> O(n)
Traverse linked list   -> O(n)
Two Pointers           -> O(n)
Sliding Window         -> O(n)
```

## Interview Question

**What is O(n) time complexity?**

> "O(n) means linear time. The amount of work grows proportionally with the input size. For example, traversing every element of a list takes O(n) time because each element may need to be visited once."

## Key Rule

```text
One complete pass through n elements
        |
        v
      O(n)
```