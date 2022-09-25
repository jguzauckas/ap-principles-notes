# Lists are a way to store multiple items in a single variable
# Lists are defined using square brackets []
# Elements in lists are separated using commas

# To learn more about lists, go over to the lists.md file

# Creating a list:
var1 = []  # Creates an empty list
print(var1)
var1 = ["Damario", "Zainab", "Saad", "Gage"]
print(var1)  # Prints the elements in square brackets


# Can use the list() constructor to convert other iterables, like tuple
# or string into a list
t = (1, 2, 3)  # Sample tuple
var2 = list(t)  # Copy and covert the tuple to a list
print(var2)  # Still prints elements in square brackets

var2 = list("Hello")  # Takes the characters as elements
print(var2)  # Prints out the individual characters list

# We can print individual elements using an index, like string
# Remember the indices start at 0, and we use square brackets
# next to the list to tell it we want to find an index
print(var1[2])
print(var2[0])

# Unlike tuples, lists are changeable, so we can change individual
# elements or add/remove elements
# To change an element, we assign a new value to the index:
var2[2] = 4
# This will update the original list and replace the value in the
# third position with 4
print(var2)

# We have two primary options to remove elements: remove() and pop()
# remove() chooses the value to remove based on its value
var2.remove(4)
print(var2)  # No more random 4!

# pop() chooses the value to remove based on its index
var2.pop(1)  # Removes character at second index
print(var2)  #

# To add an elements, we have two primary options: append() and insert()
# append() adds the element to the end of the list:
var2.append("!")
print(var2)

# insert() lets us choose where in the list we want the new element
# by providing an index and shifting all other elements to the right
var2.insert(2, "l")  # Inserts 'l' at the provided index 2
var2.insert(1, "e")  # Adds back the 'e' from earlier
print(var2)

# We can also add any iterable to the end of the list using extend()
t = tuple("What's up?")
var2.extend(t)
print(var2)

# Lists can have duplicate values, as the indices will still be unique
var3 = [5, 5, 5]  # This list won't be very helpful, but demonstrates this
print(var3)
print(var3[2])

# We can find out how many elements are in a list by using the length
# function len() (similar to strings)
print(len(var1))  # Can just use stand-alone
print(f"There are {len(var1)} elements in var1")  # Using f-string!

# Lists can hold any data type, and can mix and match within the same list
var4 = ["John", 24, 5.75, True]
print(var4)
print(var4[1])
print(len(var4))
