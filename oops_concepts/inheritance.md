# Inheritance

## Definition

Inheritance is an OOP mechanism where a **child class derives properties and methods from a parent class**.

- Promotes code reuse.
- Allows specialization of existing behavior.
- Enables method overriding and polymorphism.
- Represents an **"is-a" relationship**.

## Syntax

```python
class Parent:
    def show(self):
        print("Parent")


class Child(Parent):
    pass


obj = Child()
obj.show()
```

Output:

```text
Parent
```

## Example

```python
class Vehicle:
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


car = Car()

car.start()   # inherited
car.drive()   # own method
```

The `Car` class inherits `start()` from `Vehicle`.

## How It Works

```python
class Vehicle:
    def start(self):
        print("Starting")


class Car(Vehicle):
    pass
```

When:

```python
car = Car()
car.start()
```

Python searches for `start()` approximately in this order:

```text
Car
  |
  v
Parent classes
  |
  v
object
```

Python uses the **Method Resolution Order (MRO)** to determine where attributes and methods are searched.

```python
print(Car.__mro__)
```

## `super()`

`super()` is commonly used to call functionality from the parent class.

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


car = Car("Toyota", "Camry")

print(car.brand)
print(car.model)
```

`super()` is especially important when extending parent behavior rather than completely replacing it.

## Types

### Single

One child inherits from one parent.

```python
class Animal:
    pass


class Dog(Animal):
    pass
```

```text
Animal
  |
 Dog
```

### Multilevel

A class inherits from a child class.

```python
class Animal:
    pass


class Mammal(Animal):
    pass


class Dog(Mammal):
    pass
```

```text
Animal
  |
Mammal
  |
 Dog
```

### Multiple

One child inherits from multiple parents.

```python
class Flyable:
    def fly(self):
        print("Flying")


class Swimmable:
    def swim(self):
        print("Swimming")


class Duck(Flyable, Swimmable):
    pass
```

```python
duck = Duck()

duck.fly()
duck.swim()
```

### Hierarchical

Multiple children inherit from the same parent.

```python
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    pass


class Cat(Animal):
    pass
```

```text
       Animal
       /    \
     Dog    Cat
```

### Hybrid

A combination of two or more inheritance types.

```text
        A
       / \
      B   C
       \ /
        D
```

## Method Overriding

A child class can provide its own implementation of a parent method.

```python
class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    def speak(self):
        print("Bark")


dog = Dog()
dog.speak()
```

Output:

```text
Bark
```

The child implementation overrides the parent implementation.

## MRO

MRO stands for **Method Resolution Order**.

It determines the order in which Python searches for methods and attributes.

```python
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(D.__mro__)
```

Python uses **C3 linearization** to calculate the MRO.

This becomes particularly important with multiple inheritance.

## Inheritance vs Composition

| Feature | Inheritance | Composition |
|---|---|---|
| Relationship | Is-a | Has-a |
| Reuse | Through parent class | Through contained objects |
| Coupling | Usually higher | Usually lower |
| Flexibility | Less flexible | More flexible |
| Example | `Car(Vehicle)` | `Car(Engine)` |
| Best for | Genuine hierarchical relationships | Combining independent behaviors |

Example:

```python
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()
```

A `Car` **has an** `Engine`, so composition is appropriate.

## Inheritance vs Polymorphism

- **Inheritance** provides the relationship and reuse mechanism.
- **Polymorphism** allows different objects to respond to the same interface differently.
- Method overriding often combines both.

```python
class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("Bark")


class Cat(Animal):
    def speak(self):
        print("Meow")
```

Both `Dog` and `Cat` can be treated as `Animal` objects while providing different implementations.

## Use Cases

- Reusing common behavior.
- Creating specialized versions of a class.
- Implementing framework base classes.
- Modeling genuine "is-a" relationships.
- Supporting method overriding.
- Implementing polymorphic behavior.

## Common Pitfalls

- Using inheritance only for code reuse when composition would be better.
- Creating deep inheritance hierarchies.
- Forgetting `super().__init__()`.
- Not understanding MRO in multiple inheritance.
- Overriding a method without preserving required parent behavior.
- Assuming inherited attributes are automatically private or protected.

## Interview Tips

- Clearly explain the **is-a relationship**.
- Know all five common inheritance forms.
- Be comfortable with `super()`.
- Understand method overriding.
- Know what MRO means and how to inspect it using `__mro__`.
- Mention that Python supports multiple inheritance.
- Be able to explain inheritance vs composition.
- Remember that every Python class ultimately derives from `object` unless using a special metaclass structure.

## Common Questions

### Q1. What is inheritance?

**Answer:** Inheritance allows a child class to acquire and extend the attributes and methods of a parent class. It promotes reuse and supports specialization and polymorphism.

### Q2. Why is inheritance used?

**Answer:** It is used to reuse common behavior, specialize existing classes, and model genuine "is-a" relationships.

### Q3. What types of inheritance are supported?

**Answer:** Python supports single, multilevel, multiple, hierarchical, and hybrid inheritance.

### Q4. What is method overriding?

**Answer:** Method overriding occurs when a child class provides its own implementation of a method already defined by its parent class.

### Q5. What is `super()`?

**Answer:** `super()` provides access to methods and attributes from a parent or next class in the MRO. It is commonly used to extend parent initialization or behavior.

### Q6. What is MRO?

**Answer:** MRO, or Method Resolution Order, is the order Python follows when searching for a method or attribute through a class hierarchy.

### Q7. Does Python support multiple inheritance?

**Answer:** Yes. A class can inherit from multiple parent classes. Python uses MRO, based on C3 linearization, to resolve the lookup order.

### Q8. Inheritance or composition?

**Answer:** Use inheritance for a genuine "is-a" relationship. Use composition for a "has-a" relationship or when you want more flexible and loosely coupled designs.

### Q9. What happens if both parent classes have the same method?

**Answer:** Python follows the MRO to determine which implementation is found first.

### Q10. Why use `super()` instead of directly calling the parent class?

**Answer:** `super()` respects the MRO and works better with multiple inheritance, making the class hierarchy more cooperative and maintainable.

## One-Line Answer

> **Inheritance allows a child class to reuse and extend the behavior of a parent class, supporting code reuse, specialization, overriding, and polymorphism.**