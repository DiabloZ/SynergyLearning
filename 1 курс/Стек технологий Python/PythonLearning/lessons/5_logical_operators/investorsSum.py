minSum = float(input("Введите минимальную сумму инвестиций - "))
mikeSum = float(input("Введите сумму инвестиций Майка - "))
ivanSum = float(input("Введите сумму инвестиций Ивана - "))

investorsCount = 0

if (minSum <= mikeSum and minSum <= ivanSum):
    investorsCount += 2
elif (minSum <= mikeSum):
    investorsCount += 1
    print("Mike")
elif (minSum <= ivanSum):
    investorsCount += 1
    print("Ivan")
elif (minSum <= (mikeSum + ivanSum)):
    investorsCount += 1
print(investorsCount)
