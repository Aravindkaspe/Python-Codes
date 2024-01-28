from ArrayStack import *
from Empty import *

def arithmetic_expression(expression_list):
    s = ArrayStack()
    operator = ['+','-','*','/']
    
    for i in expression_list:
        
        if i in operator:
            a = s.pop()
            b = s.pop()
            s.push(eval(str(b) + i + str(a)))

        else:
            s.push(int(i))

    return s.top()
            


expression = input("Enter the expression : ")
expression_list = expression.split()
d = arithmetic_expression(expression_list)

print('Expression: {} = {}'.format(expression,d))

