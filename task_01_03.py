# Розширений варіант з вводом дати вручну

from datetime import datetime

print("Hello! Now we will count days from date you type!")

date = str(input("Enter date using format 'YYYY-MM-DD': "))

def get_days_from_today(date):
    try:
        date_object = datetime.strptime(date, "%Y-%m-%d")
        date_today = datetime.today()
        differecne = int(date_today.toordinal() - date_object.toordinal())
        print(differecne)
        return differecne
    except ValueError:
        print(f"Incorrect date format {date}. Try again with format: 'YYYY-MM-DD'")

get_days_from_today(date)