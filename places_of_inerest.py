# ������ ����, ������� ����� ��������.
places = [
    'Red Square',
    'Swallow Nest',
    'Niagara Falls',
    'Grand Canyon',
    'Louvre',
    'Hermitage'
]
# ������� ������������ ���� � �����
location = {
    'Red Square': 'Russia',
    'Swallow Nest': 'Russia',
    'Niagara Falls': 'USA',
    'Grand Canyon': 'USA',
    'Louvre': 'France',
    'Hermitage': 'Russia'
}
# ������ ���� �� ������ ����, ������� ����� ��������.
# place � ������� �������� �����
for place in places: 
    # �������� ������ �� ������� location �� �����
    country = location[place] 
    # ���������� �������� ������
    if country != 'Russia': 
        # �������� ����� ��� �����������
        place = 'Unavailable' 
# ������� �������������� ������
print(places)

