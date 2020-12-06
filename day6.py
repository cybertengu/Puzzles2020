from parseFile import ParseFile

def SolveDay6(filePath):
    #SolveDay6A('test6.txt')
    #SolveDay6B('test6.txt')
    SolveDay6A(filePath)
    SolveDay6B(filePath)
    print("End of day 6.")

def SolveDay6A(filePath):
    lines = []
    questions = {}
    counts = []
    with open(filePath, 'r') as file:
        for line in file:
            line = line[:-1]
            #lines.append(line[:-1])
            for question in line:
                questions[question] = 1
            if line == '':
                counts.append(len(questions))
                questions.clear()

    result = sum(counts)

    print(result)
    print("End of day 6 A.")

def SolveDay6B(filePath):
    lines = []
    questions = {}
    counts = []
    groupSize = 0
    groupIndex = 0
    with open(filePath, 'r') as file:
        for line in file:
            groupSize += 1
            line = line[:-1]
            #lines.append(line[:-1])
            for question in line:
                if question in questions.keys():
                    questions[question] += 1
                else:
                    questions[question] = 1
            if line == '':
                groupSize -= 1
                counter = 0
                counts.insert(groupIndex, 0)
                #print('Questions: ', questions, ' GroupIndex: ', groupIndex, ' Group Size: ', groupSize)
                for aQuestion in questions:
                    #print(aQuestion)
                    answeredAmount = questions[aQuestion]
                    if answeredAmount == groupSize:
                        count = counts[groupIndex] + 1
                        counts[groupIndex] = count
                        #print(counts)
                questions.clear()
                groupSize = 0
                groupIndex += 1

    result = sum(counts)

    print(result)

    print("End of day 6 B.")
