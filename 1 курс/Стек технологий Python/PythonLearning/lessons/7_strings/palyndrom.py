inputString = input("Введите слово - ")
isLengh = len(inputString)
count = 0
result = "yes"

if isLengh < 2:
    result = "no"

while count != (isLengh // 2):
    charA = inputString[count]
    charB = inputString[isLengh - count - 1]
    if(charA != charB):
        result = "no"
        break
    count += 1

print(result)