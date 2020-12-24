import copy

def SolveDay11(filePath):
    seatingChart = []

    with open(filePath, 'r') as file:
        for line in file:
            if line == '\n':
                continue
            result = line[:-1]
            seatingChart.append(result)
 
#    TestMethods()
    rowSize = len(seatingChart)
    columnSize = len(seatingChart[0])
    SolveDay11A(seatingChart, rowSize, columnSize)
    SolveDay11B(seatingChart, rowSize, columnSize)
    print('End of day 11.')

def SolveDay11A(seatingChart, rowSize, columnSize):
    occupiedSeatCount = 0
    hasMoreChanges = True
    
    while hasMoreChanges:
        newSeatingChart = copy.copy(seatingChart)
        hasMoreChanges = False

        for rowIndex, row in enumerate(seatingChart):
            for columnIndex, individualCell in enumerate(row):
                if individualCell == '.':
                    continue
                elif individualCell == 'L':
                    adjacentSeats = GetSeatsAdjacent(seatingChart, rowIndex, columnIndex, rowSize, columnSize)
                
                    if not IsAnySeatOccupied(adjacentSeats):
                        occupiedSeatCount += 1
                        newRow = newSeatingChart[rowIndex][:columnIndex] + '#' + newSeatingChart[rowIndex][columnIndex + 1:]
                        newSeatingChart[rowIndex] = newRow
                        hasMoreChanges = True
                elif individualCell == '#':
                    leftColumnIndex = columnIndex - 1
                    rightColumnIndex = columnIndex + 1
                    topRowIndex = rowIndex - 1
                    bottomRowIndex = rowIndex + 1
                    ignoreLeftColumnIndex = leftColumnIndex < 0
                    ignoreRightColumnIndex = rightColumnIndex >= columnSize 
                    ignoreTopRowIndex = topRowIndex < 0
                    ignoreBottomRowIndex = bottomRowIndex >= rowSize
                    surroundingCount = 0
                    
                    if not ignoreTopRowIndex:
                        topRow = seatingChart[topRowIndex]
                        topMiddle = topRow[columnIndex]
                        
                        if IsSeatOccupied(topMiddle):
                            surroundingCount += 1

                        if not ignoreLeftColumnIndex:
                            topLeft = topRow[leftColumnIndex]
                            if IsSeatOccupied(topLeft):
                                surroundingCount += 1

                        if not ignoreRightColumnIndex:
                            topRight = topRow[rightColumnIndex]
                            if IsSeatOccupied(topRight):
                                surroundingCount += 1

                    if not ignoreLeftColumnIndex:
                        middleLeft = row[leftColumnIndex]
                        if IsSeatOccupied(middleLeft):
                            surroundingCount += 1

                    if surroundingCount == 4:
                        occupiedSeatCount -= 1
                        hasMoreChanges = True
                        newRow = newSeatingChart[rowIndex][:columnIndex] + 'L' + newSeatingChart[rowIndex][columnIndex + 1:]
                        newSeatingChart[rowIndex] = newRow
                        continue

                    if not ignoreRightColumnIndex:
                        middleRight = row[rightColumnIndex]
                        if IsSeatOccupied(middleRight):
                            surroundingCount += 1
                            if surroundingCount >= 4:
                                occupiedSeatCount -= 1
                                hasMoreChanges = True
                                newRow = newSeatingChart[rowIndex][:columnIndex] + 'L' + newSeatingChart[rowIndex][columnIndex + 1:]
                                newSeatingChart[rowIndex] = newRow
                                continue

                    if not ignoreBottomRowIndex:
                        bottomRow = seatingChart[bottomRowIndex]
                        bottomMiddle = bottomRow[columnIndex]

                        if IsSeatOccupied(bottomMiddle):
                            surroundingCount += 1
                            if surroundingCount >= 4:
                                occupiedSeatCount -= 1
                                hasMoreChanges = True
                                newRow = newSeatingChart[rowIndex][:columnIndex] + 'L' + newSeatingChart[rowIndex][columnIndex + 1:]
                                newSeatingChart[rowIndex] = newRow
                                continue

                        if not ignoreLeftColumnIndex:
                            bottomLeft = bottomRow[leftColumnIndex]
                            if IsSeatOccupied(bottomLeft):
                                surroundingCount += 1
                                if surroundingCount >= 4:
                                    occupiedSeatCount -= 1
                                    hasMoreChanges = True
                                    newRow = newSeatingChart[rowIndex][:columnIndex] + 'L' + newSeatingChart[rowIndex][columnIndex + 1:]
                                    newSeatingChart[rowIndex] = newRow
                                    continue

                        if not ignoreRightColumnIndex:
                            bottomRight = bottomRow[rightColumnIndex]
                            if IsSeatOccupied(bottomRight):
                                surroundingCount += 1
                                if surroundingCount >=4:
                                    occupiedSeatCount -= 1
                                    hasMoreChanges = True
                                    newRow = newSeatingChart[rowIndex][:columnIndex] + 'L' + newSeatingChart[rowIndex][columnIndex + 1:]
                                    newSeatingChart[rowIndex] = newRow
                                    continue

        seatingChart = copy.copy(newSeatingChart)

    print(occupiedSeatCount)
    print('End of part A of day 11.')

