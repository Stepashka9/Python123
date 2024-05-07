import random


def generate_exam_schedule(num_exams, disciplines):
    days = ['понедельник', 'вторник', 'среду', 'четверг', 'пятницу']
    times = [9.00, 9.30, 10.00, 10.30, 11.00, 11.30, 12.00, 12.30, 13.00, 13.30, 14.00]

    for i in range(num_exams):
        discipline = random.choice(disciplines)
        day = random.choice(days)
        exam_time = random.choice(times)
        ticket_number = random.randint(1, 20)

        print(
            f"Экзамен по дисциплине «{discipline}» состоится в {day} в {exam_time}. Счастливый билет N {ticket_number}.")


num_exams = int(input("Введите количество экзаменов: "))
disciplines = input("Введите наименования дисциплин через запятую и пробел: ").split(', ')

generate_exam_schedule(num_exams, disciplines)
