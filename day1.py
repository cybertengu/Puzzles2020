def TimesThreeValuesAfterThreeValuesMatchSum(expenses, sum):
    for index, currentExpense in enumerate(expenses[:-2]):
        innerSum = sum - currentExpense
        for innerIndex, innerExpense in enumerate(expenses[index:]):
            complementaryValue = innerSum - innerExpense
            if complementaryValue in expenses[innerIndex + 1:]:
                result = currentExpense * innerExpense * complementaryValue
                return result
    else:
        print("Could not find anything that added up to " + str(sum) + ".")
        return

def SolveDay1():
    expenses = []

    with open('day1A.txt', 'r') as file:
        for line in file:
            expenses.append(int(line))

    expectedSum = 2020

    for index, currentExpense in enumerate(expenses[:-1]):
        complementaryValue = expectedSum - currentExpense
        if complementaryValue in expenses[index + 1:]:
            result = currentExpense * complementaryValue
            print(result)
            break
    else:
        print("Could not find anything that added up to " + str(expectedSum) + " for the first section of Day 1 problem.")

    print('End of day 1 A.')

    result = TimesThreeValuesAfterThreeValuesMatchSum(expenses, expectedSum)
    print(result)

    print('End of day 1 B')
