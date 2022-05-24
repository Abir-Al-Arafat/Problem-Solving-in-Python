# Write a function called concatStr() that takes a dictionary as an input and returns the concatenated values from the dictionary in string. Unpacking dictionaries is used. For example, user enters
# input = {'a':"Real", 'b':"Python", 'c':"Is", 'd':"Great", 'e':"!"}
# Output : RealPythonIsGreat!Heyo


# IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Using **kwargs provides us with the flexibility to use keyword arguments in our program. When we use **kwargs as a parameter, we don’t need to know how many arguments we would eventually like to pass to a function. Creating functions that accept **kwargs are best used in situations where you expect that the number of inputs within the argument list will remain relatively small.

def concatStr(**kwargs):
    con = ""
    for value in kwargs.values():
        con += value
    return con


input = {'a': "Real", 'b': "Python", 'c': "Is", 'd': "Great", 'e': "!"}

print(concatStr(**input))
print(concatStr(t="thank", y="you", s='so', m="much"))
