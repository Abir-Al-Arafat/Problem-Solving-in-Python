# Ask the user to enter a number then find all the prime factors for that number. 
# A prime factor is a prime number that can divide a number. 
# For example if you think about the number 35 it has two prime factors 5 and 7. Both five and seven are prime numbers and they can divide the number 35 similarly for the number 10 you will have two factors 2 & 5.

def primeFactors(number):
    primeFactors = []
    divisor = 2

    while number > 2:
        if number % divisor == 0:
            primeFactors.append(divisor)
            number = number/divisor
        else:
            divisor += 1

    return primeFactors

print(primeFactors(45))