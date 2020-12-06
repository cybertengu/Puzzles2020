def ParseFile(filePath):
    lines = []
    with open(filePath, 'r') as file:
        for line in file:
            #print(line)
            removeNewline = str.rsplit(line)
            #print(removeNewLine)
            lines.append(removeNewline[0])
            #print(lines)
 
    return lines

def ParseFileByLine(filePath):
    lines = []
    with open(filePath, 'r') as file:
        for line in file:
            if line == '\n':
                continue
            result = line[:-1]
            lines.append(result)
    
    #print(lines)
    return lines
