def isPrime(number, y=2):
    if(number == y):
        return True
    elif(number%y==0):
        return False
    return isPrime(number,y+1)

def facto(number, y=2):
    if isPrime(number):
        print(number)
        return
    else:
        if number%y == 0:
            print(y)
            facto(number//y,y)
        else:
            facto(number,y+1)

a = int(input("Enter a number : "))
facto(a)
