# Другий варіант функції яка лишає різницю як об'єкт datatime 

from datetime import datetime

def get_days_from_today(date):
    
    try:
        # Повертаємо рядок дати як об'єкт datatime
        date_object = datetime.strptime(date, '%Y-%m-%d')
        
        # Отримуэмо поточну дату 
        date_today = datetime.today()
        
        # Отримуємо різницю між датами як об'єкт datatime
        difference = date_today - date_object
        
        # Повертаємо кількість днів як ціле число 
        return difference.days
    
    # Якщо дата введена в невірному форматі то отримаемо зауваження
    except ValueError:
        print(f"Incorrect date format {date}. Try again with format: 'YYYY-MM-DD'")

