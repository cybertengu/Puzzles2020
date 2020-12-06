def ParseFile(filePath):
    lines = []
    with open(filePath, 'r') as file:
        for line in file:
            removeNewline = str.rsplit(line)
            lines.append(removeNewline[0])
 
    return lines

def ParseFileByLine(filePath):
    lines = []
    with open(filePath, 'r') as file:
        for line in file:
            if line == '\n':
                continue
            result = line[:-1]
            lines.append(result)
    
    return lines
