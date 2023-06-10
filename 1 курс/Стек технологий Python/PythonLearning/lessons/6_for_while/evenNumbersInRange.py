a = int(input("Введите число а - "))
b = int(input("Введите число б - "))

resultString = "В введённом отрезке целые числа - "

if (a % 2 == 0):
    a += 1
if (b % 2 == 0):
    b -= 1
for i in range(a, b, 2):
    resultString += " " + (i + 1).__str__()
print(resultString)
