# Naming

To make Python code readable to other users and remain consistent, we have styling guidelines provided by PEP 8, a published document that provides guidance and best practices on how to write Python code!

We will start with how we name things, in particular variables, constants, functions, and classes.

The naming.py file has all the sample code from this markdown file for you to run and modify as you'd like to get a better sense of how this works!

---

## Potential Styles

PEP 8 offers the following as potential options for styling a name:

- `b` (single lowercase letter)
- `B` (single uppercase letter)
- `lowercase`
- `lower_case_with_underscores` (or snake_case)
- `UPPERCASE`
- `UPPER_CASE_WITH_UNDERSCORES`
- `CapitalizedWords` (or CapWords, or PascalCase – so named because of the bumpy look of its letters [4]). This is also sometimes known as StudlyCaps.
  - Note: When using acronyms in CapWords, capitalize all the letters of the acronym. Thus `HTTPServerError` is better than `HttpServerError`.
- `mixedCase` (differs from CapitalizedWords by initial lowercase character!)
- `Capitalized_Words_With_Underscores` (ugly!)

While there are a lot of options, if different people just used whatever they wanted out of this list, everyone's code would look very different! PEP 8 offers guidelines for which style of naming to use in different circumstances.

---

## Variable and Function Naming

When naming variables and functions in Python, the guideline is to use `snake_case` where the first letters of every word (including the first!) are lowercase, and you place underscores between each word to improve readability.

Let's take a look at a couple of potential variable names:

```python
count = 0
count_players = 0
if_yes_count = 0
```

All three of these variable names follow the correct naming scheme for variables, as their first letters are lowercase, and there are underscores between words where applicable.

Variables can occasionally have really short names, as short as one character! This is not always recommended, as we try to have our variables provide useful information about what they store, but if needed, just be sure to avoid the following:

- `l` (lowercase letter el)
- `O` (uppercase letter oh)
- `I` (uppercase letter eye)

These specific characters are easy to misread as `0` or `1`, making them difficult to use without confusing a reader. Otherwise, for variable names use a single lowercase letter when absolutely needed:

```python
a = 5
```

We have similar naming for functions:

```python
def counter():
    return

def count_people():
    return

def if_applied_counter():
    return
```

Each of these function names should look similar to our variable names as they use the same styling!

---

## Constant Naming

Constants are much like variables, except we expect them to not have to change like a variable might have to. This is helpful when there is a standard value used in a calculation that you know will never change, and eliminates the need to write that same value over and over.

To name a constant, we use the `UPPER_CASE_WITH_UNDERSCORES` style, like the following:

```python
PI = 3.14
GRAVITY_ACCELERATION = 9.81
```

These are examples of constants (the value of pi and the constant acceleration due to gravity) that we may have to use to calculate, but the values won't change. Furthermore, when using these constants in a calculation it can be more clear what the number being used represent rather than a random decimal!

---

## Class Naming

For our final naming convention, we look at classes, where we use `CapCase`, which is also known as `PascalCase`, where the first letters of each word are capitalized, and there is no other separation between words. Here are some examples:

```python
class Person:
    b = 0


class MyClass:
    b = 0


class HighSchoolStudent:
    b = 0


```
