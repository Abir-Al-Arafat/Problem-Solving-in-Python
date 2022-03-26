# Write a program that creates and prints a list of 50 random numbers from 1 to 5 with the property that the same number never appears one after another. [Hint: One way to do this is to use a while loop to make sure the current number being generated is not equal to the previous number.]

from random import randint

result = [randint(1, 5)]

for i in range(49):
    number = randint(1, 5)
    # checking if the previous number is as same as the next one
    while number == result[i]:
        # assign another number if prev and next numbers are same
        number = randint(1, 5)
    result.append(number)

print(result)
