# write a function which takes two inputs and returns the greatest common divisor of those two inputs

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(2, 4))