a = float(input("Enter the value of a : "))
b = float(input("Enter the value of b : "))
c = ((a**2)+(b**2))**0.5
print("The value of c is",c,"\n")

d = float(input("Enter the value to calculate its 2nd,3rd and 4th powers : "))
d_sqr = d**2
d_cub = d**3
d_four = d**4
print("The value of number in 2nd power=",round(d_sqr,2),"3rd power=",round(d_cub,2),"and 4th power=",round(d_four,2), "\n")

e = int(input("Enter the number to check if it is even : "))
f = bool(e%2 == 0)
print(f)
