from datetime import datetime, timedelta

def is_happy_date(date):
    day = date.day
    month = date.month
    year = date.year
    if day % 4 != 0 and date.weekday() != 0:
        return True
    return False

def find_happy_dates(start_date, n):
    happy_dates = []
    current_date = start_date
    while len(happy_dates) < 3:
        if is_happy_date(current_date):
            happy_dates.append(current_date)
        current_date += timedelta(days=n)
    return happy_dates

input_date = input("Введите исходную дату в формате YYYY/MM/DD: ")
year, month, day = map(int, input_date.split('/'))
n = int(input("Введите число n: "))
start_date = datetime(year, month, day)
happy_dates = find_happy_dates(start_date, n)

for date in happy_dates:
    print(date.strftime('%d %B, %A'))
