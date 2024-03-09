# Враховуючи завдання - чиста функция яка повертає різницю між датами як ціле число

# Імпортуємо datetime з модулю datetime для роботи з датою та часом
from datetime import datetime

# Вводимо функцію по параметру date. Параметр буде дата з типом рядок у форматі 'РРРР-ММ-ДД'
def get_days_from_today(date):

    # Використовуємо механізм обробки винятків за допомогою оператора try
    try:
        # Повертаємо рядок дати як об'єкт datetime
        date_object = datetime.strptime(date, "%Y-%m-%d")
        
        # Отримуэмо поточну дату 
        date_today = datetime.today()
        
        # Використовуючи метод toordinal() отримуємо різницю в днях між датами як ціле число
        difference = date_today.toordinal() - date_object.toordinal()
        
        # Повертаємо отриману різницю
        return difference
    
    # Якщо дата введена в невірному форматі то отримаемо зауваження
    except ValueError:
        print(f"Incorrect date format {date}. Try again with format: 'YYYY-MM-DD'")

