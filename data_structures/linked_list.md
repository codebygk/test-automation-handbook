# Linked List

## Definition

A **linked list** is a linear data structure where elements are stored in **nodes**.

Each node contains:

- Data
- Reference to the next node

```text
[10 | next] -> [20 | next] -> [30 | None]
```

Unlike arrays/lists, linked-list elements do not need to be stored next to each other in memory.

## Node

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

## Singly Linked List

```python
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node
```

Usage:

```python
linked_list = LinkedList()

linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
```

Structure:

```text
head
 |
 v
[10] -> [20] -> [30] -> None
```

## Types

### Singly Linked List

Each node points to the next node.

```text
10 -> 20 -> 30 -> None
```

### Doubly Linked List

Each node points to both previous and next nodes.

```text
None <- 10 <-> 20 <-> 30 -> None
```

### Circular Linked List

The last node points back to the first node.

```text
10 -> 20 -> 30
^           |
|___________|
```

## Time Complexity

For a singly linked list:

| Operation | Complexity |
|---|---:|
| Access by index | O(n) |
| Search | O(n) |
| Insert at beginning | O(1) |
| Delete at beginning | O(1) |
| Insert after known node | O(1) |
| Delete after known node | O(1) |
| Insert at end | O(n) |
| Delete at end | O(n) |

If a tail pointer is maintained, insertion at the end can be O(1).

## Linked List vs Array/List

| Feature | Linked List | Array / Python List |
|---|---|---|
| Memory layout | Non-contiguous | Contiguous |
| Index access | O(n) | O(1) |
| Insert at beginning | O(1) | O(n) |
| Delete at beginning | O(1) | O(n) |
| Search | O(n) | O(n) |
| Memory overhead | Higher | Lower |
| Cache locality | Poorer | Better |
| Random access | No | Yes |
| Resizing | Node-by-node | Dynamic resizing |

## Advantages

- Efficient insertion/deletion when the node position is known
- No need for contiguous memory
- Dynamic size
- Useful for implementing other data structures

## Disadvantages

- No direct/random access
- Extra memory required for references
- More complex than arrays/lists
- Poorer cache locality
- Searching requires traversal

## Common Applications

- Implementing stacks and queues
- Graph adjacency lists
- LRU cache components
- Memory management concepts
- Polynomial representation
- Hash table chaining

## Interview Points

- A linked list consists of nodes connected through references.
- The first node is called the **head**.
- A singly linked list node contains data and a reference to the next node.
- Linked lists provide O(1) insertion/deletion when the relevant node/reference is already known.
- Access by index is O(n).
- Python's built-in `list` is **not** a linked list. It is a dynamic array.
- `collections.deque` is implemented using a doubly linked structure of blocks and is usually preferred for efficient operations at both ends.

## Common Interview Question

**Why is accessing the 5th element O(n) in a linked list?**

Because there is no direct index-based access. You must start at the head and follow the `next` references until you reach the required node.

**When would you choose a linked list over an array?**

When frequent insertions/deletions are required and direct random access is not important.