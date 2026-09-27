# Hashing

## Definition

**Hashing** is a technique that converts a key into a fixed-size value called a **hash** using a hash function.

```text
Key
 |
 v
Hash Function
 |
 v
Hash Value
 |
 v
Hash Table
```

Example:

```python
key = "apple"

hash_value = hash(key)

print(hash_value)
```

The hash value is used to efficiently store and retrieve data.

## Hash Function

A good hash function should:

- Be deterministic
- Be fast to calculate
- Distribute keys evenly
- Minimize collisions
- Produce the same hash for the same key during a run

Example concept:

```python
def simple_hash(key, size):
    return sum(ord(char) for char in key) % size
```

## Hash Table

A **hash table** stores key-value pairs using the hash of the key to determine where the value should be stored.

Python's:

- `dict`
- `set`

are hash-table-based data structures.

```python
users = {
    "alice": 100,
    "bob": 200
}

print(users["alice"])
```

Conceptually:

```text
"alice"
   |
   v
hash("alice")
   |
   v
Index
   |
   v
100
```

## Collision

A **collision** occurs when two different keys produce the same hash-table location.

```text
Key A ----\
           -> Same Index
Key B ----/
```

A good hash function reduces collisions but cannot always eliminate them.

## Collision Handling

### 1. Separate Chaining

Multiple elements can be stored in a bucket.

```text
Index 0 -> [A] -> [B]
Index 1 -> [C]
Index 2 -> [D] -> [E]
```

### 2. Open Addressing

If a position is occupied, find another available position.

Common techniques:

- Linear probing
- Quadratic probing
- Double hashing

```text
Index 5 -> occupied
Index 6 -> occupied
Index 7 -> available
```

## Hashing Complexity

For a well-designed hash table:

| Operation | Average | Worst |
| --------- | ------: | ----: |
| Search    |    O(1) |  O(n) |
| Insert    |    O(1) |  O(n) |
| Delete    |    O(1) |  O(n) |

The worst case can occur when many keys collide.

## Hashable Objects

Dictionary keys and set elements must be **hashable**.

Common hashable types:

```python
int
float
str
tuple
frozenset
```

Usually not hashable:

```python
list
dict
set
```

Example:

```python
data = {
    (1, 2): "valid"
}

data = {
    [1, 2]: "invalid"
}
# TypeError: unhashable type: 'list'
```

## `__hash__` and `__eq__`

Python objects can define:

```python
__hash__()
__eq__()
```

For dictionary/set behavior, an important rule is:

```text
If a == b
then hash(a) == hash(b)
```

The reverse is not required:

```text
hash(a) == hash(b)
does NOT mean
a == b
```

This is because collisions are possible.

## Hashing vs Encryption

| Feature      | Hashing                          | Encryption                                     |
| ------------ | -------------------------------- | ---------------------------------------------- |
| Purpose      | Data fingerprint / lookup        | Protect data confidentiality                   |
| Reversible   | No                               | Yes, with the key                              |
| Key required | Usually no                       | Yes                                            |
| Same input   | Same hash for deterministic hash | Can produce different ciphertext with nonce/IV |
| Example      | SHA-256                          | AES                                            |

## Hashing vs Hash Table

These are different concepts:

```text
Hashing
    |
    v
Hash Function
    |
    v
Hash Value

Hash Table
    |
    v
Uses hashing for efficient storage and lookup
```

## Common Applications

- Python dictionaries
- Python sets
- Caches
- Database indexing
- Duplicate detection
- Symbol tables
- Fast lookup
- Distributed systems
- Password storage

## Hashing for Passwords

Passwords should **not** normally be stored using a fast general-purpose hash such as SHA-256 alone.

Password storage should use dedicated password-hashing algorithms such as:

- Argon2
- bcrypt
- scrypt
- PBKDF2

These are deliberately expensive to make brute-force attacks harder.

## Cryptographic Hash Functions

Common cryptographic hash functions include:

```text
SHA-256
SHA-512
SHA-3
```

Example:

```python
import hashlib

value = "hello"

digest = hashlib.sha256(value.encode()).hexdigest()

print(digest)
```

## Hashing vs Searching

| Requirement          | Suitable Approach |
| -------------------- | ----------------- |
| Search unsorted list | Linear Search     |
| Search sorted list   | Binary Search     |
| Frequent key lookup  | Hash Table        |
| Unique values        | Set               |
| Key-value mapping    | Dictionary        |

## Interview Points

- Hashing converts a key into a hash value.
- Hash tables use hashing for fast lookup.
- Average dictionary/set lookup is O(1).
- Collisions occur when different keys map to the same location.
- Collision handling can use chaining or open addressing.
- Dictionary keys must be hashable.
- Mutable objects such as lists cannot normally be dictionary keys.
- Hashing is different from encryption.
- Hashing is also different from cryptographic hashing.

## Common Interview Questions

**Why is dictionary lookup O(1) on average?**

Because the dictionary uses the key's hash to locate the corresponding entry without scanning all keys.

**What is a collision?**

When two different keys map to the same hash-table location.

**Can two different objects have the same hash?**

Yes. This is called a collision.

**If two objects are equal, must their hashes be equal?**

Yes.

```text
a == b
    =>
hash(a) == hash(b)
```

But:

```text
hash(a) == hash(b)
    does not imply
a == b
```

**Why can't a list be a dictionary key?**

Because lists are mutable and therefore unhashable.

# Interview Priority

```text
P1:
- Hashing concept
- Hash function
- Hash table
- Collision
- Collision handling
- O(1) average lookup
- Dictionary and Set
- Hashable vs unhashable

P2:
- __hash__ and __eq__
- Chaining
- Open addressing
- Load factor

P3:
- Cryptographic hashing
- SHA-256
- Password hashing
- Consistent hashing
```