import copy

def SolveDay14(filePath):
    print('Started Day 14.')
    lines = []

    with open(filePath, 'r') as file:
        for line in file:
            if line == '\n':
                continue

            result = line[:-1]
            lines.append(result)

    SolveDay14A(lines)
    SolveDay14B(lines)
    print("End of day 14.")

def SolveDay14A(lines):
    memory = {}

    for line in lines:
        if 'mask' in line:
            mask = line.split('=')[1][1:]
        else:
            firstBracketIndex = line.find('[')
            secondBracketIndex = line.find(']')
            memoryLocation = line[firstBracketIndex + 1: secondBracketIndex]
            memoryValueToAdd = line.split('=')[1][1:]
            binaryValue = str(ConvertDecimalToBinary(int(memoryValueToAdd)))

            if not memoryLocation in memory:
                memory[memoryLocation] = ('0' * 36)

            updatedValue = UpdateMemory(memory[memoryLocation], binaryValue, mask)
            memory[memoryLocation] = updatedValue

    result = 0

    for key, item in memory.items():
        result += ConvertBinaryToDecimal(item)
    
    print(result)
    print('End of day 14 part 1.')

def SolveDay14B(lines):
    memory = {}

    for line in lines:
        if 'mask' in line:
            mask = line.split('=')[1][1:]
        else:
            firstBracketIndex = line.find('[')
            secondBracketIndex = line.find(']')
            memoryLocation = line[firstBracketIndex + 1: secondBracketIndex]
            memoryValueToInsert = line.split('=')[1][1:]
            binaryValue = str(ConvertDecimalToBinary(int(memoryValueToInsert)))
            
            if not memoryLocation in memory:
                memory[memoryLocation] = '0' * 36

            getMemoryAddresses = GetMemoryAddresses(memoryLocation, binaryValue, mask)

            for address in getMemoryAddresses:
                memory[address] = memoryValueToInsert

    result = 0

    for key, item in memory.items():
        result += int(item)
    
    print(result)
    print('End of day 14 part 2.')

def UpdateMemory(currentMemory, newValue, mask):
    size = len(newValue)
    fullNewValue = ('0' * (36 - size)) + newValue
    updatedValue = []

    for index in range(len(currentMemory)):
        if mask[index] == 'X':
            updatedValue.append(fullNewValue[index])
        elif mask[index] == '0':
            updatedValue.append('0')
        elif mask[index] == '1':
            updatedValue.append('1')
            
    updatedMemory = ''.join(updatedValue)

    return updatedMemory

def GetMemoryAddresses(currentMemoryLocation, newValue, mask):
    size = len(newValue)
    fullNewValue = ('0' * (36 - size)) + newValue
    updatedValues = []
    xIndex = []

    if currentMemoryLocation in decimalToBinary:
        currentMemoryLocationBinary = decimalToBinary[currentMemoryLocation]
    else:
        currentMemoryLocationBinary = ConvertDecimalToBinary(int(currentMemoryLocation))
        decimalToBinary[currentMemoryLocation] = currentMemoryLocationBinary

    currentMemoryLocationBinary = '0' * (36 - len(currentMemoryLocationBinary)) + currentMemoryLocationBinary

    for index in range(len(mask)):
        if mask[index] == 'X':
            xIndex.append(index)
            updatedValues.append('X')
        elif mask[index] == '0':
            updatedValues.append(currentMemoryLocationBinary[index])
        elif mask[index] == '1':
            updatedValues.append('1')

    updatedMemory = ''.join(updatedValues)
    xSize = len(xIndex)

    fullSize = 1

    for index in range(1, xSize + 1):
        fullSize *= 2

    binary = bin(0).replace("0b", "")
    updatedMemories = []

    while fullSize > 0:
        maskedMemory = copy.deepcopy(updatedValues)
        fullSize -= 1
        binaryLength = len(binary)

        for index, x in enumerate(xIndex):
            if binaryLength < xSize:
                binaryString = '0' * (xSize - binaryLength) + binary
            else:
                binaryString = str(binary)

            maskedMemory[x] = binaryString[index]
        
        updatedMemories.append("".join(maskedMemory))
        binary = bin(1 + int(binary, 2)).replace("0b", "")
        
        if binaryLength < xSize:
            binaryLength = len(binary)

    return updatedMemories


decimalToBinary = {}
binaryToDecimal = {}

def ConvertDecimalToBinary(value):
    if value in decimalToBinary:
        return decimalToBinary[value]

    result = bin(value).replace("0b", "")
    decimalToBinary[value] = result
    binaryToDecimal[result] = value

    return result

def ConvertBinaryToDecimal(value):
    if value in binaryToDecimal:
        return binaryToDecimal[value]

    intValue = int(value, 2)
    binaryToDecimal[value] = intValue

    return intValue
