from random import *

def add(number1, number2):
    sum = number1
    for i in range(number2):
        sum = sum + 1
    return sum

def multiply(number1, number2):
    total = 0
    for i in range(number2):
        total = add(total,number1)
    return total

def exponent(base, exponent):
    answer = 1
    for i in range(exponent):
        answer = multiply(answer, base)
    return answer

number1 = int(input("Enter a number : "))
number2 = randint(1,5)

answer = exponent(number1, number2)

print("Your input was", number1, "and", number1, "to the power of", number2, "is", answer)


    

