from parseFile import ParseFile

def SolveDay4(filePath):
    SolveDay4A(filePath)
    SolveDay4B(filePath)
    print("End of day 4.")

def SolveDay4A(filePath):
#    byr (Birth Year)
#    iyr (Issue Year)
#    eyr (Expiration Year)
#    hgt (Height)
#    hcl (Hair Color)
#    ecl (Eye Color)
#    pid (Passport ID)
#    cid (Country ID)
    birthYear = "byr"
    issueYear = "iyr"
    expirationYear = "eyr"
    height = "hgt"
    hairColor = "hcl"
    eyeColor = "ecl"
    passportId = "pid"
    countryId = "cid"
    validPassportCounter = 0
    result = []

    with open(filePath, 'r') as file:
        for line in file:
            print("Old Result: ", result)
            print("Current Line: ", line)
            if line == '\n':
                print("Result 1: ", birthYear in result)
                print("Result 2: ", issueYear in result)
                print("Result 3: ", expirationYear in result)
                print("Result 4: ", height in result)
                print("Result 5: ", hairColor in result)
                print("Result 6: ", eyeColor in result)
                print("Result 7: ", passportId in result)
                print("Result 8: ", passportId in result)
                if (birthYear in result and 
                    issueYear in result and 
                    expirationYear in result and
                    height in result and
                    hairColor in result and
                    eyeColor in result and 
                    (passportId in result or countryId in result)):
                    validPassportCounter += 1
                result.clear()
                print("Did result get cleared? ", result)

            else:
                keypairs = re.split(': ', line)
                data = str.rsplit(line)
                result.append(data)
                print("New Result: ", result)
            
    print(validPassportCounter)

    print("End of day 4 A.")

def SolveDay4B(filePath):

    print("End of day 4 B.")
