# Person class with age property defined.
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


# Testing implementation of age property
p4 = Person("Mr. G", 24)
p4.age = 25
print(p4.age)

# Creating a coordinate class to create examples of two more properties.
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


# Testing coordinate class properties and __str__ function
c1 = Coordinate(3, 5)
print(f"x is {c1.x} and y is {c1.y}.")
c1.x = 2
c1.y = 6
print(f"x is {c1.x} and y is {c1.y}.")
print(c1)
