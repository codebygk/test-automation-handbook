# Queue

## Definition

A **queue** is a linear data structure that follows **FIFO**:

**First In, First Out**

The element added first is removed first.

```text
Enqueue 10
Enqueue 20
Enqueue 30

Front                  Rear
  |                      |
  v                      v
 10 -> 20 -> 30

Dequeue -> 10
```

## Key Operations

| Operation | Meaning | Complexity |
|---|---|---:|
| `enqueue` | Add element to rear | O(1) |
| `dequeue` | Remove element from front | O(1) with `deque` |
| `peek` | View front element | O(1) |
| `is_empty` | Check whether empty | O(1) |

## Using Deque

Python's `collections.deque` is the preferred implementation.

```python
from collections import deque

queue = deque()

queue.append(10)       # Enqueue
queue.append(20)
queue.append(30)

print(queue[0])        # Peek -> 10

print(queue.popleft()) # Dequeue -> 10
print(queue.popleft()) # Dequeue -> 20
```

## Why Not Use a List?

You can technically use a list:

```python
queue = []

queue.append(10)
queue.append(20)

queue.pop(0)
```

But `pop(0)` is **O(n)** because all remaining elements need to be shifted.

Use `deque` instead:

```python
queue.popleft()  # O(1)
```

## Common Applications

- Task scheduling
- Print queues
- Request processing
- Message queues
- Breadth-First Search (BFS)
- Producer-consumer systems
- Job processing
- Rate limiting

## Queue vs Stack

| Feature | Queue | Stack |
|---|---|---|
| Principle | FIFO | LIFO |
| Add | Rear | Top |
| Remove | Front | Top |
| Python | `deque` | `list` / `deque` |
| Common use | BFS, scheduling | DFS, backtracking |

## Types of Queues

### Simple Queue

```text
Front -> [10] [20] [30] <- Rear
```

FIFO behavior.

### Circular Queue

The rear can wrap around to the beginning when space becomes available.

Useful for fixed-size buffers.

### Priority Queue

Elements are removed according to priority rather than insertion order.

Python provides `heapq` for heap-based priority queues.

```python
import heapq

queue = []

heapq.heappush(queue, (2, "Medium"))
heapq.heappush(queue, (1, "High"))
heapq.heappush(queue, (3, "Low"))

print(heapq.heappop(queue))  # (1, "High")
```

## Interview Points

- Queue follows **FIFO**.
- `enqueue` adds to the rear.
- `dequeue` removes from the front.
- `deque` is preferred for efficient queue operations.
- `list.pop(0)` is O(n).
- `deque.popleft()` is O(1).
- BFS commonly uses a queue.
- Priority Queue is different from a normal FIFO queue.

## Common Interview Question

**How would you implement a queue in Python?**

```python
from collections import deque

queue = deque()

queue.append(10)
queue.append(20)

front = queue[0]
value = queue.popleft()
```

**Why is `deque` preferred over `list` for queues?**

Because removing from the left with `popleft()` is O(1), while `list.pop(0)` is O(n).