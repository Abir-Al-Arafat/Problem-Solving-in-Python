#  Write a function which takes a string and returns the index of the alphabet characters. Then print out (all on the same line) the indices of the string that contain letters. For example: If the string is A B?*C, the program would output 0, 2, and 5 since these are the only letters at those indices.

# taking input from the user
string = input("Enter a string: ")

# declaring a function


def charIndex(string):
    # declaring an empty string
    indices = ""
    # running a for loop to get the indexes of the characters of the string
    for i in range(len(string)):
        if string[i].isalpha():  # checking if the value is an alphabet
            indices += str(i)  # adding the index which has an alphabet
    return indices  # returning the indices


print(charIndex(string))
