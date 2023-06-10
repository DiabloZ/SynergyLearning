n = int(input("Введите натуральное число - "))
i = 2
degree = 0
result = 1
while n >= 1:
    if n % i == 0:
        degree += 1
        n = n // i
    else:
        result *= (degree + 1)
        degree = 0
        i += 1
        if n == 1: break
print(result)