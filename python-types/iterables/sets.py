# Sets are a way to store multiple items in a single variable
# Sets are defined using curly brackets {}
# Elements in sets are separated using commas

# To learn more about sets, go over to the sets.md file

# Creating a set:
var1 = {"Damario", "Zainab", "Saad", "Gage"}
print(var1)  # Prints the elements in curly brackets

# Can use the set() constructor to convert other iterables, like tuple,
# list or string into a set
var2 = set()  # Can generate a blank set to add to later
print(var2)  # Just prints set() to represent empty set

t = (1, 2, 3)  # Sample tuple
var2 = set(t)  # Copy and covert the tuple to a set
print(var2)  # Still prints elements in curly brackets

var2 = set("Hello")  # Takes the characters as elements
print(var2)  # Prints out the individual characters list
# Things to notice here:
# No duplicate elements, removed extra 'l'
# Reordered the elements, doesn't care about order - if you run this
# multiple times, the order will change every time

# In a set, there are no indices (order doesn't matter), so we
# cannot print an element at an individual space
# We can use a for loop (more on these on another date) to list
# out all elements
for elem in var2:
    print(elem)

# While we can't print individual slots, we can check for the
# presence of certain values with the in keyword
print("h" in var2)  # Should be false, no lowercase 'h'
print("H" in var2)  # Should be true, there is uppercase 'H'

# Sets are kind of changeable. We cannot change individual elements
# like lists or dictionaries can, but we can add/remove elements

# We have three functions that can remove elements:
# remove(), discard(), and pop()
# remove() searches for an item and removes it, but will have an error
# if the item cannot be found
var2.remove("H")
print(var2)

# discard() does the same thing as remove, but will not not have an
# error if the item cannot be found
var2.discard("h")  # This will not do anything because there is no 'h'
print(var2)
var2.discard("o")
print(var2)

# pop() normally would take an index, but there are none for sets,
# so it just removes the last element in the set (remember that
# order doesn't matter so it will be different each time!)
var2.pop()  # Just removes the current last element
print(var2)

# To add an elements, we have one main option: add()
# add() adds the element to the end of the set:
var2.add("p")
print(var2)

# We can also add any iterable to the end of the set using update()
t = (1, 2, 3)
var2.update(t)
print(var2)

# We can find out how many elements are in a set by using the length
# function len() (similar to strings)
print(len(var1))  # Can just use stand-alone
print(f"There are {len(var1)} elements in var1")  # Using f-string!

# Sets can hold any data type, and can mix in match within the same set
var4 = {"John", 24, 5.75, True}
print(var4)
print(len(var4))
