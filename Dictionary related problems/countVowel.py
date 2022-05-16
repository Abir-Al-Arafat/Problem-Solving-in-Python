# Write a program that repeatedly asks the user to enter a word and create a dictionary whose keys are those words and whose values are counts of how many vowels are in the words. The user indicates. they are done by pressing enter without entering anything (the input will therefore be an empty string). Print out the dictionary after it is done being created."

# method-1
countVowel = {}
while True:
    word = input("Enter a word (press enter to quit): ")
    if word == "":
        break
    else:
        countVowel[word] = 0  # initializing the value of the word to zero
        # looping over the word for characters
        for char in word:
            if char in 'aeiou':  # checking if the character is vowel
                countVowel[word] += 1  # adding one if vowel found


print("Method-1: ", countVowel)
print()
# method-2
countVowel = {}
while True:
    word = input("Enter a word (press enter to quit): ")
    if word == "":  # if user press enter, break the loop
        break
    else:
        # adding sum of vowels as values of the words
        countVowel[word] = sum(word.count(char) for char in 'aeiou')

print("Method-2: ", countVowel)
