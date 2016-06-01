def isAnagram1(firstWord, secondWord):
    secondWordList = list(secondWord)
    
    pos1 = 0
    stillOk = True
    
    while pos1 < len(firstWord) and stillOk:
        pos2 = 0
        found = False
        while pos2 < len(secondWordList) and not found:
            if firstWord[pos1] == secondWordList[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        if found:
            secondWordList[pos2] = None
        else: 
            stillOk = False
        pos1 = pos1 + 1
    return stillOk
        
print(isAnagram1("python", "typhon"))

def isAnagram2(firstWord, secondWord):
    firstWordList = list(firstWord)
    secondWordList = list(secondWord)
    firstWordList.sort()
    secondWordList.sort()
    i = 0
    while i < len(firstWord):
        if firstWordList[i] == secondWordList[i]:
            i+=1
        else:
            return False
    return True

print(isAnagram2("python", "typhon"))

def isAnagram3(firstWord, secondWord):
    if(len(firstWord) != len(secondWord)):
        return False
    else:
        pos = 0
        c1 = [0]*26
        c2 = [0]*26
        while pos < len(firstWord):
            bumpPos = ord(firstWord[pos]) - ord('a')
            c1[bumpPos] = c1[bumpPos] + 1
            bumpPos = ord(secondWord[pos]) - ord('a')
            c2[bumpPos] = c2[bumpPos] + 1
            pos +=1
        return c1 == c2

print(isAnagram3("python", "typhon"))
