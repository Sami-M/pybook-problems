from implementingAStack import Stack

def baseConverter(decimal, base):
    s = Stack()
    while decimal != 0:
        s.push(decimal % base)
        decimal = decimal // base
    basedNumber = ""
    while not s.isEmpty():
        basedNumber += str(s.pop())
    return basedNumber

print baseConverter(25, 2)
print baseConverter(25, 16)
print baseConverter(25, 8)
print baseConverter(256, 16)
print baseConverter(26, 26)