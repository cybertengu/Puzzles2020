def SolveDay18(filepath):
    print('Start of day 18.')
    
    lines = []
    with open(filepath, 'r') as file:
        for line in file:
            if line == '\n':
                continue
            else:
                lines.append(line[:-1])
    #TestA()
    SolveDay18A(lines)
    SolveDay18B(lines)

    print('End of day 18.')

def SolveDay18A(lines):
    print('Start of day 18 part A.')
    result = 0

    for line in lines:
        expressions = SplitLineIntoTokens(line)
        answer = SolveExpression(expressions)
        result += answer

    print(result)
    print('End of day 18 part A.')

def SolveDay18B(lines):
    print('Start of day 18 part B.')
    result = 0

    for line in lines:
        expressions = SplitLineIntoTokens(line)
        answer = SolveExpressionWithDifferentPrecedence(expressions)
        result += answer

    print(result)
    print('End of day 18 part B.')

def SplitLineIntoTokens(line):
    result = []
    value = ""

    for token in line:
        if token == ' ':
            if value != "":
                result.append(value)
            value = ""
        elif token == '(' or token == '*' or token == '+':
            result.append(token)
            value = ""
        elif token == ')':
            if value != "":
                result.append(value)
                value = ""
            result.append(token)
        else:
            value += token
    
    if value != "":
        result.append(value)

    return result

def SolveExpression(expressions):
    if '(' not in expressions:
        result = Solve(expressions)
        return result

    queue = []
    index = 0
    expressionsLength = len(expressions)
    buildQueue = []
    biggerQueue = []

    while index < len(expressions):
        currentToken = expressions[index]
        if currentToken == '(':
            parenthesisCounter = 1
            buildQueue.append(currentToken)
            index += 1

            while parenthesisCounter > 0:
                nextToken = expressions[index]

                if '(' == nextToken:
                    parenthesisCounter += 1
                    buildQueue.append(nextToken)
                elif ')' == nextToken:
                    parenthesisCounter -= 1
                    indexOfOpenParenthesis = len(buildQueue) - buildQueue[::-1].index('(') - 1
                    result = Solve(buildQueue[indexOfOpenParenthesis + 1:])
                    buildQueue = buildQueue[:indexOfOpenParenthesis]
                    buildQueue.append(result)
                else:
                    buildQueue.append(nextToken)

                index += 1
        else:
            buildQueue.append(currentToken)
            index += 1

    result = Solve(buildQueue)
    return result

def Solve(expression):
    if '(' in expression or ')' in expression:
        print('something went horribly wrong.', expression)

    queue = []
    index = 0

    while index < len(expression):
        if len(queue) > 0:
            firstValue = queue.pop()
            operator = expression[index]
            secondValue = expression[index + 1]
            index += 2
        else:
            firstValue = expression[index]
            operator = expression[index + 1]
            secondValue = expression[index + 2]
            index += 3
        
        if operator == '+':
            result = int(firstValue) + int(secondValue)
        elif operator == '*':
            result = int(firstValue) * int(secondValue)

        queue.append(result)

    result = queue.pop()
    if len(queue) > 0:
        print('Why is this not zero?', queue)

    return result

def SolveExpressionWithDifferentPrecedence(expressions):
    if '(' not in expressions:
        result = SolveWithDifferentPrecedence(expressions)
        return result

    queue = []
    index = 0
    expressionsLength = len(expressions)
    buildQueue = []
    biggerQueue = []

    while index < len(expressions):
        currentToken = expressions[index]
        if currentToken == '(':
            parenthesisCounter = 1
            buildQueue.append(currentToken)
            index += 1

            while parenthesisCounter > 0:
                nextToken = expressions[index]

                if '(' == nextToken:
                    parenthesisCounter += 1
                    buildQueue.append(nextToken)
                elif ')' == nextToken:
                    parenthesisCounter -= 1
                    indexOfOpenParenthesis = len(buildQueue) - buildQueue[::-1].index('(') - 1
                    result = SolveWithDifferentPrecedence(buildQueue[indexOfOpenParenthesis + 1:])
                    buildQueue = buildQueue[:indexOfOpenParenthesis]
                    buildQueue.append(result)
                else:
                    buildQueue.append(nextToken)

                index += 1
        else:
            buildQueue.append(currentToken)
            index += 1

    result = SolveWithDifferentPrecedence(buildQueue)
    return result

def SolveWithDifferentPrecedence(expression):
    queue = []
    index = 0

    while index < len(expression):
        token = expression[index]

        if token == '+':
            firstValue = expression[index - 1]
            secondValue = expression[index + 1]
            result = int(firstValue) + int(secondValue)
            expression = expression[:index - 1] + [result] + expression[index + 2:]
        else:
            index += 1
    
    index = 0
    while index < len(expression):
        token = expression[index]

        if token == '*':
            firstValue = expression[index - 1]
            secondValue = expression[index + 1]
            result = int(firstValue) * int(secondValue)
            expression = expression[:index - 1] + [result] + expression[index + 2:]
        else:
            index += 1

    result = expression[0]
    return result

def TestA():
    result = SolveExpression(['5', '+', '5', '*', '6'])
    print(result, 60)
    result = SolveExpression(['2', '*', '3', '+', '4', '*', '1'])
    print(result, 10)
    result = SolveExpression(SplitLineIntoTokens('1 + 2 * 3 + 4 * 5 + 6'))
    print(result, 71)
    result = SolveExpression(SplitLineIntoTokens('(1 + 2) * (2 * 3 + 4)'))
    print(result, 30)
    result = SolveExpression(['1', '+', '(', '2', '*', '3', ')', '+', '(', '4', '*', '(', '5', '+', '6', ')', ')'])
    print(result, 51)
    result = SolveExpression(SplitLineIntoTokens('2 * 3 + (4 * 5)'))
    print(result, 26)
    result = SolveExpression(SplitLineIntoTokens('5 + (8 * 3 + 9 + 3 * 4 * 3)'))
    print(result, 437)
    result = SolveExpression(SplitLineIntoTokens('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'))
    print(result, 12240)
    result = SolveExpression(SplitLineIntoTokens('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'))
    print(result, 13632)
    result = SolveExpression(SplitLineIntoTokens('(8 + (6 + 8 + 2 + 9 * 6 * 7) + 2) * 8 + 6 * (3 + 5) + 2'))
    print(result, 67890)
    anotherExample = '9 + 6 + 5 + (2 * (7 + 3) + (3 * 8) * 8 * 8 * 4) + 9'
    print(anotherExample)
    result = SolveExpression(SplitLineIntoTokens(anotherExample))
    print(result, 11293)
    
