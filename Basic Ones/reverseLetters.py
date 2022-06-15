# Write a function called reverse_only_letters() that takes a string and creates returns a new string where all the positions of all the letters have been reversed, but all other characters have been left in same position. For instance, if the argument is ab*c&&de then the returned string would be ed*c&&ba.

# declaring a function to reverse letters
def reverse_only_letters(string):

    # keeping the letters in a reversed order in a list
    reverse = [letter for letter in string[::-1] if letter.isalpha()]
    # declaring the index to 0
    index = 0
    # declaring an empty string
    result = ''
    # running a for loop
    for letter in string:
        # checking if the character is a letter
        if letter.isalpha():
            # adding the letter
            result += reverse[index]
            # increasing index
            index += 1
        else:
            # adding the non-letter
            result += letter
            # returning the result
    return result


string = "ab*c&&de"

print(reverse_only_letters(string))
