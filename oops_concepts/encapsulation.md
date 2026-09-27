 # Encapsulation

## Definition

Encapsulation is the OOP principle of **bundling data and the methods that operate on that data inside a class**, while controlling how the data is accessed or modified.

- Protects object state from unintended changes.
- Provides controlled access through methods or properties.
- Improves maintainability and reduces coupling.

## Syntax

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    @property
    def balance(self):
        return self._balance
```

## Example

```python
account = BankAccount(1000)

account.deposit(500)

print(account.balance)  # 1500
```

Instead of allowing arbitrary modification:

```python
account.balance = -5000
```

the class controls how the balance changes.

## How It Works

1. Data and behavior are grouped inside a class.
2. Internal state is conventionally marked as non-public.
3. Public methods or properties provide controlled access.
4. Validation can be performed before modifying the state.

```python
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
```

Here, `__salary` is name-mangled and should not be accessed directly.

## Access Levels

Python does not have strict `public`, `protected`, and `private` keywords like some languages.

| Syntax | Meaning | Access |
|---|---|---|
| `name` | Public | Anywhere |
| `_name` | Protected by convention | Internal/subclasses, but technically accessible |
| `__name` | Private-like | Name mangling is applied |

Example:

```python
class User:
    def __init__(self):
        self.name = "GK"
        self._role = "Admin"
        self.__password = "x"
```

## Property

`@property` is a common way to implement controlled access.

```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
```

Usage:

```python
person = Person(30)

print(person.age)

person.age = 35
```

The user interacts with `age` like an attribute, while the class controls access internally.

## Encapsulation vs Abstraction

| Feature | Encapsulation | Abstraction |
|---|---|---|
| Main idea | Protect and control data | Hide implementation complexity |
| Focus | Data and access | Essential behavior/interface |
| Common mechanism | Classes, properties | Abstract classes, protocols |
| Goal | Controlled state management | Simplified usage |

## Encapsulation vs Data Hiding

- **Encapsulation** means bundling data and behavior together and controlling access.
- **Data hiding** specifically means restricting or hiding internal implementation details.
- Data hiding is one aspect of encapsulation.

## Use Cases

- Validating object state
- Protecting sensitive or internal data
- Controlling how attributes are modified
- Maintaining object invariants
- Hiding implementation details
- Creating maintainable APIs
- Preventing accidental state changes

## Interview Tips

- Encapsulation is **not simply making variables private**.
- Python does not enforce traditional private/protected access modifiers.
- `_name` is a convention, not true access restriction.
- `__name` triggers **name mangling**, not absolute privacy.
- `@property` is often preferred over explicit getter/setter methods.
- Mention **controlled access, validation, and maintaining object state**.

## Common Questions

### Q1. What is encapsulation?

**Answer:** Encapsulation is the OOP principle of bundling data and the methods that operate on that data inside a class and controlling how the internal state is accessed or modified.

### Q2. How do you achieve encapsulation?

**Answer:** In Python, encapsulation is commonly achieved using classes, naming conventions such as `_attribute` and `__attribute`, and properties or methods that provide controlled access.

### Q3. Does Python support private variables?

**Answer:** Python does not provide strict private variables. A double underscore triggers name mangling, which makes direct accidental access harder but does not provide absolute privacy.

### Q4. What is name mangling?

**Answer:** Name mangling changes an attribute such as `__salary` to a class-specific form such as `_Employee__salary`, mainly to avoid accidental name conflicts.

### Q5. Why use encapsulation?

**Answer:** It protects object state, allows validation, hides implementation details, reduces accidental modification, and makes code easier to maintain.

### Q6. Is `_variable` private?

**Answer:** No. A single underscore indicates that the attribute is intended for internal use, but Python does not technically prevent external access.

### Q7. What is the difference between `__x` and `_x`?

**Answer:** `_x` is a convention indicating internal use, while `__x` triggers name mangling and makes accidental access or overriding less likely.

### Q8. Give a real-world example.

**Answer:** A bank account can encapsulate its balance and expose methods such as `deposit()` and `withdraw()`. This prevents callers from arbitrarily changing the balance and allows the class to validate transactions.

## One-Line Answer

> **Encapsulation means bundling data and behavior together while providing controlled access to an object's internal state.**