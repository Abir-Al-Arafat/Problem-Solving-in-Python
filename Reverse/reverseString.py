# reverse a string

def reverseString(string):
    reversedString = ""

    for char in string:
        reversedString = char + reversedString
    
    return reversedString

print(reverseString("Hello"))