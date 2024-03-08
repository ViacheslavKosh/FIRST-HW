# Розширений варіант з вводом дати вручну

from datetime import datetime

# Виводить привітання
print("Hello! Now we will count days from date you type!")

# Користувач вводить дату у форматі РРРР-ММ-ДД
date = str(input("Enter date using format 'YYYY-MM-DD': "))

def get_days_from_today(date):
    try:

        # Повертаємо рядок дати як об'єкт datetime    
        date_object = datetime.strptime(date, "%Y-%m-%d")
        
        # Отримуэмо поточну дату 
        date_today = datetime.today()
        
        # Використовуючи метод toordinal() отримуємо різницю в днях між датами як ціле число
        differecne = int(date_today.toordinal() - date_object.toordinal())
        
        # Виводимо на екран отриману різницю
        print(differecne)
        
        # Повертаємо отриману різницю
        return differecne
    
    # Якщо дата введена в невірному форматі то отримаемо зауваження
    except ValueError:
        print(f"Incorrect date format {date}. Try again with format: 'YYYY-MM-DD'")

# Викликаємо функцію для дати введеної користувачем
get_days_from_today(date)