# Write a program that generates a list of 10 random multiplication problems, which are strings of a form like 2 x 9 or 10x 7, where the two numbers can range from 2 to 12. At the same time, generate a list of answers to those problems. Then loop through the list, asking the user to enter answers to the problems. Print out whether each answer is right or wrong, and at the end print out how many the user got correct.

from random import randint

problems = []
answers = []

for problem in range(10):
    x = randint(2, 12)
    y = randint(2, 12)

    problems.append(str(x) + " X " + str(y))
    answers.append(x*y)

count = 0

# print(problems)
# print(answers)

for index in range(len(problems)):
    print("What is the answer of", problems[index], "?")

    guess = int(input("Your answer: "))

    if(guess == answers[index]):
        print("right")
        count += 1
    else:
        print("wrong")

print("Total right answers are", count)
