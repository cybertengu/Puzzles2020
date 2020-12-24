def SolveDay7(filePath):
    SolveDay7A(filePath)
    SolveDay7B(filePath)
    print('End of day 7.')

def SolveDay7A(filePath):
    bags = {}
    expectedBag = 'shiny gold bag'
    validBagColors = set()

    with open(filePath, 'r') as file:
        for line in file:
            if line == '\n':
                break

            keypair = line.split('contain')
            key = keypair[0][:-1]
            
            if ',' in keypair[1]:
                pairs = keypair[1].split(',')
            else:
                pairs = [keypair[1][1:-2]]
            
            pairSize = len(pairs)
            
            if pairSize != 1:
                pairs = [x.strip() for x in pairs]                    
                pairs[pairSize - 1] = pairs[pairSize - 1][:-1]
            
            bags[key] = pairs

            if any(expectedBag in singleBag for singleBag in pairs):
                colorBag = key[:-1]
                validBagColors.add(colorBag)

    validBagsSize = 0
    
    while validBagsSize != len(validBagColors):
        validBagsSize = len(validBagColors)
        currentValidBagColors = validBagColors.copy()
        
        for aBag in currentValidBagColors:
            for key, value in bags.items():
                for singleBag in value:
                    if aBag in singleBag:
                        colorBag = key[:-1]
                        validBagColors.add(colorBag)

    print(validBagsSize)
    print('End of part A of day 7.')

def SolveDay7B(filePath):
    bags = {}

    with open(filePath, 'r') as file:
        for line in file:
            if line == '\n':
                break
            keypair = line.split('contain')
            key = keypair[0][:-1]
            if ',' in keypair[1]:
                pairs = keypair[1].split(',')
            else:
                pairs = [keypair[1][1:-2]]
            pairSize = len(pairs)
            if pairSize != 1:
                pairs = [x.strip() for x in pairs]                    
                pairs[pairSize - 1] = pairs[pairSize - 1][:-1]
            bags[key] = pairs
   
    expectedBag = 'shiny gold bags'
    queue = []

    values = bags[expectedBag]
    equation = []

    for value in values:
        info = value.split(' ')
        number = int(info[0])
        
        if info[len(info) - 1] == 'bag':
            info[len(info) - 1] = 'bags'

        bagColor = ' '.join(info[1:])
        
        singleBag = Bag(bagColor, number, 0)
        queue.append(singleBag)

    queueSize = len(queue)
    depth = 0

    while len(queue) > 0:
        offQueue = queue.pop()
        values = bags[offQueue.colorName]
        queueSize -= 1
        depth = offQueue.depth + 1
        equation.append(offQueue)

        for value in values:
            if 'no other bags' == value:
                continue

            info = value.split(' ')
            number = int(info[0])
            
            if info[len(info) - 1] == 'bag':
                info[len(info) - 1] = 'bags'

            bagColor = ' '.join(info[1:])
            
            singleBag = Bag(bagColor, number, depth)
            queue.append(singleBag)
            queueSize += 1

    result = 0
    solve = []
    stack = []
    
    equation.reverse()
    queue.clear()

    for aBag in equation:
        colorName = aBag.colorName
        amount = aBag.amount
        depth = aBag.depth

        if len(queue) == 0:
            queue.append(aBag)
            continue
        
        priorBag = queue.pop()

        if priorBag.depth == aBag.depth:
            aBag.amount = amount + priorBag.amount
        elif priorBag.depth > depth:
            aBag.amount = amount + amount * priorBag.amount

            if len(queue) > 0:
                anotherBag = queue.pop()
                wasQueueEmpty = False

                while anotherBag.depth == aBag.depth:
                    aBag.amount += anotherBag.amount
                
                    if len(queue) == 0:
                        wasQueueEmpty = True
                        break

                    anotherBag = queue.pop()
                
                if not wasQueueEmpty:
                    queue.append(anotherBag)
        else:
            queue.append(priorBag)

        queue.append(aBag)

    amountOfBagsInside = queue[0].amount
    print(amountOfBagsInside)
    print('End of part B of day 7.')

class Bag:
    def __init__(self, colorName, amount, depth):
        self.colorName = colorName
        self.amount = amount
        self.depth = depth

def GetTotalBagCount(bags, bagName, amount):
    #print(bags[bagName])
    currentBag = bags[bagName][0]
    #print(currentBag)

    if 'no other bags' == currentBag:
        print("Did this run?")
        return 0

    print(bags[bagName])
    
    currentAmount = 0
    for value in bags[bagName]:
        print(value)
        info = value.split(' ')
        number = int(info[0])
        #print(number)
       
        print(info)

        if info[len(info) - 1] == 'bag':
            #print("Does this run?")
            info[len(info) - 1] = 'bags'

        bagName = ' '.join(info[1:])
        print(number, ' ', bagName)

        amount.append(number + number * GetTotalBagCount(bags, bagName, amount))
        print('Run? ', amount)

    return amount[0]
