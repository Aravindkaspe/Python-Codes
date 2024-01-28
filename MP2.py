#
# Machine Problem 2
#
# Aravind Kumar kaspe
#
# Description: This script fills 100 randomly generated numbers between 1 and 1000
#              into a list. Outputs the content in the list into a 10 * 10 block
#              and prints out the highest number, the lowest number and the
#              average(upto 2 decimal point) of the 100 numbers. Finally,
#              the program iterates the same task for 3 times.
#
from random import *

random_numbers_list = []

for iteration in range (3):
    for i in range(100):
        random_number = randint(1,1000)
        random_numbers_list.append(random_number)
    for j in range(10):
        for k in range(10):
            print(f'{random_numbers_list[k + (10 * j)] :> 5}', end='')
        print()
    print()
    
    max_number = max(random_numbers_list)
    min_number = min(random_numbers_list)
    avg_number = round(sum(random_numbers_list)/len(random_numbers_list),2)

    print(f'High: {max_number}, Low: {min_number}, Average:{avg_number}')
    print()
    print()
 
