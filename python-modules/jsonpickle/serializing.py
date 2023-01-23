import json
import jsonpickle


class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    def __str__(self) -> str:
        return f"{self._name} is {self._age} years old."


p1 = Person("Mr. G", 24)

# dump_str = json.dumps(p1)

dump_str = jsonpickle.dumps(p1)

with open("person.json", "w") as my_file:
    json.dump(dump_str, my_file)

with open("person.json", "w") as my_file:
    json.dump(jsonpickle.dumps(p1), my_file)

