# The print statement offers us a basic way to output information to the user via the terminal.
# The simplest way to use the print statement is to print a single variable or string literal.
a = 5
print(
    a
)  # prints out the current value of a, it can print it even though it is not a string
print("This is a string")  # prints out exactly what is put in quotes

# We can make more complex print statements via the use of two different concatenate-like operators
# First is the comma (,). The comma tells the print statement to print each item consecutively,
# with a space placed between each. This can combine different types into one output:
print("a is", a)  # prints a string literal and then prints the value of a after a space
print(
    "this is", "two strings"
)  # prints each string literal consecutively, with a space
b = 2.2
print(a, b)  # prints two variables of different types consecutively

# The other way to make complex print statements is using the string concatenate operator (+)
# This is a more specific tool as it only works with strings, not with different types being combined.
# It also does not include the space like the comma (,) did.
print("a is" + "5")  # Notice it didn't add the space
print("a is " + "5")  # We added a space so it shows now
# This works with string variables as well:
c = "Hello "
print(c + "World!")  # The output looks normal even though we broke it up here

# With both forms, you can use multiple in the same print statement, as long as you still follow the rules.
print("a is", a, "and b is", b)  # Just go in order!
print("a is " + "an integer" + " and b is" + " a float")
# While it isn't necessarily recommended, you can use both in the same print statement as long as you still
# follow the rules.
print("c is " + c + "and a is", a)
