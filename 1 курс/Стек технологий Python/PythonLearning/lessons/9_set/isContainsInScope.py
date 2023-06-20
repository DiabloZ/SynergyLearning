# Во входную строку водится последовательность чисел через пробел.
# Для каждого числа выведите слово ”YES” (в отдельной строке), если это число ранее
# встречалось в последовательности или ”NO”, если не встречалось.

numScope = list(map(int, input("Введите через пробел числа - ").split()))
setScope: set = set()
for value in numScope:
    if (setScope.__contains__(value)):
        print("value - " + value.__str__() + " YES")
    else:
        setScope.add(value)
        print("value - " + value.__str__() + " NO")
