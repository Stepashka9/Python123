import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''
    for _ in range(length):
        password += random.choice(characters)
    return password


def generate_passwords(number, length):
    passwords = set()
    while len(passwords) < number:
        password = generate_password(length)
        passwords.add(password)
    return list(passwords)


N = int(input("Введите N: "))
K = int(input("Введите K: "))

passwords = generate_passwords(N, K)

for password in passwords:
    print(password)
