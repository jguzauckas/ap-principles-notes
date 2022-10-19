# Default Class Functions

Due to the nature of programming, all classes will require some same basic functions to be effective. Here, we will talk about the two biggest ones, `__init__()` and `__str__()`.

All of the sample code provided in this file is in the default-functions.py Python file for you to run, modify, and otherwise investigate.

---

## `__init__()` Function

Classes can have functions inside of them similar to the functions we've already worked with. There are functions that are particular to classes though, and one of the core function is the initializing function, referenced as `__init__()`, which provides instructions for how to create an object of it's class.

Let's make a class with a little more to it, to display the use of the initializing function. A classic example is a class representing a person:

```python
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
```

There's a lot to break down in this example, let's start with the declaration of the initializing function on the second line. When defining an initializing function, the first parameter represents the object being created (which in this case is a `Person`), and we used the name `self` for that temporary variable.

After the first parameter, the rest are just traditional parameters that can be of many types. In this case, we picked two, `name` and `age`, and used our type hinting to let a reader know that we intend for them to be `str` and `int`, respectively.

Finally, the return type hint is `None`, as when we create an object we do not expect any information to be returned. This will be consistent.

On the last two lines, we use the dot operator `.` with our reference to the new object `self` to create two **attributes**, which are values unique to objects of our `Person` class. In this case, we gave our attributes the same name as the values we passed in, as we want attribute names to be reflective of the data they store.

Now we have a class that we can create objects of that are a little more substantial. The creation of an object of the `Person` class is much like our last object, but with syntax similar to our uses of functions:

```python
p1 = Person("Mr. G", 24)
```

Note that we had three parameters in our `__init__()` function, but only sent two values when we created an object. The first parameter, which we called `self` is automatically added in by Python when it goes to create the object, so we write in values starting with the second listed parameter, which in our case is `name`, and continue from there.

Just like our variable `num` in `MyClass`, we can use the dot operator `.` with our attributes `name` and `age` to get access to those pieces of information for our object as well:

```python
print(f"{p1.name} is {p1.age} years old!")
```

This produces the output:

```
Mr. G is 24 years old!
```

---

## `__str__()` Function

With the `__init__()` function, we have a way to better control the creation of objects of the class. Another aspect we want to control more is how Python converts an object to a string. We've seen solid examples of this when we print out an iterable like a `list`, and it converts to a nice string with square brackets and each of the elements separated by commas. When we make our own classes and objects, the outcome is not as nice:

```python
print(p1)
```

This converts `p1` to a string and produces the output:

```
<__main__.Person object at 0x000001B3BF87BEB0>
```

This doesn't tell us anything about the `name` and `age` of `p1`, and instead tells us the memory address that the object is stored at. This information isn't useless, but it is not at all what we were looking for in this case. Let's rewrite our `Person` class to have a `__str__()` function that gives us a more useful output:

```python
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old!"
```

Note that the `__init__()` function is unchanged from our previous class definition, and only the `__str__()` function is new.

Just like the `__init__()` function, the first (and this time only) parameter is a name we assign to represent the object in question, and the typical choice is `self`. For an `__str__()` function, we don't want any other parameters.

We also give the output type hint as `str`, as the base use of this function is to return a string representing the object.

For the actual definition, we use the `return` keyword and an f-string that incorporates the attributes we feel are important to the object. This could have been none, some, or all of our attributes as you see fit.

Now when we create a new `Person` object and try to print it out, we get more useful information:

```python
p2 = Person("Mr. G", 24)
print(p2)
```

This produces the output:

```
Mr. G is 24 years old!
```

Note that we didn't even have to call the `__str__()` function, Python does that for us when it realizes it wants to print the object.

This becomes especially more useful as we have to make more objects from a class, and need to print out these kinds of statements multiple times!
