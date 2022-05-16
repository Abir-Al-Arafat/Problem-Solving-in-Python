# The substitution cipher is a simple way of encrypting a message, where each "a" is replaced with a certain letter, say "f", each b is replaced with a certain letter, say i. The key for the cipher is a string indicating the replacements. For instance, fiepltdkjbsuywqxanczrmvhg says that each a is replaces with f, each b is replaced with i, each c is replaced with e, etc. We can generate a key by shuffling the letters of the alphabet. Then given a word, we can encode it with the substitution cipher using dictionary whose keys are the letters of the alphabet and whose values are the letters they are mapped to in the key.
# A similar, but reversed, dictionary can be used for decryption.
# Write program that generates and prints a random key and uses that key to create a dictionary like the one described above. Then ask the user for a lowercase word. Encrypt and then decrypt that word using the substitution cipher dictionary and print out the encrypted and decrypted result.
# Expected Output: Decrypted word would be different for the same word
# Encrypted: ktxxw
# Decrypted: Hello

# importing shuffle function in order to shuffle characters
from random import shuffle

# declaring a variable containing alphabets as a string
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# converting the variable to list
alphabetList = list(alphabet)

# shuffling the elements of the list
shuffle(alphabetList)

# keeping the shuffled alphabets in a variable
alphabetShuffled = "".join(alphabetList)

# declaring empty dictionaries to keep encrypted and decrypted values

encrypt = {}
decrypt = {}

for index in range(len(alphabet)):
    # making a dictionary to encrypt strings
    encrypt[alphabet[index]] = alphabetShuffled[index]
    # making a dictionary to decrypt strings
    decrypt[alphabetShuffled[index]] = alphabet[index]

print("Encrypted: ", encrypt)
print("Decrypted: ", decrypt)

# asking user to give an input to encrypt
enc = input("encrypt: ")

# declaring an empty string
en = ""

# running a for loop on the input
for char in enc:
    en += encrypt[char]  # adding each character to the empty string to encrypt
print("enc", en)  # printing the encrypted string

# asking user to give an input to decrypt
dec = input("decrypt: ")
# declaring an empty string
de = ""
# running a for loop on the input
for char in dec:
    de += decrypt[char]  # adding each character to the empty string to decrypt
print("dec", de)  # printing the decrypted string
