def SolveDay12(filePath):
    instructions = []

    with open(filePath, 'r') as file:
        for line in file:
            if line == '\n':
                continue
            result = line[:-1]
            instruction = NavigationInstruction(result[0], result[1:])
            instructions.append(instruction)
    
    SolveDay12PartA(instructions)
    SolveDay12PartB(instructions)

def SolveDay12PartA(instructions):
    ship = Ship('E')
    
    for instruction in instructions:
        action = instruction.action
        value = instruction.value

        if action == 'N':
            if ship.nsDirection == 'N':
                ship.nsPosition += int(value)
            elif ship.nsDirection == 'S':
                ship.nsPosition -= int(value)
                
                if ship.nsPosition < 0:
                    ship.nsPosition *= -1
                    ship.nsDirection = 'S'

        elif action == 'S':
            if ship.nsDirection == 'S':
                ship.nsPosition += int(value)
            elif ship.nsDirection == 'N':
                ship.nsPosition -= int(value)

            if ship.nsPosition < 0:
                ship.nsPosition *= -1
                ship.nsDirection = 'S'

        elif action == 'E':
            if ship.ewDirection == 'E':
                ship.ewPosition += int(value)
            elif ship.ewDirection == 'W':
                ship.ewPosition -= int(value)

                if ship.ewPosition < 0:
                    ship.ewPosition *= -1
                    ship.ewDirection = 'E'

        elif action == 'W':
            if ship.ewDirection == 'W':
                ship.ewPosition += int(value)
            elif ship.ewDirection == 'E':
                ship.ewPosition -= int(value)

                if ship.nsPosition < 0:
                    ship.ewPosition *= -1
                    ship.ewDirection = 'W'

        elif action == 'F':
            if ship.facingDirection == 'E':
                if ship.ewDirection == 'E':
                    ship.ewPosition += int(value)
                elif ship.ewDirection == 'W':
                    ship.ewPosition -= int(value)

                    if ship.ewPosition < 0:
                        ship.ewPosition *= -1
                        ship.ewDirection = 'E'

            elif ship.facingDirection == 'W':
                if ship.ewDirection == 'W':
                    ship.ewPosition += int(value)
                elif ship.ewDirection == 'E':
                    ship.ewPosition -= int(value)

                    if ship.ewPosition < 0:
                        ship.ewPosition *= -1
                        ship.ewDirection = 'W'

            elif ship.facingDirection == 'N':
                if ship.nsDirection == 'N':
                    ship.nsPosition += int(value)
                elif ship.nsDirection == 'S':
                    ship.nsPosition -= int(value)

                    if ship.nsPosition < 0:
                        ship.nsPosition *= -1
                        ship.nsDirection = 'N'

            elif ship.facingDirection == 'S':
                if ship.nsDirection == 'S':
                    ship.nsPosition += int(value)
                elif ship.nsDirection == 'N':
                    ship.nsPosition -= int(value)

                    if ship.nsPosition < 0:
                        ship.nsPosition *= -1
                        ship.nsDirection = 'S'

        elif action == 'L' or action == 'R':
            ship.facingDirection = NewDirectionFromRotation(ship.facingDirection, action, value)
        
    result = ship.nsPosition + ship.ewPosition
    print(result)
    print('End of day 12 part 1.')

def SolveDay12PartB(instructions):
    ship = Ship('E')
    waypoint = Waypoint('NE', [1, 10])

    for instruction in instructions:
        action = instruction.action
        value = instruction.value
        
        if action == 'F':
            amount = int(value)
            nsValue = amount * waypoint.units[0]
            ewValue = amount * waypoint.units[1]
            
            if ship.nsDirection == waypoint.directions[0]:
                ship.nsPosition += nsValue
            else:
                ship.nsPosition -= nsValue

                if ship.nsPosition < 0:
                    ship.nsPosition *= -1

                    if ship.nsDirection == 'N':
                        ship.nsDirection = 'S'
                    else:
                        ship.nsDirection = 'N'

            if ship.ewDirection == waypoint.directions[1]:
                ship.ewPosition += ewValue
            else:
                ship.ewPosition -= ewValue

                if ship.ewPosition < 0:
                    ship.ewPosition *= -1

                    if ship.ewDirection == 'E':
                        ship.ewDirection = 'W'
                    else:
                        ship.ewDirection = 'E'
        elif action == 'R' or action == 'L':
            waypoint = NewWaypointRotation(waypoint, action, value)
        else:
            waypoint = MoveWaypoint(action, value, waypoint)

    result = ship.nsPosition + ship.ewPosition
    print(result)
    print('End of day 12 part 2.')

