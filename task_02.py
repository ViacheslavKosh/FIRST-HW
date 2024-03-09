# Імпортуємо пакет роботи з випадковими числами
import random

# Задаємо функцію з параметрами діапазону чисел (min, max), та кількості необхідних відібраних чисел (quantity)
def get_numbers_tickets(min, max, quantity):
    
    # перевіряємо відповідність вхідних даних заданим параметрам (min>1, max<1000)
    if min < 1 or max > 1000:
        
        # повертаємо пустий список при невідповідності вхідних параметрів
        return []
    
    # создаємо список з послідовності чисел від min до max включно. Для включення останнього числа прописуємо 'max + 1'
    number_list = list(range(min, max + 1)) 
    print(number_list)
    
    # за допомогою метода sample пакета random відбираємо необхідну кількість чисел без повторень
    ticket_numbers = random.sample(number_list, k=quantity)
    print(ticket_numbers)
    
    # створюємо новий відсортований список чисел зі списку відібраних 
    sorted_ticket_numbers = sorted(ticket_numbers)
    
    # Повертаємо відсортований за порядком список відібраних чисел
    return sorted_ticket_numbers

print(get_numbers_tickets(1, 1001, 10))