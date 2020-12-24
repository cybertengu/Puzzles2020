import re

def SolveDay16(filepath):
    lines = []
    with open(filepath, 'r') as file:
        for line in file:
            if line == '\n':
                lines.append(line)
            else:
                lines.append(line[:-1])

    SolveDay16A(lines)
    SolveDay16B(lines)

    print('End of day 16.')

def SolveDay16A(lines):
    print('Start of day 16 part 1.')
    validDatas = []
    myTicket = []
    nearbyTickets = []
    newLineCounter = 0

    for line in lines:
        if line == '\n':
            newLineCounter += 1
        elif newLineCounter == 2:
            if 'nearby tickets:' in line:
                continue
            nearbyTickets.append(line)
        elif newLineCounter == 1:
            if 'your ticket:' in line:
                continue
            myTicket.append(line)
        else:
            tokens = line.split(': ')
            ranges = tokens[1].split(' or ')
            values = ranges[0].split('-') + ranges[1].split('-')
            validDatas += values
    
    validDataSize = len(validDatas)
    invalidNumber = {}
    validNumber = {}
    ticketScanningErrorRate = []

    for nearbyTicket in nearbyTickets:
        tokens = nearbyTicket.split(',')

        for number in tokens:
            if number in invalidNumber:
                ticketScanningErrorRate.append(int(number))
            elif number in validNumber:
                continue
            else:
                index = 0
                wasNumberValid = False

                while index < validDataSize:
                    if int(number) >= int(validDatas[index]) and int(number) <= int(validDatas[index + 1]):
                        validNumber[number] = 0
                        wasNumberValid = True
                        break
                    index += 2

                if not wasNumberValid:
                    invalidNumber[number] = 0
                    ticketScanningErrorRate.append(int(number))

    result = sum(ticketScanningErrorRate)
    print(result)
    print('End of day 16 part 1.')

def SolveDay16B(lines):
    with open("day16.txt") as f:
        notes = f.read().strip()

    fields = []
    nearbyTickets = []
    isYourTicket = False
    isNearbyTicket = False

    for line in lines:
        if line.isspace():
            continue 
        elif 'your ticket' in line:
            isYourTicket = True
        elif isYourTicket:
            myTicket = list(map(int, line.split(',')))
            isYourTicket = False
        elif 'nearby tickets' in line:
            isNearbyTicket = True
        elif isNearbyTicket:
            nearbyTickets.append(list(map(int, line.split(','))))
        else:
            tokens = line.split(':')
            combo = tokens[1].split(' or ')
            leftNumbers = combo[0].split('-')
            rightNumbers = combo[1].split('-')
            fields.append((tokens[0], int(leftNumbers[0]), int(leftNumbers[1]), int(rightNumbers[0]), int(rightNumbers[1])))
    
    validTickets = []
    for ticket in nearbyTickets:
        for value in ticket:
            isValid = False
            for fieldName, a, b, c, d in fields:
                if a <= value <= b or c <= value <= d:
                    isValid = True
                    break
            
            if not isValid:
                break
        
        if isValid:
            validTickets.append(ticket)
    
    product = 1
    fieldSize = len(fields)
    columns = set(range(fieldSize))
    
    for _ in range(fieldSize):
        for index, (fieldName, a, b, c, d) in enumerate(fields):
            candidates = []
            for column in columns:
                isTicketValid = True
                for ticket in validTickets:
                    if not (a <= ticket[column] <= b or c <= ticket[column] <= d):
                        isTicketValid = False
                        break
                
                if isTicketValid:
                    candidates.append(column)
            
            if len(candidates) == 1:
                columns.remove(candidates[0])
                fields = fields[:index] + fields[index + 1:]
                return

                if fieldName.startswith("departure"):
                    product *= myTicket[candidates[0]]
                break

    print(product)
    print('End of day 16 part 2.')
