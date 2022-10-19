def sendback(name):
    return name


sendback("John")

name = sendback("John")
print(name)


def interest(money):
    money *= 1.03**10  # 10 years of 3% interest
    money *= 1.02**15  # 15 years of 2% interest
    return money


total = interest(1000)
print(f"In 25 years, your $1,000 will become ${total:.2f}")


def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


print(max(10, 12))
