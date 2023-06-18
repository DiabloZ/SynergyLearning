size = int(input("Введите кол-во строк - "))
array = []

for i in range(0, size):
    string = int(input("Введите " + (i + 1).__str__() + " значение - "))
    array.insert(0, string)

print(array)
