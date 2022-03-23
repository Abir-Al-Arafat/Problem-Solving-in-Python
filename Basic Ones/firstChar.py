# write a function which takes a sentence as an input. the sentence will consist of multiple words. The function will return the first letter of each word, all on the same line. example: input = 'The weather is so nice'. output = Twisn

inp = input("Write a sentence: ")  # taking input from the user


def firstChar(inp):  # declaring a function
    result = inp[0]  # keeping the value of first index inside a variable
    for i in range(len(inp)):  # running a for loop
        if inp[i] == " ":  # checking if the sentence has a space
            result += inp[i+1]  # adding the first letter in the empty variable

    return result  # returning the variable


print(firstChar(inp))

# implementing another approach


def firstChar2(inp):
    # using split function to keep the words of the sentence inside the variable as a list
    result = inp.split()

    output = []  # declaring an empty list
    for index in range(len(result)):  # running a for loop
        # appending the first character of each word
        output.append(result[index][0])
    return " ".join(output)  # returning the output


print(firstChar2(inp))
