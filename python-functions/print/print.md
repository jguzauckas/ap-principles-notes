# The `print` Function

The `print` statement offers us a basic way to output information to the user via the terminal.

The simplest way to use the `print` statement is to print a single variable or string literal:

```python
a = 5
print(a) #prints out the current value of a, it can print it even though it is not a string
print("This is a string") #prints out exactly what is put in quotes
```

This produces the output:

```
5
This is a string
```

---

## Utilizing Concatenation

We can make more complex `print` statements via the use of two different concatenate-_like_ operators

### Comma `,`

First is the comma `,`. The comma tells the `print` statement to print each item consecutively, with a space placed between each. This can combine different types into one output:

```python
print("a is", a)  # prints a string literal and then prints the value of a after a space
print(
    "this is", "two strings"
)  # prints each string literal consecutively, with a space
b = 2.2
print(a, b)  # prints two variables of different types consecutively
```

This produces the output:

```
a is 5
this is two strings
5 2.2
```

The comma is an excellent way to make simple and complete-looking sentences when needed!

### Concatenate `+`

The other way to make complex `print` statements is using the string concatenate operator `+`. This is a more specific tool as it only works with strings, not with different types being combined. It also does not include the space like the comma `,` did.

```python
print("a is"+"5") #Notice it didn't add the space
print("a is "+"5") #We added a space so it shows now
```

This produces the output:

```
a is5
a is 5
```

This shows we need to be more careful when crafting out `print` statement when using `+` if we want certain formatting like spaces! We also can't just use normal numbers, in this case I gave it the number `5` but I passed it in as a string due to the quotes `"5"`.

This works with string variables as well:

```python
c = "Hello "
print(c+"World!") #The output looks normal even though we broke it up here
```

This produces the output:

```
Hello World!
```

### Multiple Operators

With both forms, you can use multiple in the same `print` statement, as long as you still follow the rules:

```python
print("a is", a, "and b is", b) #Just go in order!
print("a is "+"an integer"+" and b is"+" a float")
```

This produces the output:

```
a is 5 and b is 2.2
a is an integer and b is a float
```

While it isn't necessarily recommended (primarily due to readability), you can use both in the same `print` statement as long as you still follow the rules:

```python
print("c is "+c+"and a is", a)
```

This produces the output:

```
c is Hello and a is 5
```
