# For more information on these samples, please
# see the foreach.md file, which has descriptions
# for everything

# A sample iterable
surnames = ["Guzauckas", "Kirchmeier", "Pointek", "Lorenzet"]

# More complicated for loop
for x in range(len(surnames)):
    print(surnames[x])

# Easier for each loop
for name in surnames:
    print(name)

# Both index and element
for position, name in enumerate(surnames):
    print(position, name)

# Use variables separately
for position, name in enumerate(surnames):
    print(f"{name} is in position {position}.")
