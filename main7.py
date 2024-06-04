def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

def find_max_sum_number(numbers):
    max_sum = 0
    max_number = None

    for num in numbers:
        current_sum = sum_of_digits(num)
        if current_sum > max_sum:
            max_sum = current_sum
            max_number = num

    return max_number

if __name__ == "__main__":
    N = int(input("Введите количество целых чисел: "))
    numbers = []

    for i in range(N):
        num = int(input("Введите число: "))
        numbers.append(num)

    max_number = find_max_sum_number(numbers)

    print(f"Число с максимальной суммой цифр: {max_number}")