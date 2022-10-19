# Functions

In programming, we often want to do things multiple times. A lot of those times, loops fulfill our needs as they repeat instructions a bunch of times. A lot of other times though, we might want to do something multiple times, but not all at once, and potentially at different points in a program.

In those cases where we might repeat some actions at different points in a program, we have **functions**.

The functions.py file has all the sample code from this markdown file for you to run and modify as you'd like to get a better sense of how they work!

---

## `def`

We can tell Python where we want to **def**ine a function using `def`.

Along with `def`, we have to give functions a name. To choose a name for a function, think like you are naming a variable, as you want it to describe what the function does but not too painful to rewrite in a few places when you call it.

Here is a very basic function definition:

```python
def printhw():
    print("Hello, World!")
```

Note here that our function, named `printhw` has parentheses with it so its `printhw()`, which tells Python that this is a function.

One important thing that happens when you define a function is that the function itself isn't run. If the function above was run, nothing would actually get printed even though our second line clearly has a `print` statement.

In order for that print statement to be run, we need to call the function! On any line after a function is defined, you can call a function just by using its name with the parentheses:

```python
printhw()
```

This produces the output:

```
Hello, World!
```

Unless we need to print `"Hello, World!"` multiple times, this function isn't that useful. To make functions more useful, we need parameters.

---

## Parameters/Arguments

Just like how a function in math takes in an input, we can make functions in Python take in an input. When defining a function, we call this input a **parameter**, and when we actually call the function using the input, we call it an **argument**.

To give a function a parameter when we define it, we create a variable inside of the parentheses. The name you give this variable can be used throughout the function to refer to the value passed in by the function call.

Here is a basic function with a parameter:

```python
def hello(name):
    print(f"Hello {name}!")
```

This function takes in a value called `name` and uses it to print an f-string that utilizes the value. This function could be helpful if you have various points in a program where you need to say hi to someone.

It is important to note that in order to call `hello`, we need to include a value. If we tried to call `hello` without a parameter, we would get an error:

```python
hello()
```

This produces the output:

```
TypeError: hello() missing 1 required positional argument: 'name'
```

The function works fine as long as we pass in a value:

```python
hello("John")
```

This produces the output:

```
Hello John!
```

### Multiple Parameters

By using a comma `,`, we could also give a function multiple parameters:

```python
def hello(name1, name2):
    print(f"Hello {name1} and {name2}!")
```

We can call this function by passing in two values separated by a comma, and with any function these values could be hard-coded or variables!

```python
name = "Nathan"
hello(name, "Cody")
```

This produces the output:

```
Hello Nathan and Cody!
```

Note that when we pass in the variable `name`, it's valued gets copied over to `name1` for the purpose of the function.

### Iterable Parameters

We aren't restricted to strings either, a function could take in a number like `int` or `float`, a `bool`, or even an iterable! A function with an iterable as a parameter looks no different, as we still just put a variable-like name in the parentheses of our function:

```python
def hellos(names):
    for name in names:
        print(f"Hello {name}!")
```

Let's call this function with a `tuple`:

```python
tup = ("Rianah", "Nafiza", "Christina", "Denae")
hellos(tup)
```

This produces the output:

```
Hello Rianah!
Hello Nafiza!
Hello Christina!
Hello Denae!
```

We do have to be careful when we expect a function to have an iterable as an argument. If we just passed in a single name to our new function, we'd get less desireable behavior:

```python
hellos("Madeline")
```

This produces the output:

```
Hello M!
Hello a!
Hello d!
Hello e!
Hello l!
Hello i!
Hello n!
Hello e!
```

We can see here it divided up the string into it's characters and used those as its elements!

---

## Default Values

To limit problems, sometimes we want a function's parameters to have a default value that it can use if we forget, or don't otherwise provide, a parameter. To give a parameter a default value, we set it equal to a value when we name it in the definition:

```python
def hi(name="World"):
    print(f"Hello {name}!")
```

This function can now print a greeting if we provide a value and if we don't! Let's see both:

```python
hi("Josiah")
hi()
```

This produces the output:

```
Hello Josiah!
Hello World!
```
