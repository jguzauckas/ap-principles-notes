# Modules

In Python (and many other programming languages), we use **modules** to provide a lot of pre-built functionality to our programs. This functionality is often in the form of classes, functions, and even constant values!

These modules are things that Python doesn't access in every program, as they would make the program unnecessarily more difficult to run. Therefore, we need to tell Python when we want to use one, so it loads all the required information.

All of the sample code provided in this file is in the import.py Python file for you to run, modify, and otherwise investigate.

---

## `import`

To tell Python we want to utilize a module, we use the `import` keyword. Simply enough, at the beginning of a Python file, you make the statement `import _` where the underscore would be replaced with the name of the module you would like. Here is an example with the basic module `math`:

```python
import math
```

Now when the program runs, it loads up information related to the `math` module to use when needed!

---

## `from`

Sometimes modules can have a lot of pieces, and we only need access to a certain piece rather than the whole thing. The keyword `from` in conjunction with our keyword `import` allows us to import only the certain piece. Here is an example using the module `datetime` where we only want the class `date` that it provides:

```python
from datetime import date
```

Now only things related to the `date` class from the `datetime` module are available to use in the program.

---

## `as`

As with our example above, some modules and/or components can have long names, and when we use things from those modules often, it becomes frustrating to constantly cite the whole name. The `as` keyword allows us to set a name to utilize a module (or component) throughout the program that is distinct from its original. We set this name at the same point we import the module. Here is an example with the `random` module:

```python
import random as rdm
```

Now we have both imported the `random` module and can refer to it from there on as `rdm` for simplicity.

---

## Using a Module

Once you have imported a module, you can use it by referencing it's name with the dot `.` operator. For example, our `math` module offers functions like `ceil()` which take a float and determine the integer just above it (i.e., 4.5 would be 5). To use it would look like the following:

```python
x = math.ceil(4.5)
```

As you can see, the `ceil()` function ends up getting used just like any other function we've written would, which parameters put into parentheses. In the coming sections, we'll check out the three modules briefly referenced here: `math`, `random`, and `datetime`.
