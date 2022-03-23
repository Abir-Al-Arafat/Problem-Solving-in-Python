# Write a program that remove the items of given indices from the list. The list of indexes are as follows: [2,4]. Then create a new list that consists of all the strings from the user’s list except for those at the indices from the list of indices. For instance, if the list of strings is ['a','bc','d','e','fg'] and the list of indices is[2,4], then the new list would be ['a','bc','e']. L= ['a','bc','d','e','fg'] I = [4,2]

inp = ['a', 'bc', 'd', 'e', 'fg']  # list of strings
index = [2, 4]  # list of indices whose elements need to be removed
j = 0  # initializing to 0 number index
out = []  # initializing an empty list

# running a for loop in the string
for i in range(len(inp)):
    # running a while loop in the index list
    while(j < len(index)):
        # appending value not according to the given index
        if(i != index[j]):
            out.append(inp[i])
            break
        # going to the next index
        else:
            j += 1
            break

print(out)
