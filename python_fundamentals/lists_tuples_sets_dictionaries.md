# Lists, Tuples, Sets, Dictionaries

| Feature           | List                    | Tuple                             | Set             | Dictionary            |
| ----------------- | ----------------------- | --------------------------------- | --------------- | --------------------- |
| Ordered           | Yes                     | Yes                               | No              | Yes                   |
| Mutable           | Yes                     | No                                | Yes             | Yes                   |
| Allows duplicates | Yes                     | Yes                               | No              | Keys: No, Values: Yes |
| Indexing          | Yes                     | Yes                               | No              | By key                |
| Slicing           | Yes                     | Yes                               | No              | No                    |
| Syntax            | `[]`                    | `()`                              | `{}`            | `{key: value}`        |
| Empty creation    | `[]`                    | `()`                              | `set()`         | `{}`                  |
| Membership check  | O(n)                    | O(n)                              | O(1) average    | O(1) average          |
| Access            | O(1) by index           | O(1) by index                     | N/A             | O(1) average by key   |
| Insertion         | O(1) amortized (append) | Not supported                     | O(1) average    | O(1) average          |
| Deletion          | O(n) generally          | Not supported                     | O(1) average    | O(1) average          |
| Comprehension     | Yes                     | No (generator expression instead) | Yes             | Yes                   |
| Primary use       | Ordered collection      | Fixed collection                  | Unique elements | Key-value pairs       |
