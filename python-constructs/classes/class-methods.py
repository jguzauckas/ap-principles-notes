class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old!"

    def hello(self) -> None:
        print(f"Hello {self.name}!")


p3 = Person("Mr. G", 24)
p3.hello()


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old!"

    def birthday(self) -> int:
        return self.age + 1


p4 = Person("Mr. G", 24)
print(f"Next year, {p4.name} will be {p4.birthday()} years old!")
