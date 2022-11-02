from datetime import datetime

my_date = datetime(2022, 10, 31, 14)
print(my_date)

current_date = datetime.now()
print(current_date)

print(f"{my_date} is greater than {current_date} is {my_date > current_date}")
