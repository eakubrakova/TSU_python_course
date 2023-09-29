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
# Создаём цикл по списку мест, которые хотим посетить.
# place — текущее название места
for place in places: 
    # Получаем страну из словаря location по ключу
    country = location[place] 
    # Сравниваем название страны
    if country != 'Russia': 
        # Помечаем место как недоступное
        place = 'Unavailable' 
# Выводим результирующий список
print(places)

