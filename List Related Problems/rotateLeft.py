# Write a program that rotates all the elements in a list one element to the left, with the first element rotating to the end. For instance, if the list is [1,2,3,4], it would rotate into [2,3,4,1].

inp = [1, 2, 3, 4, 5, 6, 7, 8]

# declaring an empty list
output = []

# running a for loop
for i in range(len(inp)):
    if i < len(inp)-1:  # checking condition to move the elements to one step left
        output.append(inp[i+1])  # placing the elements
    if i == len(inp)-1:  # checking condition to move the first element to last
        output.append(inp[0])  # adding the element to last index

print(output)
