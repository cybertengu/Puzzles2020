def SolveDay10(filePath):
    jolts = []
    with open(filePath, 'r') as file:
        for line in file:
            if line == '\n':
                continue
            jolt = int(line[:-1])
            jolts.append(jolt)

    jolts.sort()
    SolveDay10A(jolts)
    SolveDay10B(jolts)

def SolveDay10A(jolts):
    oneAway = []
    threeAway = []
    priorJolt = 0

    for jolt in jolts:
        if jolt - priorJolt == 1:
            oneAway.append(jolt)
        elif jolt - priorJolt == 3:
            threeAway.append(jolt)

        priorJolt = jolt

    deviceJolt = jolts[-1] + 3
    threeAway.append(deviceJolt)
    oneAwaySize = len(oneAway)
    threeAwaySize = len(threeAway)
    result = oneAwaySize * threeAwaySize

    print(result)
    print('End of part 1 of day 10.')

def SolveDay10B(jolts):
    cache = {0:1}

    for jolt in jolts:
        cache[jolt] = 0

        if jolt - 1 in cache:
            cache[jolt] += cache[jolt - 1]
        if jolt - 2 in cache:
            cache[jolt] += cache[jolt - 2]
        if jolt - 3 in cache:
            cache[jolt] += cache[jolt - 3]

    maxCount = max(cache)
    print(cache[maxCount])
    print('End of part 2 of day 10.')
