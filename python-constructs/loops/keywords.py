# For more information on these samples, please
# see the keywords.md file, which has descriptions
# for everything

# A sample iterable
surnames = surnames = ["Kirchmeier", "Pointek", "Guzauckas", "Lorenzet"]

# For loop with break
for name in surnames:
    if name == "Guzauckas":
        break
    print(name)

# For loop with continue
for name in surnames:
    if name == "Guzauckas":
        continue
    print(name)
