# write a function which returns if a string is palindrome or not

def palString(string, leftIndex, rightIndex):
    if leftIndex >= rightIndex:  # checking if left  index surpasses right index or not
        return True
    # checking if the character from left index is not equal to right index character
    if string[leftIndex] != string[rightIndex]:
        return False
    # calling the function while increasing the left index and decreasing the right index
    return palString(string, leftIndex+1, rightIndex-1)


string = "racecarr"
rightIndex = len(string)-1

print(palString(string, 0, rightIndex))
