# Use lambda and filter function to filter out vowels from the list below.
# Input:
# alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# vowels = ['a', 'e', 'i', 'o', 'u']
# Output:
# ['a', 'e', 'i']

# declaring a list of alphabets
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# declaring a list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# using filter function to filter out the vowels
filteredVowels = filter(lambda vowel: vowel in vowels, alphabets)

print(list(filteredVowels))
