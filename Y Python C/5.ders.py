# name = input("Enter your name: ")
# birth_year = int(input("Enter your birth year: "))
# current_year = int(input("Enter current year: "))

# age =  current_year - birth_year
# is_adult = age >= 18

# if is_adult:
#     print(f"{name} can vote!!")

# 1. Syntax Error
# 2. Runtime Error
# x = 10
# y = 0
# result = x / y

# print(f"{x} divided by {y} is {result}")

# 3. Logical Error
hourly_wage = float(input("Hourly wage: "))
hours = int(input("Hours worked: "))
day = input("Day of the week: ")

daily_wages = hourly_wage * hours
if day == "sunday":
    daily_wages *= 2

print(f"Daily wages: {daily_wages} euros")


