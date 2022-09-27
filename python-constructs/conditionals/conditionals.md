# Conditionals

Conditionals are a foray for us to make computers make decisions given some parameters.

Conditionals come primarily in the form of `if`, `else` statements. This could be read as "If some condition is true, do **\_**, and otherwise (else) do **\_**."

---

## Boolean Values and Comparisons

As we already know, booleans can hold two values: either `True` or `False`.

Sometimes, we want the boolean value to be based on other information, like if two strings are equal (or not equal), if one number is bigger (or smaller) than another, etc.

Here are our basic boolean comparison operators:

- `==` - check if two values are equal
- `!=` - check if two values are not equal
- `>` - check if the left value is bigger than the right value
- `>=` - check if the left value is bigger than or equal to the right value
- `<` - check if the left value is smaller than the right value
- `<=` - check if the left value is smaller than or equal to the right value

A quick sample of these operators:

```python
print("Hello" == "hello")  # False
print(3 != 4)  # True
print(4 > 2)  # True
print(5 >= 5)  # True
print(4 < 2)  # False
print(3 <= 2)  # False
```

This produces the output:

```
False
True
True
True
False
False
```

We can also incorporate our boolean operations like `and`, `or`, and `not` in these situations to make more complex statements.

A quick example - is the person's age above 20 or below 10:

```python
age = 9
print(age < 10 or age > 20)  # True or False is True
```

This produces the output:

```
True
```

---

## `if`

The most basic form of the conditional is the `if` statement, whose syntax looks like this:

```python
if statement:
    action
```

The colon `:` is critical, and you'll notice it automatically indents the next line after the colon!

Here is a sample `if` statement:

```python
age = 24
if age >= 18:
    print("You are an adult")
```

This produces the output:

```
You are an adult
```

A couple of notes here:

- The action will only be performed if the boolean evaluates to True
- The action can be multiple lines if needed

---

## `if`, `else`

Sometimes we want to do two different things based on a condition, rather than just one thing if a condition is true. To do this, we have a second piece to the conditional, the `else` statement. The syntax looks like this:

```python
if statement:
    action
else:
    action
```

A quick example following up on our previous:

```python
age = 16
if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")
```

This produces the output:

```
You are not an adult
```

An `if-else` statement will only ever do one or the other, never both!

---

## `if`, `elif`, `else`

Sometimes two options isn't enough, and we need to have a few paths based on different conditions. To do this, we have an intermediate statement `else if`, which in Python is shortened to `elif`. `elif` takes another boolean condition, and can be used several times to give your conditionals many paths. The syntax looks like this:

```python
if statement:
    action
elif statement:
    action
elif statement:
    action
else:
    action
```

In this syntactical example, we could have four paths based on up to three different conditions!

Here is an example building on our previous:

```python
age = 10
if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
elif age >= 9:
    print("You are a tween")
else:
    print("You are very young")
```

In this example, our boolean conditions might look odd to you. If you were 20, aren't you above 18, 13, and 9? In programming, we choose the first path that we meet the requirements for and skip the rest. In this case, if we had been 20, we would print `"You are an adult"` and skip the other conditions.

On a similar note, since we must have failed the 18 or older check to get to the teenager check, we don't need an upper bound on our condition, as we already know they must be under 18.

## Ternary Operator

For simpler `if`, `else` statements, we have what is called the **ternary operator**, which allows us to write a much more compact conditional. They look like this:

```python
action if statement else action
```

While this does change the order that we typically think of our conditionals in, when phrased as a sentence it might make more sense: "Do **\_** if statement is true, otherwise do **\_**"

Lets take a code from earlier:

```python
if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")
```

and turn it into a ternary to make it shorter:

```python
print("You are an adult") if age >= 18 else print("You are not an adult")
```

When we run this, given that `age` was most recently set to 10, this produces the following output:

```
You are not an adult
```

So this ternary functions just like the normal `if`, `else` statement, it is just written more compactly. This helps a lot if you have a lot of small conditionals!
