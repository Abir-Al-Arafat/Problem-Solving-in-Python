# "Create a dictionary whose keys are the strings 'abc', 'def', 'ghi', 'jkl', and 'mno' and whose corresponding values are 7, 11, 13, 17, and 19. Then write dictionary code that does the following:\n",
# "(a) Print the value in the dictionary associated with the key 'def'.\n",
# "(b) Use the keys() method to print out all the keys.\n",
# "(c) Loop over the dictionary and print out all the keys and their associated values",
# "(d) Use an if statement to check if the dictionary contains the key 'pqr' and print out an appropriate message indicating whether it does or doesn’t
# (e) Change the value associated with the key 'abc' to 23 and then print out all the values in the dictionary using the values() method

# Dictionary given in problem
problem = {'abc': 7, 'def': 11, 'ghi': 13, 'jkl': 17, 'mno': 19}

# (a) Print the value in the dictionary associated with the key 'def'.
print(problem['def'])

# get() method is used to get the value of the key
print(problem.get('def'))
print(problem.get('pqr', 20))
print(problem)


# (b) Use the keys() method to print out all the keys
for key in problem.keys():
    print(key)
print(list(problem.keys()))

# (c) Loop over the dictionary and print out all the keys and their associated values

# method-1
for key in problem:
    print(key, problem[key])

# method-2
for key, value in problem.items():
    print(key, value)

# (d) Use an if statement to check if the dictionary contains the key 'pqr' and print out an appropriate message indicating whether it does or doesn’t

if 'pqr' in problem:
    print("yes")
else:
    print("no")

# (e) Change the value associated with the key 'abc' to 23 and then print out all the values in the dictionary using the values() method

problem['abc'] = 23

for value in problem.values():
    print(value)


# "Merge following two Python dictionaries into one dictionary. Add all the values into the result variable and print it out
#     "dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}",
#     "dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}",
#     "Expected Output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
#     "Result is 150"

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# unpacking the dictionary using aesterics and merging it into another dictionary
merged = {**dict1, **dict2}

print(merged)
result = 0
for key in merged:
    result += merged[key]

print(result)
