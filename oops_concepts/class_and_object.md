# Class and Object

## Definition

### Class

A class is a **blueprint or template for creating objects**. It defines the attributes and behaviors that its objects can have.

### Object

An object is an **instance of a class**. It contains its own state and can use the behavior defined by the class.

```text
Class  = Blueprint
Object = Instance created from the blueprint
```

## Syntax

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"I am {self.name}")


person = Person("GK", 34)
person.introduce()
```

Here:

- `Person` is the class.
- `person` is an object.
- `name` and `age` are instance attributes.
- `introduce()` is an instance method.
- `__init__()` initializes the object.

## How It Works

When this executes:

```python
person = Person("GK", 34)
```

Python:

1. Creates a new `Person` object.
2. Calls `__init__()`.
3. Passes the object as `self`.
4. Stores `"GK"` in `self.name`.
5. Stores `34` in `self.age`.
6. Returns the object reference to `person`.

Conceptually:

```text
Person class
    |
    +---- person1 -> name="GK", age=34
    |
    +---- person2 -> name="John", age=30
```

Each object has its own instance state.

## Class Attributes

A class attribute belongs to the class and is shared by instances unless overridden.

```python
class Employee:
    company = "ABC"

    def __init__(self, name):
        self.name = name


e1 = Employee("GK")
e2 = Employee("John")

print(e1.company)
print(e2.company)
```

Both objects access the same class attribute.

## Instance Attributes

Instance attributes belong to a specific object.

```python
class Employee:
    def __init__(self, name):
        self.name = name


e1 = Employee("GK")
e2 = Employee("John")

print(e1.name)  # GK
print(e2.name)  # John
```

`e1.name` and `e2.name` are separate values.

## Class vs Object

| Feature  | Class                        | Object                                 |
| -------- | ---------------------------- | -------------------------------------- |
| Meaning  | Blueprint/template           | Instance of a class                    |
| Defines  | Attributes and methods       | Actual state and behavior              |
| Memory   | Class itself occupies memory | Each object has its own instance state |
| Creation | Defined using `class`        | Created by calling the class           |
| Example  | `Person`                     | `Person("GK", 34)`                     |
| Count    | Usually one class definition | Can create many objects                |

## Class vs Instance Attributes

| Feature    | Class Attribute               | Instance Attribute     |
| ---------- | ----------------------------- | ---------------------- |
| Belongs to | Class                         | Individual object      |
| Shared     | Usually yes                   | No                     |
| Defined    | Inside class, outside methods | Usually through `self` |
| Example    | `company`                     | `self.name`            |

Example:

```python
class Employee:
    company = "ABC"       # class attribute

    def __init__(self, name):
        self.name = name  # instance attribute
```

## `self`

`self` refers to the **current object instance**.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(self.name)
```

When:

```python
person = Person("GK")
person.greet()
```

Python effectively passes `person` to the method:

```python
Person.greet(person)
```

Therefore, `self.name` refers to that object's `name`.

## `__init__`

`__init__()` is an initializer that runs automatically after an object is created.

```python
class Person:
    def __init__(self, name):
        self.name = name
```

It is commonly used to initialize instance attributes.

Important interview point:

> `__init__()` initializes an object. It is not the method that actually creates the object.

Object creation is handled by `__new__()`.

## Object Identity

Every object has an identity.

```python
a = Person("GK")
b = Person("GK")

print(a is b)  # False
```

Although the objects may contain the same data, they are different objects.

Useful functions:

```python
id(a)
type(a)
isinstance(a, Person)
```

## Related Concepts

```text
Class
  |
  +-- Attributes
  |     +-- Class attributes
  |     +-- Instance attributes
  |
  +-- Methods
        +-- Instance methods
        +-- Class methods
        +-- Static methods

Object
  |
  +-- Identity
  +-- State
  +-- Behavior
```

## Object State and Behavior

An object generally consists of:

- **State** - data stored by the object.
- **Behavior** - operations the object can perform.
- **Identity** - unique identity of the object.

Example:

```python
class Car:
    def __init__(self, color):
        self.color = color

    def drive(self):
        print("Driving")
```

For:

```python
car = Car("Red")
```

- State: `color = "Red"`
- Behavior: `drive()`
- Identity: the specific `car` object

## Use Cases

Classes and objects are used to model:

- Users
- Employees
- Bank accounts
- Cars
- Orders
- Products
- API clients
- Test automation components
- Database entities

## Interview Tips

- Know the difference between a class and an object.
- Understand `self`.
- Know instance attributes vs class attributes.
- Know what `__init__()` does.
- Understand that multiple objects can be created from one class.
- Be able to explain object state, behavior, and identity.
- Know the difference between `is` and `==`.

## Common Questions

### Q1. What is a class?

**Answer:** A class is a blueprint that defines the attributes and methods that objects created from it can have.

### Q2. What is an object?

**Answer:** An object is an instance of a class with its own identity and instance state.

### Q3. What is the difference between a class and an object?

**Answer:** A class defines the structure and behavior, while an object is a concrete instance created from that class.

### Q4. What is `self`?

**Answer:** `self` refers to the current object instance and is used to access its instance attributes and methods.

### Q5. Can we create multiple objects from one class?

**Answer:** Yes. A single class can be used to create any number of objects, with each object potentially having different instance state.

### Q6. What is the difference between class and instance attributes?

**Answer:** Class attributes belong to the class and are generally shared by instances, while instance attributes belong to individual objects.

### Q7. What is `__init__()`?

**Answer:** `__init__()` is an initializer that runs after an object is created and is commonly used to initialize its instance attributes.

### Q8. Is `__init__()` a constructor?

**Answer:** It is commonly called a constructor in everyday Python discussions, but technically `__new__()` creates the object while `__init__()` initializes it.

### Q9. What is the difference between `is` and `==`?

**Answer:** `==` compares values for equality, while `is` checks whether two references point to the same object.

```python
a = [1, 2]
b = [1, 2]
c = a

a == b  # True
a is b  # False
a is c  # True
```

### Q10. What are the three characteristics of an object?

**Answer:** An object has identity, state, and behavior.

## One-Line Answers

- **Class:** A blueprint that defines attributes and behavior.
- **Object:** An instance of a class.
- **Instance:** A concrete object created from a class.
- **`self`:** Reference to the current object.
- **`__init__()`:** Initializes an object's state.
- **Class attribute:** Attribute shared by the class and normally accessible through its instances.
- **Instance attribute:** Attribute belonging to a specific object.