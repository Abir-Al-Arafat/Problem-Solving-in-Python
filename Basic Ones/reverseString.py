# Write a function to reverse a string. For example, user enters 'how' and the output is 'woh'.

def revStr(string):
    index = len(string)  # keeping the length of the string as an index
    reverse = ""  # initializing an empty string
    while index > 0:  # running a while loop
        reverse += string[index-1]  # adding the character in reversed order
        index -= 1  # subtracting 1 from the index
    return reverse  # returning the reversed string


print(revStr("hey"))

# -----------------------------------------------------------------------------------------
# another method

string = "hey"
print(string[::-1])
