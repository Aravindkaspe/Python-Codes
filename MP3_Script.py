#
# Machine Problem 3
#
# Aravind Kumar Kaspe
#
# Description: This script is addition practice problems. The user is given 2
#              integers to add together. The user gives an answer and is told
#              if the answer is correct, or not. The user is then asked if they
#              want to do another problem. The number of correct and the number
#              of incorrect answers are recorded after each problem.
#

from random import *

def additionProblem(problemNum):

    #
    # Prompts the user with an addition problem with 2 random int values between
    # 1 and 100. Collects the answer from the user, and generates the correct
    # answer.
    #
    # problemNum An int value.
    #
    # Returns a tuple with 2 elements. The 1st element is the user's
    # answer(int) and the 2nd element is the correct answer (int).
    #
    
    number1 = randint(1,100)
    number2 = randint(1,100)

    print("Problem", str(problemNum)+":", number1, "+", number2, end=' =')

    user_answer = int(input(" "))
    correct_answer = number1 + number2

    answer = (user_answer, correct_answer)

    return answer

def gradeAnswer(answers, answerTally):
    
    #
    # Checks to see if the user's answer and the correct answer are the same.
    # Prints the appropriate message to the user, along with a running total
    # of how many right and wrong answers the user has accumulated in this
    # session.
    #
    # answers A tuple with 2 elements. The 1st element is the user's
    # answer (int) and the 2nd element is the correct answer (int).
    # answerTally a list with 2 elements. The 1st element is a running total
    # of how many right answers so far in this session (int),
    # and the 2nd element is a running total of how many wrong
    # answers so far in this session (int). The list is modified
    # in the function.
    #
    # There is no return value.
    #
    
    if(answers[0] == answers[1]):
        answerTally[0] += 1
        print("You are right!")

    else:
        answerTally[1] += 1
        print("Sorry, that is not correct. The correct answer is", str(answers[1])+".")
    
### Main Program ###

print("ADDITION PRACTICE PROBLEMS")
print()
print("Add the numbers together and enter your answer.")
print("I'll tell you if you are right or wrong.")
print()

problemNum = 1
addition = additionProblem(problemNum)
answerTally = [0,0]
gradeAnswer(addition, answerTally)

print()
print("So far...", answerTally[0], "right,", answerTally[1], "wrong.")
print()
decision = input("Do you want to do another problem? ('Y' or 'N') ")
print()
yes = ['y', 'Y', 'yes','Yes','YES']

while decision in yes:
    
    problemNum += 1
    addition = additionProblem(problemNum)
    gradeAnswer(addition, answerTally)

    print()
    print("So far...", answerTally[0], "right,", answerTally[1], "wrong.")
    print()
    decision = input("Do you want to do another problem? ('Y' or 'N') ")
    print()
    
    
