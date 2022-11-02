import math

print(math.ceil(5))
print(math.ceil(4.9))
print(math.ceil(4.5))
print(math.ceil(4.1))
print(math.ceil(4))

print(math.floor(5))
print(math.floor(4.9))
print(math.floor(4.5))
print(math.floor(4.1))
print(math.floor(4))

grades = [90, 100, 92, 83, 67, 70, 75, 94, 96, 89]

sum = 0
for grade in grades:
    sum += grade
print(f"The average grade is {sum / len(grades):.2f}")

sum = math.fsum(grades)
print(f"The average grade is {sum / len(grades):.2f}")


product = 1
for grade in grades:
    product *= grade
print(f"The product of all the grades is {product:,}")

product = math.prod(grades)
print(f"The product of all the grades is {product:,}")

print(f"20! = {math.factorial(20):,}")

print(f"The area of a circle with a radius of 5 is {math.pi * 5 ** 2:.2f}")
