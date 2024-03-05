import datetime
print("Hello! Now we will count days from date you type!")

try:
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    day = int(input("Enter a day: "))
except ValueError:
    print("It`s not number")
date = (year, month, day)
def get_days_from_today(date):
    None