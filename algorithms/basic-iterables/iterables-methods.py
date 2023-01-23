my_list = [12, 15, 11, 16, 18, 14]
total = 0
for item in my_list:
    total += item
print(total)

my_list = [12, 15, 11, 16, 18, 14]
print(sum(my_list))


my_list = [12, 15, 11, 16, 18, 14]
maximum = 0
minimum = 100
for item in my_list:
    if item > maximum:
        maximum = item
    elif item < minimum:
        minimum = item
print(maximum)
print(minimum)

my_list = [12, 15, 11, 16, 18, 14]
print(max(my_list))
print(min(my_list))
