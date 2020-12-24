from parseFile import ParseFileByLine

def SolveDay9(filePath, preamble):
    numbers = ParseFileByLine(filePath)
    invalidNumber = SolveDay9A(numbers, preamble)
    SolveDay9B(numbers, invalidNumber)
    print('End of day 9.')

def SolveDay9A(numbers, preamble):
    lastPreambleNumbers = []

    for index in range(preamble):
        lastPreambleNumbers.append(numbers[index])

    index = preamble + 1
        
    for number in numbers[preamble:]:
        isValidCombinationFound = False
        #print(number)

        for priorNumber in lastPreambleNumbers:
            #print('Start of this loop', number, priorNumber, type(number), type(priorNumber))
            if int(number) < int(priorNumber):
                continue
            
            otherNumber = str(int(number) - int(priorNumber))
            #print(number, priorNumber, otherNumber, lastPreambleNumbers)

            if otherNumber == priorNumber:
                #print('Testing for duplicate.')
                aSet = set(lastPreambleNumbers)
                #print(len(aSet), preamble, type(preamble))

                if preamble == len(aSet):
                    #print('This is no duplicate')
                    continue

            if otherNumber in lastPreambleNumbers:
                isValidCombinationFound = True
                #print('This should be run.')
                break

        if not isValidCombinationFound:
            invalidNumber = number
            break
        else:
            lastPreambleNumbers.pop(0)
            lastPreambleNumbers.append(number)

    print(invalidNumber)
    print('End of part 1 of day 9.')
    return int(invalidNumber)

def SolveDay9B(numbers, invalidNumber):
    #print(numbers)
    invalidNumberPosition = numbers.index(str(invalidNumber))
    #print(numbers[:invalidNumberPosition])
    #print(len(numbers[:invalidNumberPosition]), invalidNumberPosition)
    contiguousSet = []
    foundContiguousSet = False
    priorNumbers = numbers[:invalidNumberPosition]
    size = len(priorNumbers)
    index = 0

    while not foundContiguousSet:
        contiguousSet.clear()
        position = index

        while position < size:
            number = int(priorNumbers[position])
            contiguousSet.append(number)
            result = sum(contiguousSet)

            if result == invalidNumber:
                aSet = set(contiguousSet)

                if len(contiguousSet) != len(aSet):
                    break
                else:
                    foundContiguousSet = True
                    break
            elif result > invalidNumber:
                break;

            position += 1

        index += 1
   
    contiguousSet.sort()
    #print(contiguousSet[0], contiguousSet[-1], contiguousSet)
    result = contiguousSet[0] + contiguousSet[-1]
    print(result)
    print('End of part 2 of day 9.')
