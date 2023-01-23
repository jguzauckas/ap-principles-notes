list1 = [1, 2, 3, 4, 5, 6]
list2 = [2, 4, 6, 8, 10, 12]
list3 = [3, 6, 9, 12, 15, 18]
print(list(zip(list1, list2, list3)))

list1 = [1, 2, 3, 4, 5, 6]
print(list(zip(list1, list1[1:])))

list1 = [1, 2, 3, 4, 5, 6]
print(list(zip(list1, list1[1:] + [list1[0]])))

list1 = [1, 2, 3, 4, 5, 6]
count = 0
for first, second in zip(list1, list1[1:] + [list1[0]]):
    if first == second:
        count += 1
print(count)

list1 = [1, 2, 3, 4, 5, 6]
count = 0
for pos, (first, second) in enumerate(zip(list1, list1[1:] + [list1[0]])):
    if first == second:
        count += 1
print(count)

list1 = [1, 2, 3, 4, 5, 6]
count = 0
for first, second, third in zip(list1, list1[1:] + [list1[0]], list1[2:] + list1[:2]):
    if first + second + third > 10:
        count += 1
print(count)