def SolveDay11B(seatingChart, rowSize, columnSize):
    occupiedSeatCount = 0
    hasMoreChanges = True
    
    while hasMoreChanges:
        newSeatingChart = copy.deepcopy(seatingChart)
        hasMoreChanges = False

        for rowIndex, row in enumerate(seatingChart):
            for columnIndex, individualCell in enumerate(row):
                if individualCell == '.':
                    continue
                elif individualCell == '#':
                    if SeeNumberOfOccupiedSeat(seatingChart, rowIndex, rowIndex - 1, rowIndex + 1, columnIndex, columnIndex - 1, columnIndex + 1, rowSize, columnSize, 5):
                        newRow = newSeatingChart[rowIndex][:columnIndex] + 'L' + newSeatingChart[rowIndex][columnIndex + 1:]
                        newSeatingChart[rowIndex] = newRow
                        occupiedSeatCount -= 1
                        hasMoreChanges = True
                elif individualCell == 'L':
                    if not SeeNumberOfOccupiedSeat(seatingChart, rowIndex, rowIndex - 1, rowIndex + 1, columnIndex, columnIndex - 1, columnIndex + 1, rowSize, columnSize, 1):
                        newRow = newSeatingChart[rowIndex][:columnIndex] + '#' + newSeatingChart[rowIndex][columnIndex + 1:]
                        newSeatingChart[rowIndex] = newRow
                        occupiedSeatCount += 1
                        hasMoreChanges = True

        seatingChart = copy.copy(newSeatingChart)

    print(occupiedSeatCount)
    print('End of part B of day 11.')

def SeeNumberOfOccupiedSeat(seatingChart, rowIndex, topRowIndex, bottomRowIndex, columnIndex, leftColumnIndex, rightColumnIndex, rowSize, columnSize, number):
    occupiedSeatCount = 0    

    while bottomRowIndex < rowSize:
        currentSeat = seatingChart[bottomRowIndex][columnIndex]
        if currentSeat == 'L':
            break
        elif IsSeatOccupied(currentSeat):
            occupiedSeatCount +=1
            break
        else:
            bottomRowIndex += 1

    if occupiedSeatCount >= number:
        return True

    while topRowIndex > -1:
        currentSeat = seatingChart[topRowIndex][columnIndex]
        if currentSeat == 'L':
            break
        elif IsSeatOccupied(currentSeat):
            occupiedSeatCount +=1
            break
        else:
            topRowIndex -= 1

    if occupiedSeatCount >= number:
        return True

    while leftColumnIndex > -1:
        currentSeat = seatingChart[rowIndex][leftColumnIndex]
        if currentSeat == 'L':
            break
        elif IsSeatOccupied(currentSeat):
            occupiedSeatCount += 1
            break
        else:
            leftColumnIndex -= 1

    if occupiedSeatCount >= number:
        return True

    while rightColumnIndex < columnSize:
        currentSeat = seatingChart[rowIndex][rightColumnIndex]
        if currentSeat == 'L':
            break
        elif IsSeatOccupied(currentSeat):
            occupiedSeatCount += 1
            break
        else:
            rightColumnIndex += 1

    if occupiedSeatCount >= number:
        return True

    topRowIndex = rowIndex - 1
    leftColumnIndex = columnIndex - 1

    while leftColumnIndex > -1 and topRowIndex > -1:
        currentSeat = seatingChart[topRowIndex][leftColumnIndex]
        if currentSeat == 'L':
            break
        elif IsSeatOccupied(currentSeat):
            occupiedSeatCount += 1
            break
        else:
            leftColumnIndex -= 1
            topRowIndex -= 1

    if occupiedSeatCount >= number:
        return True

    leftColumnIndex = columnIndex - 1
    bottomRowIndex = rowIndex + 1

    while leftColumnIndex > -1 and bottomRowIndex < rowSize:
        currentSeat = seatingChart[bottomRowIndex][leftColumnIndex]
        if currentSeat == 'L':
            break
        elif IsSeatOccupied(currentSeat):
            occupiedSeatCount += 1
            break
        else:
            leftColumnIndex -= 1
            bottomRowIndex += 1
    
    if occupiedSeatCount >= number:
        return True

    topRowIndex = rowIndex - 1
    rightColumnIndex = columnIndex + 1

    while rightColumnIndex < columnSize and topRowIndex > -1:
        currentSeat = seatingChart[topRowIndex][rightColumnIndex]
        if currentSeat == 'L':
            break
        elif IsSeatOccupied(currentSeat):
            occupiedSeatCount += 1
            break
        else:
            topRowIndex -= 1
            rightColumnIndex += 1

    if occupiedSeatCount >= number:
        return True

    rightColumnIndex = columnIndex + 1
    bottomRowIndex = rowIndex + 1

    while rightColumnIndex < columnSize and bottomRowIndex < rowSize:
        currentSeat = seatingChart[bottomRowIndex][rightColumnIndex]
        if currentSeat == 'L':
            break
        elif IsSeatOccupied(currentSeat):
            occupiedSeatCount += 1
            break
        else:
            rightColumnIndex += 1
            bottomRowIndex += 1

    if occupiedSeatCount >= number:
        return True
    else:
        return False
    

