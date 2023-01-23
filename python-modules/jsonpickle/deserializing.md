# Using `jsonpickle`

`jsonpickle` is going to be used as an intermediate step in our JSON serializing/deserializing (encoding/decoding) process. It will help turn our objects into something that JSON can serialize/deserialize.

All of the sample code provided in this file is in the deserializing.py Python file for you to run, modify, and otherwise investigate, as well as the person.json file!

---

## `json` and `jsonpickle` Workflow

To move an object from one program to another using a `.json` file, we have a certain workflow. Assuming you already have the object ready to go, here is the general flow:

Writing program:
`object` -> `jsonpickle` -> `json`

Reading program:
`json` -> `jsonpickle` -> `object`

You'll notice that these are the same flow, but reversed from one-another.

---

## Deserializing Objects

Given a `.json` file with some `jsonpickle.dumps` encoded objects, we can deserialize them by using `json` and `jsonpickle` in tandem. This time we are going to reverse the order from our encoding. First step is to `import` our module:

```python
import json
import jsonpickle
```

If you want to use `jsonpickle` to turn a `.json` back into an `object`, you need to have similarly defined code to your object in the other file as well. When we say "similarly-defined", we mean that it has the same class name, and same instance variable/parameter names, otherwise this won't work. So we will repeat our `Person` class by copying it (though we could have given it some different methods if we needed):

```python
class Person:
    def __init__(self, name:str, age:int) -> None:
        self._name = name
        self._age = age

    def __str__(self) -> str:
        return f"{self._name} is {self._age} years old."
```

Now we follow our reversed workflow, first by reading the file into a `json` string:

```python
with open("person.json", "r") as my_file:
    load_str = json.load(my_file)
```

Now we use `jsonpickle` as our intermediate to translate this back into a `Person` object for us to use:

```python
p1 = jsonpickle.loads(load_str)
print(p1)
```

This produces the output:

```
Mr. G is 24 years old.
```

We can see based on how it printed `p1` that it correctly turned it back into a `Person` object!

Just like with serializing, we could have condensed this to fewer lines to make it more efficient, at the cost of readability:

```python
with open("person.json", "r") as my_file:
    p2 = jsonpickle.loads(json.load(my_file))

print(p2)
```

This produces the same output!
