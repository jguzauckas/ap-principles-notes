# Tuples are a way to store multiple items in a single variable
# Tuples are defined using round brackets (parentheses)
# Elements in tuples are separated using commas

# To learn more about tuples, go over to the tuples.md file

# Creating a tuple:
var1 = ("Damario", "Zainab", "Saad", "Gage")
print(var1)  # Prints the elements in round brackets
var1 = ("Damario",)  # Can create with just one element as long as you have a comma
print(var1)

# Can use the tuple() constructor to convert other iterables, like list
# or string into a tuple
l = [1, 2, 3]  # Sample list, don't worry about this for now
var2 = tuple(l)  # Copy and covert the list to a tuple
print(var2)  # Still prints elements in round brackets

var2 = tuple("Hello")  # Takes the characters as elements
print(var2)  # Prints out the individual characters tuple

# We can print individual elements using an index, like string
# Remember the indices start at 0, and we use square brackets
# next to the tuple to tell it we want to find an index
print(var1[0])
print(var2[1])

# Note that if I want to change a tuple. I will need to create
# a new one, as they are immutable.
var1 = ("Damario", "Zainab", "Saad", "Gage", "John")
# This will not update the original var1 tuple, it will create a
# new one
print(var1)

# Tuples can have duplicate values, as the indices will still be unique
var3 = (5, 5, 5)  # This tuple won't be very helpful, but demonstrates this
print(var3)
print(var3[2])

# We can find out how many elements are in a tuple by using the length
# function len() (similar to strings)
print(len(var1))  # Can just use stand-alone
print(f"There are {len(var1)} elements in var1")  # Using f-string!

# Tuples can hold any data type, and can mix and match within the same tuple
var4 = ("John", 24, 5.75, True)
print(var4)
print(var4[1])
print(len(var4))
