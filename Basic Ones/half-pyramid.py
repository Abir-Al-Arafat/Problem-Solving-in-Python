# write a program to generate random 0s(zeroes) and 1s(ones) where the first line generates one random 0 or 1 and with each line, a random number also increases. generate 10 lines. the output should look like the right side of a pyramid

from random import randint

for i in range(1, 11):
    for j in range(i):
        print(randint(0, 1), end=" ")
    print()
