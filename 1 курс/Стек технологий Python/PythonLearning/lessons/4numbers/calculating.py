import math

countNumber = 5
baseNumber = int(input("Введи целое число из 5 символов - "))

digits = int(math.log10(baseNumber)) + 1
if digits > countNumber or digits < countNumber:
    exit("Я так не играю.")

first = baseNumber % 10
baseNumber //= 10
second = baseNumber % 10
baseNumber //= 10
third = baseNumber % 10
baseNumber //= 10
fourth = baseNumber % 10
baseNumber //= 10
fifth = baseNumber % 10

result = ((second ** first)) * third / (fifth - fourth)

print("И у нас получается - " + result.__str__())
