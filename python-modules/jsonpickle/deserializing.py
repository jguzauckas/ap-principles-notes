import json
import jsonpickle


class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    def __str__(self) -> str:
        return f"{self._name} is {self._age} years old."


with open("person.json", "r") as my_file:
    load_str = json.load(my_file)

p1 = jsonpickle.loads(load_str)
print(p1)


with open("person.json", "r") as my_file:
    p2 = jsonpickle.loads(json.load(my_file))

print(p2)
