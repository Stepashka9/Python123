# Импортируем наш созданный модуль
import laba_6_module

# Заданный список A
A = [3, 5, 7, 5, 6, 8]

# Заданное значение K
K = 5

# Вызываем функцию для переписывания элементов, не равных K
B = laba_6_module.rewrite_list(A, K)

# Выводим исходный список A и полученный список B
print("Исходный список A:", A)
print("Результат переписывания элементов, не равных", K, "в список B:", B)