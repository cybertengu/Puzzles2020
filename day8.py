from parseFile import ParseFileByLine

def SolveDay8(filePath):
    instructions = []
    instructions = ParseFileByLine(filePath)

    SolveDay8A(instructions)
    SolveDay8B(instructions)
    print("End of day 8.")

def acc(argument, assemblyTool):
    if argument[0] == '+':
        assemblyTool.accumulator += int(argument[1:])
    elif argument[0] == '-':
        assemblyTool.accumulator -= int(argument[1:])

    assemblyTool.index += 1

    return assemblyTool

def jmp(argument, assemblyTool):
    if argument[0] == '+':
        assemblyTool.index += int(argument[1:])
    if argument[0] == '-':
        assemblyTool.index -= int(argument[1:])

    return assemblyTool

def nop(argument, assemblyTool):
    assemblyTool.index += 1
    return assemblyTool

class AssemblyTool:
    def __init__(self, accumulator, index):
        self.accumulator = accumulator
        self.index = index

def SolveDay8A(instructions):
    accumulator = 0
    index = 0
    assemblyTool = AssemblyTool(accumulator, index)
    argument = []

    switcher = {
                "acc": acc,
                "jmp": jmp,
                "nop": nop
                }
    
    instructionsAmount = len(instructions)
    instructionEncounter = [0] * instructionsAmount

    while index < instructionsAmount:
        currentInstruction = instructions[index]
        data = currentInstruction.split()
        operation = data[0]
        argument = data[1]
        instructionEncounter[index] += 1

        if instructionEncounter[index] > 1:
            break

        assemblyTool = switcher.get(operation)(argument, assemblyTool)
        index = assemblyTool.index

    print(assemblyTool.accumulator)
    print("End of day 8 part 1.")

def SolveDay8B(instructions):
    switcher = {
                "acc": acc,
                "jmp": jmp,
                "nop": nop
                }
    
    instructionsAmount = len(instructions)
    instructionEncounter = [0] * instructionsAmount
    allCorruptOperators = {}
    parseIndex = 0

    for operator in instructions:
        currentOperator = operator[0:3]

        if currentOperator == 'nop':
            allCorruptOperators[parseIndex] = operator.replace('nop', 'jmp')
        elif currentOperator == 'jmp':
            allCorruptOperators[parseIndex] = operator.replace('jmp', 'nop')
        
        parseIndex += 1

    didLoopTerminate = True

    for corruptOperators in allCorruptOperators:
        didLoopTerminate = True
        accumulator = 0
        index = 0
        assemblyTool = AssemblyTool(accumulator, index)
        argument = []
  
        for i in range(instructionsAmount):
            instructionEncounter[i] = 0

        while index < instructionsAmount:
            currentInstruction = instructions[index]

            if index == corruptOperators:
                currentInstruction = allCorruptOperators[index]
                    
            data = currentInstruction.split()
            operation = data[0]
            argument = data[1]

            instructionEncounter[index] += 1

            if instructionEncounter[index] > 1:
                didLoopTerminate = False
                break

            assemblyTool = switcher.get(operation)(argument, assemblyTool)
            index = assemblyTool.index

        if didLoopTerminate:
            break

    print(assemblyTool.accumulator)
    print("End of day 8 part 2.")
