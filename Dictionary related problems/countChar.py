# Count the each character in message and return as dictionary output like in expected output.
# Input:
# message = 'It was a bright sunday in May, and we needed to stay at home due to quarantine.'
# "Expected Output:
# "{'I': 1, 't': 7, ' ': 17, 'w': 2, 'a': 9, 's': 3, 'b': 1, 'r': 2, 'i': 3, 'g': 1, 'h': 2, 'c': 1, 'o': 4, 'l': 1, 'd': 5, 'y': 3, 'n': 5, 'M': 1, ',': 1, 'e': 6, 'm': 1, 'u': 2, 'q': 1, '.': 1}"

#method - 1
message = 'It was a bright sunday in May, and we needed to stay at home due to quarantine.'

count = {}

for char in message:
    if char not in count.keys():
        count[char] = 1
    else:
        count[char] += 1

print(count)

#method - 2

message = 'It was a bright sunday in May, and we needed to stay at home due to quarantine.'

count = {}  # Declaring an empty dictionary

# looping through all the characters of the string
for character in message:
    count.setdefault(character, 0)  # setting the default character to 0

    # adding 1 for each character
    count[character] = count[character] + 1

print(count)
