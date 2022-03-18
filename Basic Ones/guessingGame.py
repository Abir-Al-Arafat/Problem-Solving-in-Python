# Write a program to play the following game. The program should randomly generate 10 addition problems with three numbers ranging from 20 to 50 (for example 23+50+37). For each problem, the user guesses the answer. If they get the answer exactly right, print “Right!” If their answer is within 5 of the correct answer, print “Close!” Otherwise, print “Wrong.”

# importing randint function from random module to generate random numbers
from random import randint

for i in range(10):  # for loop to generate 10 problems
    p1, p2, p3 = randint(20, 50), randint(20, 50), randint(
        20, 50)  # keeping the problems in three different variables
    print(p1, "+", p2, "+", p3, "= ?")  # printing the problems
    guess = eval(input("Guess the answer: "))  # letting th user guess

    if guess == p1+p2+p3:  # checking if the guess is right
        print("right")

    elif abs(guess-(p1+p2+p3)) <= 5:  # checking if the guess is close
        print("close")

    else:
        print("wrong")
