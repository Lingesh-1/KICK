#Addition 
def add():
    print("The addition value of",a,"and",b,"=",a+b)
#Subraction
def sub():
    if a>b:
        print("THE subraction of",a,"and",b,"=",a-b)
    else:
        print("enter valid numbers")
#Division
def div():
    print("Division of",a,"and",b,"=",a/b)
#Floor Division
def floor():
    print("Floor Divisoin of",a,"and",b,"=",a//b)
#Multiplication
def mul():
    print("Multiplication of",a,"and",b,"=",a*b)
#Power/Expotential
def exp():
    s=input("For doing this operation which variable should be in power: ")
    if s == "A" or"a":
        print(a,"to the power",b,"=",a**b)
    elif s== "B" or "b":
        print(b,"to the power",a,"=",b**a)

    

a = int(input("Enter value of A: "))
b = int(input("Enter Value of B: "))
print("Operation SL.no\n1.Addition\n2.Subraction\n3.Division\n4.Floor division\n5.Multiplication\n6.exponetiation")
l = int(input("Enter the Operation Num: "))
if l ==1:
    add()
elif l == 2:
    sub()
elif l==3:
    div()
elif l==4:
    floor()
elif l ==5:
    mul()
elif l==6:
    exp()
else:
    print("Enter Valid SL.no")
