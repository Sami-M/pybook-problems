from implementingAStack import Stack

def bracketChecker(stringToCheck):
    s = Stack()
    pos = 0
    while pos < len(stringToCheck):
        if(stringToCheck[pos] in "({[<"):
            s.push(stringToCheck[pos])
        else:
            if(s.isEmpty()):
                return False
            else:
                if(matches(s.peek(), stringToCheck[pos])):
                    s.pop()
                else:
                    return False
        pos += 1
    if(s.isEmpty()):
        return True
    else:
        return False
    
def matches(left, right):
    open = ['(','{','[','<']
    close = [')','}',']','>']
    return open.index(left) == close.index(right)

print(bracketChecker("(){{}}[]<>"))