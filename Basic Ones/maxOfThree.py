# Write a Python function which returns the Max of three numbers

def maxOfThree(one, two, three):
    if one > two and one > three:
        return one
    elif two > one and two > three:
        return two
    else:
        return three


print(maxOfThree(400, 440, 350))
