def SolveDay2(filePath):
    #testpasswords = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    passwords = []
    with open(filePath, 'r') as file:
        for line in file:
            passwords.append(line)
    SolveDay2A(passwords)
    SolveDay2B(passwords)

def SolveDay2A(passwords):
    validPasswordsCount = 0
    for currentLine in enumerate(passwords):
        tokens = currentLine[1].split()
        minValue = int(limits[0])
        maxValue = int(limits[1])
        letter = tokens[1][:-1]
        password = tokens[2]
        letterAmountFound = password.count(letter)
        if letterAmountFound >= minValue and letterAmountFound <= maxValue:
            validPasswordsCount += 1

    print(validPasswordsCount)

    print("End of day 2 A.")

def SolveDay2B(passwords):
    validPasswordsCount = 0
    for currentLine in enumerate(passwords):
        tokens = currentLine[1].split()
        limits = tokens[0].split('-')
        firstPosition = int(limits[0])
        secondPosition = int(limits[1])
        letter = tokens[1][:-1]
        password = tokens[2]
        letterAtPosition1 = password[firstPosition - 1]
        letterAtPosition2 = password[secondPosition - 1]
        if (letterAtPosition1 == letter and letterAtPosition2 != letter) or (letterAtPosition2 == letter and letterAtPosition1 != letter):
            validPasswordsCount += 1

    print(validPasswordsCount)

    print("End of day 2 B.")
