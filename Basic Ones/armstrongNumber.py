# check whether a number is an armstrong number

def isArmstrongNumber(number):
    power = len(str(number))
    originalNumber = number
    compareNumber = 0

    while number>0:
        compareNumber += (number%10)**power
        number //= 10
    
    return originalNumber == compareNumber

print(isArmstrongNumber(371))