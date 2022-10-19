# Attributes and Properties

So far we've made classes that have **attributes**, which are assigned at creation. Often we want more dynamic and specific control of our information though, and to do that, we expand on our attributes to make them **properties**.

All of the sample code provided in this file is in the attributes-properties.py Python file for you to run, modify, and otherwise investigate.

---

## Properties - Getters and Setters

Oftentimes, we want specific control over two interactions with our information, in the form of **getters** and **setters**. Getters are functions that allow us to _get_ the value of a property, and setters are functions that allow us to _set_ the value of a property. Python has a way for us to do this a little more quickly than normal using the decorator `@`.

We'll do another expansion of our `Person` class, with getter and setter methods for the `age` property. We'll leave `name` as an attribute:

```python
class Person:
    class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self._age = age

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old!"

    @property
    def age(self) -> str:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if value >= 0:
            self._age = value
        else:
            print("Could not set age to {value}.")
```

Note first that when using `self` with the dot operator `.` and our variable `age`, we now have slightly different syntax. The underscore `_` essentially marks our attribute as private, which is needed to be a property.

Our `@` decorators tell Python to treat our new methods as getters and setters. The simple decorator `@property` is for getters, so the method that comes after it should be treated as a getter method for its variable. The setter decorator uses the dot operator `.` and the variable name to make clear what the following method is a setter method for.

Note the return types on the getter and setter methods. Getters return the value, so they have a return type, and setters just set it, so they have a return type of `None`.

The reason we use setters is to help make sure the values we are saving meet certain criteria. In the case of `age`, it would only make sense for `age` to be a positive number, so we use a conditional to check that that is the case before saving it to `_age`. If it doesn't meet the criteria, we do not save it, and in this case, we write a message to the user to let them know.

With those methods defined, we can easily get and set our property as a variable from outside of the class using the dot operator `.`:

```python
p5 = Person("Mr. G", 24)
p5.age = 25
print(p5.age)
```

This produces the output:

```
25
```

Note that even though in the class definition we had to use `_age`, whereas when we are working with objects of the class we can just use `age`, which is one of the advantages of setting up these property methods.

Let's check out one more example with a class that holds a coordinate pair (like for graphing!):

```python
class Coordinate:
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    def __str__(self) -> str:
        return f"({self._x}, {self._y})"

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, x: int) -> None:
        self._x = x

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, y: int) -> None:
        self._y = y
```

This class has two properties: an `x` value and a `y` value, just like a coordinate pair. We defined getter and setter methods for each value so that they can both be accessed and modified appropriately when needed. Let's test that out:

```python
c1 = Coordinate(3, 5)
print(f"x is {c1.x} and y is {c1.y}.")
c1.x = 2
c1.y = 6
print(f"x is {c1.x} and y is {c1.y}.")
print(c1)
```

This produces the output:

```
x is 3 and y is 5.
x is 2 and y is 6.
(2, 6)
```

In this case, we were able to _get_ the values of `x` and `y` in our f-strings to make statements about their current values, and could assign new values similar to how we'd assign a variable a new value. The last `print()` statement shows the `__str__()` method at work, turning the information into a nice string.
