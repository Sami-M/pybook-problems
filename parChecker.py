from implementingAStack import Stack

def parChecker(stringToCheck):
    s = Stack()
    i = 0
    while i < len(stringToCheck):
        if(stringToCheck[i] == "("):
            s.push(stringToCheck[i])
        else:
            s.pop()
        i += 1
    if(s.isEmpty()):
        return True
    else:
        return False
    
print(parChecker("()((()"))
print(parChecker("()(()())"))