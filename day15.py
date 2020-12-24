def SolveDay15(filepath):
    print('Start of day 15 part 1.')
    SolveDay15A(filepath, 2020)
    #SolveDay15A(filepath, 10)
    print('End of day 15 part 1.')
    print('Start of day 15 part 2.')
    SolveDay15A(filepath, 30000000)
    print('End of day 15 part 2.')
    print('End of day 15.')

def SolveDay15A(filepath, expectedNumber):
    with open(filepath, 'r') as file:
        for line in file:
            if line == '\n':
                continue

            startingNumbers = (line[:-1]).split(',')

    numbers = []
    turnCounter = 1
    numberEncountered = {}
    numbersSize = len(numbers)

    for number in startingNumbers:
        numbers.append((number, turnCounter))
        numberEncountered[number] = turnCounter
        turnCounter += 1
   
    while turnCounter <= expectedNumber:
        lastNumber = numbers[-1][0]
        #wasNumberSpokenBefore = False

        if lastNumber in numberEncountered and numberEncountered[lastNumber] != turnCounter - 1:
            #print('in if', numberEncountered[lastNumber], turnCounter - 1)
            oldIndex = numberEncountered[lastNumber]
            numberEncountered[lastNumber] = turnCounter - 1
            newNumber = turnCounter - oldIndex - 1
            numbers.append((str(newNumber), turnCounter))
        #for sublist in reversed(numbers[:-1]):
        #    if sublist[0] == lastNumber:
        #        index = sublist[1]
        #        newNumber = turnCounter - index - 1
        #        numbers.append((str(newNumber), turnCounter))
        #        wasNumberSpokenBefore = True
        #        break
        else:
            #print('in else')
            numberEncountered[lastNumber] = turnCounter - 1
            newNumber = '0'
            numbers.append((newNumber, turnCounter))

        #print(lastNumber, turnCounter, newNumber, numbers)
        turnCounter += 1

    result = numbers[-1][0]
    print(result)

