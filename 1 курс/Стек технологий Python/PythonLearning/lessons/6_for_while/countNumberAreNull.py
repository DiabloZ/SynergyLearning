n = int(input("Введите сколько раз будем писать число - "))
zeroCount = 0
while (n > 0):
    inputNumber = int(input("Введите число - "))
    if inputNumber == 0:
        zeroCount += 1
    n += -1
print(zeroCount)
