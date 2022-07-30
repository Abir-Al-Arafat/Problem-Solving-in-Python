# You are given three integers A, B and C, which are the side lengths of a triangle in some order. Print "Yes" if this triangle is right-angled, otherwise print "No".

def rightAngled(a, b, c):
    if a < 1 or b < 1 or c < 1:
        return 'No'

    if a > 1000 or b > 1000 or c > 1000:
        return 'No'

    if a > b and a > c:
        a = a**2
        temp = b**2 + c**2
        return a == temp

    if b > a and b > c:
        b = b**2
        temp = a**2 + c**2
        return b == temp

    if c > a and c > b:
        c = c**2
        temp = a**2 + b**2
        return c == temp

    return 'No'


# print(rightAngled(10, 9, 10))

# another approach
a, b, c = list(map(int, input().split()))
a = a*a
b = b*b
c = c*c

if (a == b+c or b == c+a or c == a+b):
    print('Yes')
else:
    print('No')
