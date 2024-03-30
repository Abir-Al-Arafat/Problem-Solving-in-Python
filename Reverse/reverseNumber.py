# reverse a number

def reverseNumber(number):
    divident = 10
    reversedNumber = 0

    while number > 0:
        lastNumber = number % divident
        reversedNumber = (reversedNumber * 10) + lastNumber
        number = number//divident
    
    return reversedNumber

print(reverseNumber(12345))