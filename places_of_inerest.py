# Список мест, которые хотим посетить.
places = [
    'Red Square',
    'Swallow Nest',
    'Niagara Falls',
    'Grand Canyon',
    'Louvre',
    'Hermitage'
]
# Словарь соответствия мест и стран
location = {
    'Red Square': 'Russia',
    'Swallow Nest': 'Russia',
    'Niagara Falls': 'USA',
    'Grand Canyon': 'USA',
    'Louvre': 'France',
    'Hermitage': 'Russia'
}
# Вычисляем длину списка
N = len(places)
# Создаём цикл по списку мест, которые хотим посетить.
# i — текущее значение последовательности
for i in range(N):
    # places[i] — i-й элемент в списке places
    # Получаем страну из словаря location по ключу
    country = location[places[i]]
    # Сравниваем название стран
    if country != 'Russia':
        # Помечаем место как недоступное
        places[i] = 'Unavailable'
# Выводим результирующий список
print(places)

