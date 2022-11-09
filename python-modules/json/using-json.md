# Using JSON

Now that we understand what JSON is, let's learn how to actually use it to store data!

All of the sample code provided in this file is in the using-json.py Python file for you to run, modify, and otherwise investigate, as well as the using-json.json file!

---

## Opening the file to access

We have to tell Python to open a JSON file to do anything with it. To do this, we will typically use the following:

```python
with open("filename.json", "r/w") as my_file:
    # Continue from here
```

In this snippet, the filename is the name of your JSON, so in this context it would be `using-json.json`.

The `"r/w"` is going to be either `"r"` for **r**eading from the file (to take in the data) or `"w"` for **w**riting to the file (to output data).

You can also use any temporary variable name you would like in place of `my_file`, as its just a shortcut due to the `as` keyword.

An example for us to write data in this context would look like this:

```python
with open("using-json.json", "w") as my_file:
    # Continue from here
```

---

## Encoding/Serializing Data

Now that we can open a file, let's learn how to write data into it. First step is having some data to write in, so let's define a brief dictionary and save it to a variable:

```python
my_dict = {"Mr. G": "Teacher", "Jeet": "Student"}
```

Now that we have data and can open a file, we need a way to make it write in JSON. To do this, we have the `json.dump()` method. This takes in two arguments: first, the data to write in (in this case our variable), and second, the name of the file.

```python
with open("using-json.json", "w") as my_file:
    json.dump(my_dict, my_file)
```

This will create the JSON file if it doesn't already exist, or write over existing data in the JSON file (so be careful!). Looking in our JSON file, we see this:

```json
{ "Mr. G": "Teacher", "Jeet": "Student" }
```

While much more rare, we can get an `str` in Python that represents the JSON information that would be encoded with `json.dumps()`, where the `s` is short for **string**! It only takes one argument, the data to convert, as it doesn't need to write to a file.

```python
my_str = json.dumps(my_dict)
print(my_str)
```

This produces the output:

```
{"Mr. G": "Teacher", "Jeet": "Student"}
```

Again, this is infrequently used, but has it's purposes nonetheless!

---

## Decoding/Deserializing Data

Now that we have a JSON file with data in it, we will want to be able to decode/deserialize it to use in Python! Now we will want to to use the `"r"` tag when opening our file, as we want to read data from it!

To take in data, we load it with the `json.load()` function. It takes in one parameter, the file to be loaded from. Though we will want to set it equal to a variable to store the data within our Python program!

```python
with open("using-json.json", "r") as my_file:
    data = json.load(my_file)

print(data)
```

This results in the following:

```
{'Mr. G': 'Teacher', 'Jeet': 'Student'}
```

We notice that the only thing different from the JSON file is that this uses Python's standard `'` for strings as opposed to `"`, even though both work!

Just like the nice case of `json.dumps()`, we have a niche case where we might want to read data from a string that is holding JSON-formatted data. This is where `json.loads()` comes in.

```python
data_str = json.loads(my_str)

print(data_str)
```

This results in the output:

```
{'Mr. G': 'Teacher', 'Jeet': 'Student'}
```

Using our JSON string from earlier, we decode it to reveal that we got the same output as putting it in a JSON file and then reading it back out!