# The parameter value is a string.
def MoveWaypoint(direction, value, waypoint):
    if direction == 'N':
        if waypoint.directions[0] == 'N':
            waypoint.units[0] += int(value)
        else:
            waypoint.units[0] -= int(value)

            if waypoint.units[0] < 0:
                waypoint.units[0] *= -1
                waypoint.directions = 'N' + waypoint.directions[1]

    elif direction == 'S':
        if waypoint.directions[0] == 'S':
            waypoint.units[0] += int(value)
        else:
            waypoint.units[0] -= int(value)

            if waypoint.units[0] < 0:
                waypoint.units[0] *= -1
                waypoint.directions = 'S' + waypoint.directions[1]

    elif direction == 'E':
        if waypoint.directions[1] == 'E':
            waypoint.units[1] += int(value)
        else:
            waypoint.units[1] -= int(value)

            if waypoint.units[1] < 0:
                waypoint.units[1] *= -1
                waypoint.directions = waypoint.directions[0] + 'E'

    elif direction == 'W':
        if waypoint.directions[1] == 'W':
            waypoint.units[1] += int(value)
        else:
            waypoint.units[1] -= int(value)

            if waypoint.units[1] < 0:
                waypoint.units[1] *= -1
                waypoint.directions = waypoint.directions[0] + 'W'

    return waypoint
# NE 1, 10 -> SE 10, 1 -> SW 1, 10

# The parameter amount is a string.
def NewWaypointRotation(waypoint, turnTo, amount):
    degree = int(amount)
    newDirections = waypoint.directions
    newUnits = [waypoint.units[0], waypoint.units[1]]
    
    while degree > 0:
        degree -= 90

        if turnTo == 'R':
            if newDirections == 'NE':
                newDirections = 'SE'
            elif newDirections == 'SE':
                newDirections = 'SW'
            elif newDirections == 'SW':
                newDirections = 'NW'
            elif newDirections == 'NW':
                newDirections = 'NE'

            tmpValue = newUnits[0]
            newUnits[0] = newUnits[1]
            newUnits[1] = tmpValue

        elif turnTo == 'L':
            if newDirections == 'NE':
                newDirections = 'NW'
            elif newDirections == 'SE':
                newDirections = 'NE'
            elif newDirections == 'SW':
                newDirections = 'SE'
            elif newDirections == 'NW':
                newDirections = 'SW'

            tmpValue = newUnits[0]
            newUnits[0] = newUnits[1]
            newUnits[1] = tmpValue

    newWaypoint = Waypoint(newDirections, newUnits)

    return newWaypoint

rotationLookup = {}

# Parameters are all assumed to be strings
def NewDirectionFromRotation(currentDirection, turnTo, degree):
    action = currentDirection + turnTo + degree
    
    if action in rotationLookup:
        return rotationLookup[action]

    value = int(degree)
    newDirection = currentDirection

    while value > 0:
        value -= 90

        if turnTo == 'L':
            if newDirection == 'N':
                newDirection = 'W'
            elif newDirection == 'W':
                newDirection = 'S'
            elif newDirection == 'S':
                newDirection = 'E'
            elif newDirection == 'E':
                newDirection = 'N'

        if turnTo == 'R':
            if newDirection == 'N':
                newDirection = 'E'
            elif newDirection == 'W':
                newDirection = 'N'
            elif newDirection == 'S':
                newDirection = 'W'
            elif newDirection == 'E':
                newDirection = 'S'
        
    rotationLookup[action] = newDirection
    return newDirection

# N S E W
# N 90 L -> E N 90 R -> W
# S 90 L -> W S 90 R -> E
# E 90 L -> N E 90 R -> S
# W 90 L -> S W 90 R -> N
# 90, 180, 270, 360

class NavigationInstruction:
    def __init__(self, action, value):
        self.action = action
        self.value = value

class Ship:
    def __init__(self, facingDirection):
        self.ewPosition = 0
        self.ewDirection = 'E' 
        self.nsPosition = 0
        self.nsDirection = 'N' 
        self.facingDirection = facingDirection

class Waypoint:
    def __init__(self, directions, units):
        self.directions = directions
        self.units = units

def PrintInstructions(instructions):
    for instruction in instructions:
        print(instruction.action, instruction.value)

def PrintShipDetails(ship):
    print('NS:', ship.nsDirection, ship.nsPosition, 'EW:', ship.ewDirection, ship.ewPosition, 'Facing Direction:', ship.facingDirection)
        
