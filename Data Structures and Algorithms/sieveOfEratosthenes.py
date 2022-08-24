# write a function which a takes a limit and returns a list of prime numbers till that limit

def sieveOfEratosthenes(limit):
    # initializing list of numbers
    numbers = [number for number in range(limit+1)]

    numbers[0] = 0  # initializing 1st index to 0 because 0 is not prime
    numbers[1] = 0  # initializing 2nd index to 0 because 0 is not prime

    number = 2  # declaring a variable with number 2

    while number*number <= limit:
        if number != 0:
            for n in range(number*2, limit+1, number):
                # setting non prime numbers to 0
                numbers[n] = 0
        number += 1

    return numbers


print(sieveOfEratosthenes(25))
