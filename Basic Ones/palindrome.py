# write a function which returns if a number is a palindrome or not

# declaring the function
def isPalindrome(number):
    original = number  # keeping the number in another variable
    reverse = 0  # declaring a variable to keep the reversed value
    while number > 0:  # while loop runs until the number is zero
        reverse = reverse * 10 + number % 10  # adding the last value
        number = number//10  # dividing the number by 10 to get the second last value
    return original == reverse  # returning a boolean value


print(isPalindrome(52525))
