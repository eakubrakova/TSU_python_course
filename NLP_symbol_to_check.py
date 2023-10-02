"""��� ������ �� ����� str_list. 
�������� ��������� ��� �������� ���������� ��������� ��������� ������� � ������ �� ����� ����� ������. 
������� ������ �������� � ���������� symbol_to_check.

��� �������� ����������� �������: � �������� ����� �������� � ���� ������, 
� �������� �������� � ����� ��������� �������� ������� � ��� ������.
��� �������� ������� ����������� ���������� � ������ word_dict"""

str_list = ["text", "morning", "notepad", "television", "ornament"]
symbol_to_check = 't'
word_dict = {}

for word in str_list:
    count = word.count(symbol_to_check)
    word_dict[word] = count
    
print(word_dict)
