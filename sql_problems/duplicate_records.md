# SQL - Duplicate Records

Assume:

```text
Employee
+----+----------+-------------------+
| id | name     | email             |
+----+----------+-------------------+
| 1  | John     | john@test.com     |
| 2  | Alice    | alice@test.com    |
| 3  | John     | john@test.com     |
| 4  | Bob      | bob@test.com      |
| 5  | John     | john@test.com     |
+----+----------+-------------------+
```

## 1. Find Duplicate Records

Using `GROUP BY` + `HAVING`:

```sql
SELECT name, email, COUNT(*) AS count
FROM Employee
GROUP BY name, email
HAVING COUNT(*) > 1;
```

Result:

```text
John | john@test.com | 3
```

### Why?

```text
GROUP BY  -> Groups identical values
COUNT(*)  -> Counts records in each group
HAVING    -> Filters groups
```

Important:

```sql
WHERE
```

filters rows **before** grouping.

```sql
HAVING
```

filters groups **after** grouping.

---

# 2. Find Duplicate Emails

```sql
SELECT email, COUNT(*) AS count
FROM Employee
GROUP BY email
HAVING COUNT(*) > 1;
```

---

# 3. Find Complete Duplicate Rows

If the combination of `name` and `email` defines a duplicate:

```sql
SELECT name, email, COUNT(*) AS count
FROM Employee
GROUP BY name, email
HAVING COUNT(*) > 1;
```

If more columns define uniqueness, include them:

```sql
SELECT name, email, department, salary, COUNT(*) AS count
FROM Employee
GROUP BY name, email, department, salary
HAVING COUNT(*) > 1;
```

---

# 4. Get the Actual Duplicate Rows

`GROUP BY` tells you which values are duplicated.

If you want the actual rows:

```sql
SELECT *
FROM Employee
WHERE email IN (
    SELECT email
    FROM Employee
    GROUP BY email
    HAVING COUNT(*) > 1
);
```

This returns every row whose email is duplicated.

---

# 5. Find Duplicate Rows Using ROW_NUMBER()

Useful when you need to identify which occurrence should be kept/deleted.

```sql
SELECT *,
       ROW_NUMBER() OVER (
           PARTITION BY email
           ORDER BY id
       ) AS rn
FROM Employee;
```

Result conceptually:

```text
id   email             rn
1    john@test.com     1
3    john@test.com     2
5    john@test.com     3
2    alice@test.com    1
4    bob@test.com      1
```

Rows where:

```sql
rn > 1
```

are duplicate occurrences.

---

# 6. Delete Duplicate Records

A common interview approach:

```sql
DELETE FROM Employee
WHERE id IN (
    SELECT id
    FROM (
        SELECT id,
               ROW_NUMBER() OVER (
                   PARTITION BY email
                   ORDER BY id
               ) AS rn
        FROM Employee
    ) t
    WHERE rn > 1
);
```

This keeps the first record and deletes subsequent duplicates.

Conceptually:

```text
id 1 -> Keep
id 3 -> Delete
id 5 -> Delete
```

Always verify the rows with the equivalent `SELECT` before executing a `DELETE`.

---

# 7. GROUP BY vs ROW_NUMBER()

| Requirement                               | Approach                        |
| ----------------------------------------- | ------------------------------- |
| Find which values are duplicated          | `GROUP BY + HAVING`             |
| Count duplicates                          | `GROUP BY + COUNT()`            |
| Retrieve all duplicate rows               | `GROUP BY` + subquery           |
| Identify individual duplicate occurrences | `ROW_NUMBER()`                  |
| Keep first, remove subsequent duplicates  | `ROW_NUMBER()`                  |
| Find duplicate based on multiple columns  | `PARTITION BY` multiple columns |

---

# 8. Duplicate Based on Multiple Columns

Suppose a duplicate means the same:

```text
name + email + department
```

Use:

```sql
SELECT name, email, department, COUNT(*) AS count
FROM Employee
GROUP BY name, email, department
HAVING COUNT(*) > 1;
```

With `ROW_NUMBER()`:

```sql
SELECT *,
       ROW_NUMBER() OVER (
           PARTITION BY name, email, department
           ORDER BY id
       ) AS rn
FROM Employee;
```

---

# Interview Answer

If asked:

**"How do you find duplicate records?"**

A concise answer:

> "I use GROUP BY on the columns that define a duplicate and HAVING COUNT(*) > 1."

```sql
SELECT email, COUNT(*) AS count
FROM Employee
GROUP BY email
HAVING COUNT(*) > 1;
```

If asked:

**"How do you identify and remove duplicate rows while keeping one?"**

Use:

```sql
ROW_NUMBER() OVER (
    PARTITION BY email
    ORDER BY id
)
```

and remove rows where:

```text
ROW_NUMBER > 1
```

## Quick Revision

```text
Find duplicates:
    GROUP BY + HAVING COUNT(*) > 1

Get duplicate rows:
    WHERE column IN (
        SELECT column
        GROUP BY column
        HAVING COUNT(*) > 1
    )

Identify duplicate occurrences:
    ROW_NUMBER() OVER (
        PARTITION BY column
        ORDER BY id
    )

Delete duplicates:
    DELETE rows WHERE ROW_NUMBER() > 1
```