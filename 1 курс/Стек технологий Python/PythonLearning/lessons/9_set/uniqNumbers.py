# В первую строку вводится число N – количество чисел (1 ≤ N ≤ 100000).
# Во вторую строку вводится через пробел N чисел, каждое не превышает 2*10e9 по модулю.
# Требуется выяснить, сколько среди этих чисел различных.
# Выведите число, равное количеству различных чисел среди данных.

size = int(input("Введите количество чисел - "))
setScope = set(map(int, input("Введите через пробел числа - ").split()))
print("Уникальных чисел - " + len(setScope).__str__())
