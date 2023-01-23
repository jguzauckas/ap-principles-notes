my_list = [12, 15, 11, 16, 18, 14]
print(11 in my_list)
print(10 in my_list)

my_list = [12, 15, 11, 16, 18, 14]
for item in my_list:
    print()

my_list = [12, 15, 11, 16, 18, 14]
for pos, item in enumerate(my_list):
    print()

my_list = [12, 15, 11, 16, 18, 14]
for pos, item in enumerate(my_list):
    if item == 15:
        print(pos)
