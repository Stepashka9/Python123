from datetime import datetime, timedelta
my_str = '05-17-2024'
date_1 = datetime.strptime(my_str, '%m-%d-%Y')
print(date_1)
days = int(input("Введите количество дней до экзамена: "))
result = date_1 + timedelta(days)
print(result) 