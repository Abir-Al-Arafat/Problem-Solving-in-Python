# calculate the gcd(greatest common divisor) of two numbers

def gcd(number1, number2):
    smallest = min(number1, number2)
    gcd = 0

    for num in range(1, smallest+1):
        if number1 % num == 0 and number2 % num == 0:
            gcd=num
    
    return gcd

print(gcd(15,45))