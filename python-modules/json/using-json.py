import json

my_dict = {"Mr. G": "Teacher", "Jeet": "Student"}

with open("using-json.json", "w") as my_file:
    json.dump(my_dict, my_file)

my_str = json.dumps(my_dict)
print(my_str)

with open("using-json.json", "r") as my_file:
    data = json.load(my_file)

print(data)

data_str = json.loads(my_str)

print(data_str)