text = """
She sells sea shells on the sea shore;
The shells that she sells are sea shells I am sure.
So if she sells sea shells on the sea shore,
I am sure that the shells are sea shore shells.
"""
# Приводим текст к нижнему регистру
text = text.lower() 
# Заменяем символы переноса строки на пробелы
text = text.replace("\n", " ") 
# Заменяем запятые на пустые строки
text = text.replace(",", "") 
# Заменяем точки на пустые строки
text = text.replace(".", "") 
# Заменяем точки с запятыми на пустые строки
text = text.replace(";", "") 
# Разделяем текст на слова
word_list = text.split()
# Создаём пустой словарь для подсчёта количества слов
count_dict = {} 
# Создаём цикл по словам в списке word_list
# word — текущее слово из списка word_list
for word in word_list: 
    # Проверяем условие, что слова ещё нет среди ключей словаря.
    if word not in count_dict:
        # Если условие выполняется, заносим слово в словарь со значением 1.
        count_dict[word] = 1
    else: 
        # В противном случае увеличиваем частоту слова
        count_dict[word] += 1
# Выводим результирующий словарь
print(count_dict) 
