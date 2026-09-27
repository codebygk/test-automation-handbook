# SQL - Second Highest Salary

This is a very common SQL interview question.

Assume:

```text
Employee
+----+--------+
| id | salary |
+----+--------+
| 1  | 50000  |
| 2  | 80000  |
| 3  | 60000  |
| 4  | 80000  |
| 5  | 40000  |
+----+--------+
```

## 1. Using DISTINCT + LIMIT

For MySQL/PostgreSQL:

```sql
SELECT DISTINCT salary
FROM Employee
ORDER BY salary DESC
LIMIT 1 OFFSET 1;
```

Result:

```text
60000
```

`DISTINCT` is important because there can be duplicate highest salaries.

---

## 2. Using MAX()

```sql
SELECT MAX(salary) AS second_highest_salary
FROM Employee
WHERE salary < (
    SELECT MAX(salary)
    FROM Employee
);
```

How it works:

```text
1. Find highest salary
2. Ignore salaries equal to the highest
3. Find MAX() from the remaining salaries
```

This is a very good interview solution because it clearly handles duplicates.

---

## 3. Using DENSE_RANK()

```sql
SELECT salary
FROM (
    SELECT
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
    FROM Employee
) ranked
WHERE salary_rank = 2;
```

Result:

```text
60000
```

If multiple employees have the second-highest salary, this returns all of them.

Example:

```text
50000
80000
60000
60000
40000
```

Result:

```text
60000
60000
```

---

# If You Need the Employee Details

```sql
SELECT *
FROM Employee
WHERE salary = (
    SELECT MAX(salary)
    FROM Employee
    WHERE salary < (
        SELECT MAX(salary)
        FROM Employee
    )
);
```

This returns all employees having the second-highest salary.

---

# ROW_NUMBER vs RANK vs DENSE_RANK

This is an important interview follow-up.

```sql
DENSE_RANK() OVER (ORDER BY salary DESC)
```

For:

```text
80000
80000
60000
50000
```

Ranks:

```text
salary   DENSE_RANK
80000    1
80000    1
60000    2
50000    3
```

`RANK()`:

```text
salary   RANK
80000    1
80000    1
60000    3
50000    4
```

`ROW_NUMBER()`:

```text
salary   ROW_NUMBER
80000    1
80000    2
60000    3
50000    4
```

So for finding the **second distinct highest salary**, `DENSE_RANK()` is usually the right window function.

# Interview Answer

> "I would use DENSE_RANK when I need the second distinct highest salary because duplicate salaries should have the same rank."

```sql
SELECT salary
FROM (
    SELECT
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM Employee
) t
WHERE rnk = 2;
```

# Quick Comparison

| Approach           | Handles Duplicates               | Returns            |
| ------------------ | -------------------------------- | ------------------ |
| `DISTINCT + LIMIT` | Yes                              | Salary             |
| `MAX() + subquery` | Yes                              | Salary             |
| `DENSE_RANK()`     | Yes                              | Salary / employees |
| `ROW_NUMBER()`     | No, treats duplicates separately | Specific row       |

For interviews, know **`MAX() + subquery`** and **`DENSE_RANK()`** especially well.