text = """
She sells sea shells on the sea shore;
The shells that she sells are sea shells I am sure.
So if she sells sea shells on the sea shore,
I am sure that the shells are sea shore shells.
"""
# �������� ����� � ������� ��������
text = text.lower() 
# �������� ������� �������� ������ �� �������
text = text.replace("\n", " ") 
# �������� ������� �� ������ ������
text = text.replace(",", "") 
# �������� ����� �� ������ ������
text = text.replace(".", "") 
# �������� ����� � �������� �� ������ ������
text = text.replace(";", "") 
# ��������� ����� �� �����
word_list = text.split()
# ������ ������ ������� ��� �������� ���������� ����
count_dict = {} 
# ������ ���� �� ������ � ������ word_list
# word � ������� ����� �� ������ word_list
for word in word_list: 
    # ��������� �������, ��� ����� ��� ��� ����� ������ �������.
    if word not in count_dict:
        # ���� ������� �����������, ������� ����� � ������� �� ��������� 1.
        count_dict[word] = 1
    else: 
        # � ��������� ������ ����������� ������� �����
        count_dict[word] += 1
# ������� �������������� �������
print(count_dict) 
