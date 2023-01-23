import json
import jsonpickle


class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    def __str__(self) -> str:
        return f"{self._name} is {self._age} years old."


people = [Person("Mr. G", 24), Person("Evan", 17)]

with open("people.json", "w") as my_file:
    json.dump(jsonpickle.dumps(people), my_file)

with open("people.json", "r") as my_file:
    new_people = jsonpickle.loads(json.load(my_file))

for person in people:
    print(person)
for person in new_people:
    print(person)
