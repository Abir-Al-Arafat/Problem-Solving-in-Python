# Write a function that asks the user to enter a string, then replace all the spaces with asterisks and replace every fifth character (starting with index 0) with an exclamation point, and returns a new string. For example, this is a test would become: !his * !s * a * !est

string = input("Write a sentence: ")  # taking input from the user


def encrypt(string):  # declaring a function
    string = string.replace(" ", "*")  # replacing the spaces with aesterics
    output = ""  # declaring a new empty string variable
    for i in range(len(string)):  # for loop to go through every letter of the input
        if i % 5 == 0:  # checking if the loop reached the desired index
            output += "!"  # adding letter to the variable
        else:
            output += string[i]

    return output  # returning the desired output


print(encrypt(string))
