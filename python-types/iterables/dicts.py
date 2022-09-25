# Dicts are a way to store multiple items in a single variable
# Dicts are defined using curly brackets {}
# Elements in dicts come in key:value pairs, where the key
# functions as an index of sorts
# Elements in dicts are separated using commas

# Creating a dict:
var1 = {}
print(var1)
var1 = {
    "Damario": 10,
    "Zainab": 10,
    "Saad": 12,
    "Gage": 12,
}  # We often write with multiple lines for readability
print(var1)  # Prints the pairs in curly brackets
# As you can see in this dict, values can be repeated, but keys cannot

# In a dict, there are no indices, and instead we have keys.
# We can print an individual element by requesting its key.
print(var1["Damario"])

# If you want to see all the keys in a dict, you can use the keys() method
print(var1.keys())

# Similar to keys, to see all values in a dict, you can use values()
print(var1.values())

# To see all key:value pairs, you can use items()
print(var1.items())  # It shows them as a list of tuples

# We can check for the presence of a key in a dict by using the
# in keyword
print("Cody" in var1)  # Should be false, no "Cody" key
print("Gage" in var1)  # Should be true, there is a "Gage" key

# dicts are changeable, so we can change individual elements or
# add/remove elements

# To change an element, we assign a new value to a key:
print(var1["Zainab"])  # Currently 10
var1["Zainab"] = 11
print(var1["Zainab"])  # Now 11

# We could also use the update() method to change a particular value:
var1.update({"Zainab": 10})
print(var1["Zainab"])  # Now back to 10

# You can use the same two methods to add new elements to a dict
# just by using a new, unused, key
var1["Nathan"] = 12
var1.update({"Nigel": 10})
print(var1)

# We have three functions that can remove elements:
# pop(), popitem(), del, and clear()
# pop() will search for a given key and remove it
var1.pop("Gage")
print(var1)

# popitem() removes the last inserted element
var1.popitem()  # This should remove Nigel
print(var1)

# clear() allows us to empty a dict while still maintaining
# its reference as a dict at all (unlike del)
var1.clear()
print(var1)

# We can find out how many pairs are in a dict by using the length
# function len() (similar to strings)
print(len(var1))  # Can just use stand-alone
print(f"There are {len(var1)} elements in var1")  # Using f-string!

# In a dict, we can mix and match data types with some restrictions:
# Keys should be an immutable type (think our basic types)
# While not required, it is strongly recommended that all of your
# keys be the same type
# Your values paired with the keys can be any types and can be
# mixed throughout
var1 = {
    2: "Hello",
    4: 3.2,
    8: 2,
    11: True,
}  # Note that my keys are all the same type - int
print(var1)
