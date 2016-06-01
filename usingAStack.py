from implementingAStack import Stack

s = Stack()

s.push(1)
s.push(2)
s.push(3)
print(s.peek())
print(s.size())
print(s.isEmpty())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.isEmpty())

def reverseString(stringToReverse):
    s = Stack()
    for letter in stringToReverse:
        s.push(letter)
    reversedString=""
    while not s.isEmpty():
        reversedString += s.pop()
    return reversedString

print(reverseString("alphabet"))
    