def GetSeatsAdjacent(seatingChart, rowIndex, columnIndex, rowSize, columnSize):
    leftColumnIndex = columnIndex - 1
    rightColumnIndex = columnIndex + 1
    topRowIndex = rowIndex - 1
    bottomRowIndex = rowIndex + 1
    ignoreLeftColumnIndex = leftColumnIndex < 0
    ignoreRightColumnIndex = rightColumnIndex >= columnSize 
    ignoreTopRowIndex = topRowIndex < 0
    ignoreBottomRowIndex = bottomRowIndex >= rowSize
    adjacentSeats = []
    
    if not ignoreLeftColumnIndex:
        adjacentSeats.append(seatingChart[rowIndex][leftColumnIndex])

        if not ignoreTopRowIndex:
            adjacentSeats.append(seatingChart[topRowIndex][leftColumnIndex])
        
        if not ignoreBottomRowIndex:
            adjacentSeats.append(seatingChart[bottomRowIndex][leftColumnIndex])

    if not ignoreRightColumnIndex:
        adjacentSeats.append(seatingChart[rowIndex][rightColumnIndex])

        if not ignoreTopRowIndex:
            adjacentSeats.append(seatingChart[topRowIndex][rightColumnIndex])
        
        if not ignoreBottomRowIndex:
            adjacentSeats.append(seatingChart[bottomRowIndex][rightColumnIndex])

    if not ignoreTopRowIndex:
        adjacentSeats.append(seatingChart[topRowIndex][columnIndex])

    if not ignoreBottomRowIndex:
        adjacentSeats.append(seatingChart[bottomRowIndex][columnIndex])

    return adjacentSeats

def IsAnySeatOccupied(seats):
    for seat in seats:
        if IsSeatOccupied(seat):
            return True

    return False

def IsSeatOccupied(seat):
    if seat == '#':
        return True
    else:
        return False

def PrintSeatingChart(seatingChart):
    for row in seatingChart:
        print(row)

def TestMethods():
    seats = ['L.LL.LL.LL', 'LLLLLLL.LL', 'L.L.L..L..', 'LLLL.LL.LL', 'L.LL.LL.LL', 'L.LLLLL.LL', '..L.L.....', 'LLLLLLLLLL', 'L.LLLLLL.L', 'L.LLLLL.LL']
    row = seats[0]
    
    print('Expected: true', IsSeatOccupied('#'))
    print('Expected: false', IsSeatOccupied(seats[0][0]))
    rowSize = len(seats)
    columnSize = len(seats[0])
    print(rowSize, columnSize)
    adjacentSeats = GetSeatsAdjacent(seats, 0, 0, rowSize, columnSize)
    print('Expected: false', IsAnySeatOccupied(adjacentSeats))
    adjacentSeats = GetSeatsAdjacent(seats, 9, 9, rowSize, columnSize)
    print('Expected: false', IsAnySeatOccupied(adjacentSeats))
    adjacentSeats = GetSeatsAdjacent(seats, 5, 5, rowSize, columnSize)
    print('Expected: false', IsAnySeatOccupied(adjacentSeats))

