# reverse a string using stack

def reverseString(string):
    reversedString = ""
    stringStack = []

    for char in string:
        stringStack.append(char)

    for _ in range(len(stringStack)):
        reversedString += stringStack.pop()
    
    return reversedString

print(reverseString("Hello"))