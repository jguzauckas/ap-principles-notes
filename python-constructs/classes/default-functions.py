# For more information on these samples, please see the
# default-functions.md file, which has descriptions for everything

# Person class with __init__()
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


# Create person object utilizing __init__()
p1 = Person("Mr. G", 24)

# Utilize the attributes of the person object
print(f"{p1.name} is {p1.age} years old!")

# Printing an object doesn't work very well
print(p1)

# Person class with __init__() and __str__()
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old!"

# Create another person object
p2 = Person("Mr. G", 24)

# Demonstrate use of __str__()
print(p2)