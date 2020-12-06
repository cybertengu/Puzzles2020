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
            if line == '\n':
                if (birthYear in result and 
                    issueYear in result and 
                    expirationYear in result and
                    height in result and
                    hairColor in result and
                    eyeColor in result and 
                    (passportId in result or countryId in result)):
                    validPassportCounter += 1
                result.clear()
            else:
                keypairs = re.split(': ', line)
                data = str.rsplit(line)
                result.append(data)
            
    print(validPassportCounter)

    print("End of day 4 A.")

def SolveDay4B(filePath):

    print("End of day 4 B.")
