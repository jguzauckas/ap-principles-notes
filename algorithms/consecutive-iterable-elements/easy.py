my_list = [1, 2, 3, 4, 5, 6, 7]
count = 0
for pos, item in enumerate(my_list):
    if item == my_list[pos - 1]:
        count += 1
print(count)

my_list = [1, 2, 3, 4, 5, 6, 7]
count = 0
for pos, item in enumerate(my_list):
    if item + my_list[pos - 1] + my_list[pos - 2] > 10:
        count += 1
print(count)
