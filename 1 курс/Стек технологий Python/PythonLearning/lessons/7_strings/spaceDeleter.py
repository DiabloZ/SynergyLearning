str = input("Введите строку - ")
tempString = str

while str == tempString:
    tempString = str
    str = str.replace("  ", " ")

    if tempString != str:
        tempString = str
    else:
        break

print(str)
