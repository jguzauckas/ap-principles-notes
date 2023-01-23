my_list = [12, 13, 13, 14]
count = 0
for item in my_list:
    if item == 13:
        count += 1
print(count)

my_list = [12, 13, 13, 14]
my_list.count(13)

my_list = [12, 15, 11, 16, 18, 14]
my_list.sort()
print(my_list)

my_list = [12, 15, 11, 16, 18, 14]
my_list.sort(reverse=True)
print(my_list)
