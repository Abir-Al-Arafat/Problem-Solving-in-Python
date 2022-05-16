# write a function which takes a number and returns the trailing zeroes of the factorial of that number

def trailingZeroes(number):
    multiply = 5  # keeping the interval in the variable
    output = 0  # initializing the output to 0
    for n in range(5, number+1, multiply):  # running a for loop
        output += number//multiply  # adding the quotient in the output
        multiply *= multiply  # multiplying the interval with 5
    return output  # returning the output


print(trailingZeroes(30))

# number = 30
# fac = 1
# for i in range(1, number+1):
#     fac = fac*i

# print(fac)
