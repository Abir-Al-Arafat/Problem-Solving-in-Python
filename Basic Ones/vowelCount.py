# create a functions which takes an input and returns the number of vowels in a sentence, consider uppercase lowercase scenario

def countVowel(sentence):
    vowel = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in sentence:
        if char.lower() in vowel:
            count += 1
    return count


print(countVowel('APPLE'))
