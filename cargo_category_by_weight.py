
# ����� ������ �������� ����� �������
weight_of_products = [10, 42.4, 240.1, 101.5, 98, 0.4, 0.3, 15] 


# ����� ������������ �������� ���� �����
max_weight = 100 
# ����� ��������� ����� �����
num = 1 
# ������ ���� �� ��������� ������ �� ���������� ����� �������
# weight � ������� �������� ����
for weight in weight_of_products: 
    # ���� ������� ��� ������ �������������,
    if weight < max_weight: 
        # ������� ����� �����, ��� ��� � ���������� ��� � �������� ������.
        print('Product {}, weight: {} -passenger car'.format(num, weight)) 
    else:
        # � ��������� ������
        # ������� ����� �����, ��� ��� � ���������� ��� � �������� ������.
        print('Product {}, weight: {} -truck'.format(num, weight))
    # ����������� �������� ������ ����� �� 1
    num += 1