# Using `jsonpickle`

`jsonpickle` is going to be used as an intermediate step in our JSON serializing/deserializing (encoding/decoding) process. It will help turn our objects into something that JSON can serialize/deserialize.

All of the sample code provided in this file is in the serializing.py Python file for you to run, modify, and otherwise investigate, as well as the person.json file!

---

## `json` and `jsonpickle` Workflow

To move an object from one program to another using a `.json` file, we have a certain workflow. Assuming you already have the object ready to go, here is the general flow:

Writing program:
`object` -> `jsonpickle` -> `json`

Reading program:
`json` -> `jsonpickle` -> `object`

You'll notice that these are the same flow, but reversed from one-another.

---

## Serializing Objects

`jsonpickle` has similar methods to `json`, except that we exclusively work with strings, and we let `json` continue to handle the actual files. Our first step is to `import` our modules:

```python
import json
import jsonpickle
```

In order to work with `jsonpickle` (for serializing **or** deserializing), we need a custom class to work with! Here is a basic Person class:

```python
class Person:
    def __init__(self, name:str, age:int) -> None:
        self._name = name
        self._age = age

    def __str__(self) -> str:
        return f"{self._name} is {self._age} years old."
```

We'll also need an object made from this class to serialize:

```python
p1 = Person("Mr. G", 24)
```

Now we are ready to serialize! If we went with our typical method using `json`, we wouldn't even be able to serialize it into a `str`. For example if you tried:

```python
dump_str = json.dumps(p1)
```

We'd get the following error:

```
TypeError: Object of type Person is not JSON serializable
```

This is where `jsonpickle` comes in. We need to save a translated string as an intermediate before we hand it off to JSON to serialize. To do this, we use the `jsonpickle.dumps` method:

```python
dump_str = jsonpickle.dumps(p1)
```

Now `jsonpickle` has converted the information into a `str` that has the form of a Python dictionary, which `json` will play much nicer with. So we can continue and use our typical `json.dump` method to turn this into a `.json` file:

```python
with open("person.json", "w") as my_file:
    json.dump(dump_str, my_file)
```

For those interested, we could have written this without an intermediate variable by nesting our functions. This is by means required, but is considered more efficient:

```python
with open("person.json", "w") as my_file:
    json.dump(jsonpickle.dumps(p1), my_file)
```

Note that while this works, it does become a little bit harder to read.
