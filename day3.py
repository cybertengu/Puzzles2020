from parseFile import ParseFile

def SolveDay3(filePath):
    testData = ParseFile(filePath)
    SolveDay3A(testData)
    SolveDay3B(testData)
    print("End of day 3.")

def SolveDay3A(testData):
    length = len(testData[0])
    #print(length)
    #print(testData[0])
    currentPosition = 0
    moveRight = 3
    moveDown = 1
    hitTreeCount = 0
    openLocationCount = 0
    for rowIndex, currentLine in enumerate(testData[:-moveDown]):
        currentPosition = (currentPosition + moveRight) % length
        #print(currentPosition)
        secondLine = testData[rowIndex + moveDown]
        currentLocation = secondLine[currentPosition]
        if currentLocation == '#':
            hitTreeCount += 1
            #print("Hit tree")
        else:
            openLocationCount += 1
            #print("No tree")

    print(hitTreeCount)
    #print(openLocationCount)
    print("End of day 3 A.")

def SolveForHitTrees(testData, moveRight, moveDown, length, numberOfRows):
    currentPosition = 0
    hitTreeCount = 0
    openLocationCount = 0
    rowIndex = moveDown
    while rowIndex < numberOfRows:
        currentPosition = (currentPosition + moveRight) % length
        #print(currentPosition)
        currentLine = testData[rowIndex]
        #print(rowIndex + moveDown)
        #print(secondLine)
        currentLocation = currentLine[currentPosition]
        if currentLocation == '#':
            hitTreeCount += 1
            #print("Hit tree")
        rowIndex += moveDown

    return hitTreeCount

def SolveDay3B(testData):
    length = len(testData[0])
    numberOfRows = len(testData)
    
    firstValue = SolveForHitTrees(testData, 1, 1, length, numberOfRows)
    secondValue = SolveForHitTrees(testData, 3, 1, length, numberOfRows)
    thirdValue = SolveForHitTrees(testData, 5, 1, length, numberOfRows)
    fourthValue = SolveForHitTrees(testData, 7, 1, length, numberOfRows)
    fifthValue = SolveForHitTrees(testData, 1, 2, length, numberOfRows)

    #print(firstValue)
    #print(secondValue)
    #print(thirdValue)
    #print(fourthValue)
    #print(fifthValue)

    result = firstValue * secondValue * thirdValue * fourthValue * fifthValue
    print(result)

    print("End of day 3 B.")
