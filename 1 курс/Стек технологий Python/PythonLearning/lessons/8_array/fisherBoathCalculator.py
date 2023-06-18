def prepareFishing():
    global fisherCount, fisherWeights, maxWeight
    maxWeight = int(input("Введите максимальную массу для лодки  - "))
    fisherCount = int(input("Введите кол-во рыбаков  - "))


def collectFishermans(fisherCount):
    fisherWeights = []
    for fisherNumber in range(0, fisherCount):
        fisherWeight = int(input("Введите вес " + (fisherNumber + 1).__str__() + " рыбака  - "))
        fisherWeights.append(fisherWeight)
    return fisherWeights


def calculateBoads(maxWeight:int, fisherWeights:list):
    countOfBoads = 0
    arr = fisherWeights
    arr.sort(reverse=True)
    tempFishers = []

    while(arr != tempFishers):
        tempFishers = arr.copy()

        for fisherNum in range(0, len(tempFishers)):
            if len(tempFishers) != len(arr) or len(arr) <= fisherNum:
                continue

            fisher = tempFishers[fisherNum]

            if fisher == maxWeight:
                countOfBoads += 1
                arr.pop(fisherNum)
                continue

            if len(arr) == 1 and fisher < maxWeight:
                countOfBoads += 1
                arr.pop(fisherNum)
                continue

            if fisher > maxWeight:
                arr.pop(fisherNum)
                continue

            for otherFisherNum in range(fisherNum + 1, len(tempFishers)):
                otherFisher = tempFishers[otherFisherNum]

                if fisher + otherFisher <= maxWeight:
                    countOfBoads += 1
                    arr.pop(otherFisherNum)
                    arr.pop(fisherNum)
                    break

    return countOfBoads


prepareFishing()
fisherWeights = collectFishermans(fisherCount)
boards = calculateBoads(maxWeight, fisherWeights)

print(boards)
