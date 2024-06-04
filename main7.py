def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))


def find_number_with_max_digit_sum(numbers):
    max_sum = 0
    number_with_max_sum = None

    for number in numbers:
        current_sum = sum_of_digits(number)
        if current_sum > max_sum:
            max_sum = current_sum
            number_with_max_sum = number

    return number_with_max_sum