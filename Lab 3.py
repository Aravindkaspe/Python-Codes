number = int(input("Enter the number = "))

if(number % 2 == 0):
    print(number, "is an Even number.")
else:
    print(number, "is a Odd number.")

count = 0
i =1
while i < number:
    if(number%i == 0):
        count += 1
    i+=1
if(count == 1):
    print(number, "is a prime number.")
else:
    print(number, "is a composite number.")
