def SolveDay13(filePath):
    lines = []

    with open(filePath, 'r') as file:
        for line in file:
            if line == '\n':
                continue

            result = line[:-1]
            lines.append(result)

    timestamp = int(lines[0])
    busIds = lines[1].split(',')

    SolveDay13A(timestamp, busIds)
    SolveDay13B(busIds)
    print("End of day 13.")

def SolveDay13A(timestamp, busIds):
    isNotFound = True
    foundBusId = -1
    results = {}
    smallestValue = 100000000

    for busId in busIds:
        if busId == 'x':
            continue

        results[busId] = timestamp % int(busId)
        newValue = int(busId) - results[busId]

        if smallestValue > newValue:
            smallestValue = newValue
            foundBusId = busId

    newTimestamp = timestamp + smallestValue
    result = smallestValue * int(foundBusId)
    print(result)
    print('End of day 13 part A.')

def SolveDay13B(busIds):
    crt = []

    for index, busId in enumerate(busIds):
        if busId == 'x':
            continue

        crt.append((int(busId), index))

    leastCommonMultipler = 1
    timestamp = 0

    for index in range(len(crt) - 1):
        busId = crt[index + 1][0]
        indexValue = crt[index + 1][1]
        leastCommonMultipler *= crt[index][0]

        while (timestamp + indexValue) % busId != 0:
            timestamp += leastCommonMultipler

    print(timestamp)
    print('End of day 13 part B.')

