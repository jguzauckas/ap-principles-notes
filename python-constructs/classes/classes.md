# Object-Oriented Programming

Python is an object-oriented programming language, which means that when programming, we design things around groups of data, called **objects**.

In Python, we have a lot of built-in objects that we already have used, like `str` and our iterables: `tuple`, `list`, `set`, and `dict`. These are designed for us to use them as templates to hold our own information, like when we create any of these types of objects.

We call the framework a **class** and the actual times we use the class an **object**.

All of the sample code provided in this file is in the classes.py Python file for you to run, modify, and otherwise investigate.

---

## Classes

To program a framework, we use the keyword `class`. This syntax will look very similar to how we defined functions with `def`. Here is a very basic example of a class:

```python
class MyClass:
    num = 10
```

Following the class keyword, we give our class a name, and importantly, we distinguish classes from functions and variables by capitalizing the first letter of each word.

A framework is only so helpful though, until we start using to create objects in its image. After defining a class, we can create an object of its type using the class name as if it was a function:

```python
obj = MyClass()
```

Now the variable `obj` is an object of type `MyClass`. Now in our example, `MyClass` is very small and basic, so having an object is not that useful, but the object will contain all the features set out in the class. In this case, we have access to the variable `num` that was set to `10` inside of the class definition. We can access `num` using the dot operator `.` with our object:

```python
print(obj.num)
```

This produces the output:

```
10
```

Classes are almost always more complex than this, but we can build on this foundational example next by using our default functions.
