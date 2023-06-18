size = int(input("Введите кол-во строк - "))
array = list(map(int, input("Введите значения по кол-ву строк указанному выше - ").split()))
resultArray = []
middleOfArray = size // 2
isNotEvenArray = size % 2 != 0

count = 0
while middleOfArray > count:
    resultArray.append(array[count])
    count += 1
    resultArray.append(array[count * -1])
    if isNotEvenArray and count == middleOfArray:
        resultArray.append(array[count])
print(resultArray)
