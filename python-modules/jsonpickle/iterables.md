# Using `jsonpickle` with iterables

Oftentimes we want to use more than just one object at a time, we might want to work with a list, tuple, set, or dictionary of them! Fortunately, `jsonpickle` works very well with iterables!

All of the sample code provided in this file is in the iterables.py Python file for you to run, modify, and otherwise investigate, as well as the people.json file!

---

## `json` and `jsonpickle` Workflow

To move an object from one program to another using a `.json` file, we have a certain workflow. Assuming you already have the object ready to go, here is the general flow:

Writing program:
`object iterable` -> `jsonpickle` -> `json`

Reading program:
`json` -> `jsonpickle` -> `object iterable`

You'll notice that these are the same flow, but reversed from one-another.

---

## Serializing an Iterable of Objects

As usual, let's start with `import` for our modules:

```python
import json
import jsonpickle
```

Let's make a Person class to work with:

```python
class Person:
    def __init__(self, name:str, age:int) -> None:
        self._name = name
        self._age = age

    def __str__(self) -> str:
        return f"{self._name} is {self._age} years old."
```

Let's make a simple iterable of Person objects to demonstrate:

```python
people = [Person("Mr. G", 24), Person("Evan", 17)]
```

From this point on, this shouldn't feel any different from serializing a single object:

```python
with open("people.json", "w") as my_file:
    json.dump(jsonpickle.dumps(people), my_file)
```

---

## Deserializing an Iterable of Objects

If we were in a different file, we would need to re-`import` our modules and redefine our `Person` class. In this case we have not left the file, so we will skip that step.

To take in an iterable of objects, it looks no different from a single object:

```python
with open("people.json", "r") as my_file:
    new_people = jsonpickle.loads(json.load(my_file))
```

We can see this works by iterating through both iterables and seeing that they print the same information:

```python
for person in people:
    print(person)
for person in new_people:
    print(person)
```

This produces the output:

```
Mr. G is 24 years old.
Evan is 17 years old.
Mr. G is 24 years old.
Evan is 17 years old.
```
