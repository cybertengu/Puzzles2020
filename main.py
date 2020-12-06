import re

#filePath = "test.txt"
filePath = "input.txt"
dictionary = {}
validPassportCounter = 0
validPassportWithValidDataCounter = 0
birthYear = "byr"
issueYear = "iyr"
expirationYear = "eyr"
height = "hgt"
hairColor = "hcl"
eyeColor = "ecl"
passportId = "pid"
countryId = "cid"

with open(filePath) as file:
    for line in file:
        #print(line)
        if not line.isspace():
            #print(line[:-1])
            keypairs = re.split(r'[: ]', line[:-1])
            #print(keypairs)
            keypairsSize = len(keypairs)
            index = 0
            while index < keypairsSize:
                #print(type(keypairs))
                #print(keypairsSize)
                #print(keypairs[index], ":", keypairs[index + 1])
                dictionary[keypairs[index]] = keypairs[index + 1]
                index += 2
            #print(dictionary)
        else:
            #print(line[:-1])
            #print("Result: ", birthYear in dictionary, ' ', issueYear in dictionary, ' ', expirationYear in dictionary, ' ', height in dictionary, ' ', hairColor in dictionary, ' ', eyeColor in dictionary, ' ', passportId in dictionary, ' ', countryId in dictionary)
            if (birthYear in dictionary and 
                issueYear in dictionary and 
                expirationYear in dictionary and 
                height in dictionary and 
                hairColor in dictionary and 
                eyeColor in dictionary and 
                passportId in dictionary):
                #print("dictionary: ", dictionary)
                validPassportCounter += 1

                birthYearValue = int(dictionary[birthYear])
                issueYearValue = int(dictionary[issueYear])
                expirationYearValue = int(dictionary[expirationYear])
                heightValue = dictionary[height]
                hairColorValue = dictionary[hairColor]
                eyeColorValue = dictionary[eyeColor]
                passportIdValue = dictionary[passportId]

                numberStr = ''
                isHeightValid = False
                number = 0
                #print(heightValue)
                for currentCharacter in heightValue:
                    if currentCharacter == 'i':
                        number = int(numberStr)
                        isHeightValid = (number >= 59 and number <= 76)
                        break
                    elif currentCharacter == 'c':
                        number = int(numberStr)
                        isHeightValid = (number >= 150 and number <= 193)
                        break
                    else:
                        numberStr = numberStr + currentCharacter
                
                #print(heightValue, ' ', numberStr, ' ', isHeightValid)
                #print((birthYearValue >= 1920 and birthYearValue <= 2002), ' ', (issueYearValue >= 2010 and issueYearValue <= 2020), ' ', (expirationYearValue >= 2020 and expirationYearValue <= 2030), ' ', (isHeightValid), ' ', (re.fullmatch('#[0-9a-f]{6}', hairColorValue)), ' ', (re.fullmatch('(amb|blu|brn|gry|grn|hzl|oth){1}', eyeColorValue)), ' ', (re.fullmatch('[0-9]{9}', passportIdValue)))
                
                if ((birthYearValue >= 1920 and birthYearValue <= 2002) and
                    (issueYearValue >= 2010 and issueYearValue <= 2020) and
                    (expirationYearValue >= 2020 and expirationYearValue <= 2030) and
                    (isHeightValid) and
                    (re.fullmatch('#[0-9a-f]{6}', hairColorValue)) and
                    (re.fullmatch('(amb|blu|brn|gry|grn|hzl|oth){1}', eyeColorValue)) and
                    (re.fullmatch('[0-9]{9}', passportIdValue))):
                    validPassportWithValidDataCounter += 1
                    #print("entered")
            #print(validPassportCounter)
            #print('\n')
            dictionary.clear()
            #print("Should be empty: ", dictionary)

print(validPassportCounter)
print(validPassportWithValidDataCounter)
print("End of part one of day 4.")