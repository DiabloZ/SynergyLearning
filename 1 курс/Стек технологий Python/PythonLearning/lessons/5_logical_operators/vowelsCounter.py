word = input("Введите слово/набор символов - ")

validateChars = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
aCount = 0
eCount = 0
iCount = 0
oCount = 0
uCount = 0

for num in range(len(word)):
    if word[num] == 'a':
        aCount += 1
    elif word[num] == 'e':
        eCount += 1
    elif word[num] == 'i':
        iCount += 1
    elif word[num] == 'o':
        oCount += 1
    elif word[num] == 'u':
        uCount += 1


if aCount == 0 or eCount == 0 or iCount == 0 or oCount == 0 or uCount == 0:
    print("False")
else:
    print("Вы ввели слово/набор символов - " + word)
    print("Кол-во букв  a - " + aCount.__str__())
    print("Кол-во букв  e - " + eCount.__str__())
    print("Кол-во букв  i - " + iCount.__str__())
    print("Кол-во букв  o - " + oCount.__str__())
    print("Кол-во букв  u - " + uCount.__str__())
