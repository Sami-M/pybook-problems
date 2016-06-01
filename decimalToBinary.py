from implementingAStack import Stack

def decimalToBinary(decimal):
    s = Stack()
    while decimal != 0:
        s.push(decimal % 2)
        decimal = decimal // 2
    binary = ""
    while not s.isEmpty():
        binary += str(s.pop())
    return binary

print(decimalToBinary(42))