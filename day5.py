from parseFile import ParseFileByLine

def SolveDay5(filePath):
    testDataList = ParseFileByLine(filePath)
    maxRowValue = 127
    maxColumnValue = 7

    SolveDay5A(testDataList, maxRowValue, maxColumnValue)
    SolveDay5B(testDataList, maxRowValue, maxColumnValue)
    print("End of day 5.")

def SolveDay5A(testDataList, maxRowValue, maxColumnValue):
    rowRoot = Node(0, maxRowValue)
    columnRoot = Node(0, maxColumnValue)
    highestSeatId = -1

    for element in testDataList:
        if len(element) < 10:
            print("This should never happened. Might be a bug in the parser logic.")
            break

        rowInformation = element[0:7]
        columnInformation = element[7:10]
        
        rowId = GetId(rowRoot, rowInformation, 0)
        columnId = GetId(columnRoot, columnInformation, 0)
        seatId = rowId * 8 + columnId
        
        if highestSeatId < seatId:
            highestSeatId = seatId
    
    print(highestSeatId)
    print("End of day 5 A.")

#    BFFFBBFRRR: row 70, column 7, seat ID 567.
#    FFFBBBFRRR: row 14, column 7, seat ID 119.
#    BBFFBBFRLL: row 102, column 4, seat ID 820.

def SolveDay5B(testDataList, maxRowValue, maxColumnValue):
    rowRoot = Node(0, maxRowValue)
    columnRoot = Node(0, maxColumnValue)
    seatIds = []

    for element in testDataList:
        if len(element) < 10:
            print("This should never happened. Might be a bug in the parser logic.")
            break
        
        rowInformation = element[0:7]
        columnInformation = element[7:10]
        
        rowId = GetId(rowRoot, rowInformation, 0)
        columnId = GetId(columnRoot, columnInformation, 0)
        seatId = rowId * 8 + columnId
        seatIds.append(seatId)
    
    seatIds.sort()
    missingNumbers = [x for x in range(seatIds[0], seatIds[-1]+1) if x not in seatIds] 
    print(missingNumbers[0])
    print("End of day 5 B.")

# Logic of what I think will happen.
#FBF
#FBF. Start with F, left node created with (0, 3). Go on left node with BF. 
#BF. Start with B, right node created with (2, 3). Go on right node with F.
#F. Start with F, left node created with (2, 2). Return min value of 2.
#FBB
#FBB. Start with F, Go on left with BB.
#BB. Start with B, Go on right with B.
#B. Start with B, create right with (3, 3). Return with min value of 3.
#RLR
#R with LR. 0 - 7. 4, 7. Go right.
#L with R. 4 - 7. 4, 5. Go left.
#R. 4 - 5. 
def GetId(root, seat, value):
    if seat == '':
        return root.minValue 
    
    firstLetter = seat[0]
    
    if firstLetter == 'F' or firstLetter == 'L':
        if root.left is None:
            newStartMaxValue = (1 + root.maxValue - root.minValue) / 2 + root.minValue
            root.left = Node(root.minValue, newStartMaxValue - 1)
        if len(seat) > 1:
            value = GetId(root.left, seat[1:], value)
        else:
            value = GetId(root.left, '', value)
    elif firstLetter == 'B' or firstLetter == 'R':
        if root.right is None:
            newStartMaxValue = (1 + root.maxValue - root.minValue) / 2 + root.minValue
            root.right = Node(newStartMaxValue, root.maxValue)
        if len(seat) > 1:
            value = GetId(root.right, seat[1:], value)
        else:
            value = GetId(root.right, '', value)
    return int(value)

class Node:
    def __init__(self, minValue, maxValue):
        self.left = None
        self.right = None
        self.minValue = minValue
        self.maxValue = maxValue

# 0 - 127
# F means 0 - 63 = (127 - 0) / 2 + 0 = 63.5
# B means 32 - 63 = (63 - 32) / 2 + 32 = 63.5
# F means 32 - 47
# B means 40 - 47
# B means 44 - 47
# F means 44 - 45
# F means 44
