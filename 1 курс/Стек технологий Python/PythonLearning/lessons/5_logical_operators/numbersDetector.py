number = int(input("Введи любое целое число - "))

zeroString = "нулевое число"
positiveOddNumber = "положительное нечетное число"
positiveEvenNumber = "положительное четное число"
negativeOddNumber = "отрицательное нечетное число"
negativeEvenNumber = "отрицательное четное число"
evenNumberMessage = "число является четным"
oddNumberMessage = "число не является четным"

isEvenNumber = number % 2 == 0

#проверка добавлена исключительно для соответствия требованию -
#"Если число не является четным - выведите сообщение "число не является четным""

if isEvenNumber:
    print(evenNumberMessage)
else:
    print(oddNumberMessage)

if number == 0:
    print(zeroString)
elif number > 0:
    if isEvenNumber:
        print(positiveEvenNumber)
    else:
        print(positiveOddNumber)
elif number < 0:
    if isEvenNumber:
        print(negativeEvenNumber)
    else:
        print(negativeOddNumber)