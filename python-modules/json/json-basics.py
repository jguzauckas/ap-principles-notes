import json

with open("json-basics.json", "w") as my_file:
    # json.dump(5, my_file)
    # json.dump("Hello World!", my_file)
    # json.dump([1, 2, 3], my_file)
    json.dump({"Mr. G": "Teacher", "Saad": "Student"}, my_file)
