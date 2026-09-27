# Time vs Space Complexity

## Definition

**Time complexity** describes how the **execution time/work** of an algorithm grows as input size increases.

**Space complexity** describes how the **memory usage** of an algorithm grows as input size increases.

```text
Time  -> How much work does it do?
Space -> How much extra memory does it need?
```

## Example 1 - O(n) Time, O(1) Space

```python
def find_max(numbers):
    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum
```

Analysis:

```text
Time:
Loop through n elements
-> O(n)

Space:
Only `maximum` is stored
-> O(1)
```

## Example 2 - O(n) Time, O(n) Space

```python
def double_numbers(numbers):
    result = []

    for number in numbers:
        result.append(number * 2)

    return result
```

Analysis:

```text
Time:
Loop through n elements
-> O(n)

Space:
Result contains n elements
-> O(n)
```

## Example 3 - O(n²) Time, O(1) Space

```python
def print_pairs(numbers):
    for i in numbers:
        for j in numbers:
            print(i, j)
```

Analysis:

```text
Time:
n * n
-> O(n²)

Space:
Only loop variables
-> O(1)
```

## Example 4 - O(n²) Time, O(n²) Space

```python
def create_matrix(n):
    matrix = []

    for i in range(n):
        row = []

        for j in range(n):
            row.append(0)

        matrix.append(row)

    return matrix
```

Analysis:

```text
Time:
n * n
-> O(n²)

Space:
n * n elements
-> O(n²)
```

## Quick Comparison

| Algorithm | Time | Extra Space |
|---|---:|---:|
| List index access | O(1) | O(1) |
| Linear search | O(n) | O(1) |
| Binary search | O(log n) | O(1) |
| Create a copy of list | O(n) | O(n) |
| Nested loops | O(n²) | O(1) |
| Create n x n matrix | O(n²) | O(n²) |

## Time-Space Tradeoff

Sometimes we use **more memory to reduce execution time**.

Example:

```python
def find_duplicates(numbers):
    seen = set()

    for number in numbers:
        if number in seen:
            return True

        seen.add(number)

    return False
```

Complexity:

```text
Time  -> O(n) average
Space -> O(n)
```

The `set` uses extra memory, but it gives fast average O(1) membership checks.

Without extra memory, a brute-force approach could be:

```text
Time  -> O(n²)
Space -> O(1)
```

So:

```text
More memory
     |
     v
Potentially less computation

Less memory
     |
     v
Potentially more computation
```

## Important Interview Point

**Space complexity** can sometimes refer to total memory usage, but in algorithm interviews it usually means **auxiliary space**, the extra memory used by the algorithm excluding the input itself.

For example:

```python
def find_max(numbers):
    maximum = numbers[0]
```

The input list already exists, so we normally count only the additional variable:

```text
Auxiliary Space -> O(1)
```

## Time vs Space

| | Time Complexity | Space Complexity |
|---|---|---|
| Measures | Computation/work | Memory usage |
| Question | How much work? | How much extra memory? |
| Example | O(n) | O(n) |
| Main concern | Performance | Memory consumption |
| Can trade off? | Yes | Yes |

## Interview Answer

> "Time complexity describes how the execution work grows with input size, while space complexity describes how the memory required by the algorithm grows with input size. For example, a linear search takes O(n) time and O(1) auxiliary space."

## Key Rule

```text
Time  -> How much work?
Space -> How much extra memory?
```