# Write a function called genStr() that takes an integer parameter and returns a random string of that many lowercase letters.

from secrets import choice


def genStr(length):
    return "".join(choice('abcdefghijklmnopqrstuvwxyz') for index in range(length))


print(genStr(5))
