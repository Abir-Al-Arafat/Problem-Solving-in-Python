# write a function which takes a number as an input and returns the fibonacci value of the number using recursion

def fibonacciNumber(number):
    if number <= 1:
        return number

    return fibonacciNumber(number-1) + fibonacciNumber(number-2)

print(fibonacciNumber(10))