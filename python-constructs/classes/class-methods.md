# Functions vs. Methods

While there are a couple of standard functions like we've gone over, one of the most powerful parts of making classes is the ability to write functions that are more customized to your uses. We can make custom functions specifically for our classes, which we call **methods**.

All of the sample code provided in this file is in the class-methods.py Python file for you to run, modify, and otherwise investigate.

---

## Other Class Methods

Let's expand our `Person` class one more time to add another method:

```python
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old!"

    def hello(self) -> None:
        print(f"Hello {self.name}!")
```

The only thing that has changed from our previous `Person` class is two more lines, adding in the method `hello()`. Continuing the trend from our first two standard functions, we have to include the `self` parameter to utilize any information stored by the object. We also note the `None` return type hint as we just intend to print the information when the method is called.

To utilize this method, we use the dot operator `.` with our object to call this like we would any other function. We also don't need parameters, since Python handles the `self` parameter on its own:

```python
p3 = Person("Mr. G", 24)
p3.hello()
```

This produces the output:

```
Hello Mr. G!
```

The methods we add don't just need to print, they can return a value just like any other function. Let's add a `birthday()` function that returns the new age of a person:

```python
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old!"

    def birthday(self) -> int:
        return self.age + 1
```

Note that the birthday() function doesn't actually change the value of age, we'll look at those types of variables in attributes-properties.md

We can call our method in an f-string:

```python
p4 = Person("Mr. G", 24)
print(f"Next year, {p4.name} will be {p4.birthday()} years old!")
```

This produces the output:

```
Next year, Mr. G will be 25 years old!
```

With some additional tools, let's look at how we can store and change data in an object with attributes and properties.
