# JSON

**JSON** is an acronym which stands for **J**ava**S**cript **O**bject **N**otation.

In it's simplest form, JSON is a standard way to move data between programs more easily than just a normal text file.

All of the sample code provided in this file is in the json-basics.py Python file for you to run, modify, and otherwise investigate, as well as the json-basics.json file!

---

## `import`

To use JSON, we need to import it:

```python
import json
```

---

## Type Conversions

Unfortunately, since **JavaScript** is in the name, JSON was not made for Python. So even though it works, there is not a perfect translation of types from Python to JSON and vice-a-versa. That being said, we can accomplish a lot with JSON.

In order to put data into a JSON, Python has to **encode** or **serialize** it. On the other end, to take data out of a JSON, Python has to **decode** or **deserialize** it.

For the time being, we will stick to our basic types (things like `int`, `str`, etc.) and will talk about class objects in a future class. Here is a table stating how Python and JSON interact with types:

| Python before Serialize |  JSON  | Python after Deserialize |
| ----------------------- | :----: | -----------------------: |
| `dict`                  | Object |                   `dict` |
| `list`, `tuple`         | Array  |                   `list` |
| `str`                   | String |                    `str` |
| `int`                   | Number |                    `int` |
| `float`                 | Number |                  `float` |
| `True`                  |  true  |                   `True` |
| `False`                 | false  |                  `False` |
| `None`                  |  null  |                   `None` |

As we can see, JSON has a different interpretation of the Python types, but fortunately that turns out to be mostly in name, as we can see most cases are able to convert back to the correct Python type! The only exception is `tuple`, which will return to Python as a `list`, but this is manageable!

---

## Type Examples

Let's look at some basic examples of types and how they convert to JSON:

`int`:

```python
5
```

In JSON this would look like:

```json
5
```

Obviously, this does not look different, which is part of the power of JSON! This is similar for most of our basic types: `int`, `float`, and `bool`.

Let's look at `str`:

```python
"Hello World!"
```

In JSON this would look like:

```json
"Hello World!"
```

This is also not different, but wanted to demonstrate the quotes still being present. Just like Python, JSON uses the quotes to determine if something is a string!

Now for the more powerful reason we use JSON to transfer data: iterables.

Let's start with lists:

```python
[1, 2, 3]
```

In JSON this would look like:

```json
[1, 2, 3]
```

This looks just like our list! One thing to note is that if we had a `tuple `made up of the same elements, the JSON output would not change, as JSON does not differentiate between a `list` and a `tuple`!

Finally, dictionaries also work as we'd expect:

```python
{"Mr. G": "Teacher", "Saad": "Student"}
```

In JSON this would look like:

```json
{ "Mr. G": "Teacher", "Saad": "Student" }
```

As all of our values were barely changed when written in JSON, JSON is also useful for humans as it is a fairly readable output!
