# The `input` Function

Showing output to the user is important, but so is getting information from the user!

Our most basic way to do this is with the `input` function. The `input` function will prompt the user to type an input string (and press enter) and will return that string to the program.

Inside the parentheses, you put a string that you would like to prompt the user with. For example:

```python
input(
    "Enter your name: "
)
```

This produces the output:

```
Enter your name:
```

Besides the prompt, this program doesn't have any output, or accomplish anything on its own, as we don't save the string! Remember that programming languages are efficient and will only remember information when we tell them to!

The most useful combination is to save this as a String variable so we can use it later:

```python
name = input("Enter your name: ")  # now the name variable holds the users entered name
```

This has the same output as before, but now what the user entered is saved to a variable! A classic use case for `input` is to incorporate the entered information into an output:

```python
print(
    "Hello", name + "!"
)  # This is a use case for the input, incorporating it into a response!
```

Given I type in "Mr. Guzauckas", this produces the output:

```
Hello Mr. Guzauckas!
```

---

## Limitations

It is important to note an initial limitation of `input`: its always a string! Even if you enter a number, it treats it as a string:

```python
a = input("Enter a number: ")
print(
    "The type of a is", type(a)
)  # this will show that a is a string even if the user entered a number
```

This produces the output:

```
Enter a number: 5
The type of a is <class 'str'>
```

This shows that even though we entered a number, Python naturally interprets it as a string.

## Casting

We can force Python to reinterpret the input as another type by using casting

**Note**: this is relatively ineffective with our current tools because a user entering the wrong type of information can break the program, but we'll show basic examples.

To cast, we use the type name as a command (i.e., int(), float(), bool()):

**`int`**

```python
b = int(input("Enter an integer: "))
print("The type of b is", type(b))
```

This produces the output:

```

```

**`float`**

```python
c = float(input("Enter an float: "))
print("The type of c is", type(c))
```

This produces the output:

```

```

**`bool`**

The conversion from `str` to `bool` is not as clear as the others. Python interprets a string with any characters (even just a space) as being `True`, and only a blank string to be `False`. This means that regardless of what is in a string (or not in a string), it can convert it to a `bool`.

```python
d = bool(input("Enter an boolean (anything for True, blank for False): "))
print("The type of d is", type(d))
```

This produces the output:

```
Enter an boolean (anything for True, blank for False): a
The type of d is <class 'bool'>
```
