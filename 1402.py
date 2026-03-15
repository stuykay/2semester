# Стоимость 500, проверка данных, посчитать итоговую стоимость, проверка нехватки денег, вывести результаты
TICKET_COST = 500

def validate_name(name: str):
    if name == '':
        raise ValueError('Имя должно быть не пустым')

def validate_age(age: int):
    if not isinstance(age, int):
        raise ValueError('Возраст должен быть числом')
    if age < 12:
        raise ValueError('Возраст слишком маленький')

def validate_tickets(count):
    if not isinstance(count, int):
        raise ValueError('Количество билетов должно быть числом')
    if not (0 < count < 6):
        raise ValueError('Некорректное количество билетов')

def validate_budget(budget):
    if not isinstance(budget, int):
        raise ValueError('Бюджет должен быть числом')
    if budget < 0:
        raise ValueError('Некорректный бюджет')

def calculate_total(count):
    pass

validate_age('10')
print('hello')