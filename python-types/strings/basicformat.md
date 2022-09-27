# Basic String Formatting

Strings can be formatted to produce simpler outputs when we want to incorporate variable values into a statement we use frequently

For a functioning example, check out basicformat.py and feel free to play around with some values for our variables to see how the operations behave!

---

## `format` Function

We can effectively put blanks in a String and fill them in using the `format` function

This allows us to have strings that can easily change portions of their values without starting over every time

### One Blank

Blanks are marked using curly braces, here is the most basic example of a "blank"

```python
line1 = "My name is {}!"
```

If we were to print the string line1 as is, we would see the curly braces, which doesn't look nice

```python
print(line1)
```

This produces the output:

```
My name is {}!
```

We can do our `stringname.format()` to pass in argument(s) to fill in any blank(s)

```python
print(line1.format("John Guzauckas"))
```

This produces the output:

```
My name is John Guzauckas!
```

### Multiple Blanks

We can have and fill in multiple blanks using multiple sets of curly braces:

```python
line2 = "My first name is {} and my last name is {}."
```

To fill in multiple blanks, just list multiple values in format() using commas between the blanks are filled in the same order you write your values in

```python
print(line2.format("John", "Guzauckas"))
```

This produces the output:

```
My first name is John and my last name is Guzauckas.
```

### Numbering Blanks

When we start to use a few blanks, it can be harder to keep track of which blank is which to help ease this problem, we can number the blanks (remember zero-indexing!)

```python
line3 = "My first name is {0} and my last name is {1}."
```

Now it will still fill in order, but it can be easier for us to identify which piece goes where

```python
print(line3.format("John", "Guzauckas"))
```

This produces the output:

```
My first name is John and my last name is Guzauckas.
```

### Naming Blanks

To get even more clarity, we can assign temporary "names" to each blank to be referenced later

```python
line4 = "My first name is {first} and my last name is {last}."
```

To fill in, we need to let format() know which value is for which reference by using `reference = value`

```python
print(line4.format(first = "John", last = "Guzauckas"))
```

This produces the output:

```
My first name is John and my last name is Guzauckas.
```

### Repeating Blanks

Sometimes we might need to repeat a blank, and with names they will automatically be used as many times as needed. See here two `{first}` blanks:

```python
line5 = "My first name is {first} and my last name is {last}, but you can call me {first}."
```

The print statement doesn't look different because it `"John"` twice

```python
print(line5.format(first="John", last="Guzauckas"))
```

This produces the output:

```
My first name is John and my last name is Guzauckas, but you can call me John.
```

This repeating blanks works with the numbering too (note two `{0}` here). This can, however, get a little more confusing with more blanks required

```python
line6 = "My first name is {0} and my last name is {1}, but you can call me {0}."
```

Here, since "John" has index 0, it is filled in everywhere 0 is asked for

```python
print(line6.format("John", "Guzauckas"))
```

This produces the output:

```
My first name is John and my last name is Guzauckas, but you can call me John.
```

If we were just using empty braces, we would have to repeat inputs to achieve the same result.

```python
line7 = "My first name is {} and my last name is {}, but you can call me {}."
print(line7.format("John", "Guzauckas", "John"))
```

This produces the output:

```
My first name is John and my last name is Guzauckas, but you can call me John.
```

---

## Incorporating `input`

First, some classic input statements gathering strings and assigning them to variables:

```python
firstname = input("What is your first name? ")
lastname = input("What is your last name? ")
```

Her is a string asking for two unique blanks:

```python
line8 = "My first name is {0} and my last name is {1}."
```

Can utilize string variables as arguments in format to be more dynamic:

```python
print(line8.format(firstname, lastname))
```

This produces the output:

```
What is your first name? John
What is your last name? Guzauckas
My first name is John and my last name is Guzauckas.
```

### Different Blanks Types

Here is a string asking for two (potentially similar) blanks

```python
line9 = "I am {} years old. This statement is {}"
```

Format will automatically convert types to string to plug them in, like int, float, and bool

```python
print(line9.format(24, True))
```
