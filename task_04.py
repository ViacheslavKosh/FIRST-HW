# Імпорт datetime та timedelta для роботи з датами і часом
from datetime import datetime, timedelta 

# Функція для знаходження наступного заданого дня тижня після заданої дати
def find_next_weekday(d, weekday: int):  
    
    days_ahead = weekday - d.weekday()  # Різниця між заданим днем тижня та днем тижня заданої дати
    if days_ahead <= 0:  # Якщо день народження вже минув
        days_ahead += 7  # Додаємо 7 днів, щоб отримати наступний тиждень
    return d + timedelta(days=days_ahead)  # Повертаємо нову дату

# Вводимо функцію для перетворення дат у словнику користувачів у об'єкт datetime
def get_datetime_from_users (users):
    
    # Словник підготовлених користувачів
    prepared_users = []  
    
    # Ітерація по кожному користувачеві зі словнику
    for user in users:  
        
        # Використовуємо механізм обробки винятків за допомогою оператора try
        try:
            # Перетворюємо дату для користувача в об'єкт datetime за допомогою методу strptime
            birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()  
            
            # Додаємо користувача з підготовленою датою народження
            prepared_users.append({"name": user['name'], 'birthday': birthday})  
        
        # Якщо дата некоректна виводимо попередження про помилку
        except ValueError:
            print(f'Некоректна дата народження для користувача {user["name"]}')  
    
    # Кількість днів для перевірки на наближені дні народження
    days = 7  
    today = datetime.today().date()  # Поточна дата

    # Словник днів народження на наступні 7 днів 
    upcoming_birthdays = []  
    
    # Ітерація по підготовленим користувачам та заміна року на поточний 
    for user in prepared_users:  
        birthday_this_year = user["birthday"].replace(year=today.year)
            
        # За умови що дата народження вже пройшла цього року переносимо її на наступний рік
        if birthday_this_year < today:  
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # За умови що день народження в межах наступних 7 днів
        if 0 <= (birthday_this_year - today).days <= days:  
        
        # За умови що день народження випадає на суботу або неділю шукаємо наступний понеділок
            if birthday_this_year.weekday() >= 5: 
                birthday_this_year = find_next_weekday(birthday_this_year, 0)  

        # Форматуємо дату у рядок
            congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d') 
        
        # Додаємо дані про майбутній день народження у словник upcoming_birthdays
            upcoming_birthdays.append({  
                "name": user["name"],
                "congratulation_date": congratulation_date_str
                })
    return upcoming_birthdays


# Перевірка роботи функції
# Словник користувачів з їхніми датами народження
users = [  
    {"name": "Daffy Duck", "birthday": "1985.03.15"},
    {"name": "Mickey Mouse", "birthday": "1990.01.27"},
    {"name": "Bugs Bonny", "birthday": "1990.03.11"},
    {"name": "Lola Bonny", "birthday": "1990.06.17"},
    {"name": "Road Runner", "birthday": "1990.03.10"},
]

print(get_datetime_from_users (users))  # Виводимо список майбутніх днів народження