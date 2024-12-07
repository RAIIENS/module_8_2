def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for item in numbers:
        try:
            result += item
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {item}')
            incorrect_data += 1
    return result, incorrect_data
def calculate_average(numbers):
    try:
# Проверяем, является ли numbers коллекцией
        if not isinstance(numbers, (list, tuple)):
            raise TypeError
        total_sum, incorrect_data = personal_sum(numbers)
# Вычисляем количество корректных данных
        valid_count = len(numbers) - incorrect_data
        average = total_sum / valid_count if valid_count > 0 else 0
        return average
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None
# Примеры работы функции calculate_average
print(f'Результат 1: {calculate_average("1, 2, 3")}')                       # Строка
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Смешанные типы
print(f'Результат 3: {calculate_average(567)}')                             # Не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')                # Все корректно

# Функция personal_sum(numbers) инициализирует переменные result для хранения суммы чисел и
# incorrect_data для подсчета некорректных данных.
# Перебирает элементы в numbers, пытаясь суммировать их. Если возникает TypeError, выводит
# сообщение о некорректном типе данных и увеличивает счетчик некорректных данных.
# В конце возвращает кортеж из суммы и количества некорректных данных.
# Функция calculate_average(numbers) проверяет, является ли numbers коллекцией
# (списком или кортежем). Если нет, то вызывает исключение TypeError.
# Вызывает personal_sum для получения суммы и количества некорректных данных.
# Вычисляет среднее арифметическое, обрабатывая ZeroDivisionError, если все данные некорректны.
# Если возникает TypeError, выводит сообщение и возвращает None.
