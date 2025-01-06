#10. program to find largest of 3 numbers

n1=int(input("Enter num1 : "))
n2=int(input("Enter num2 : "))
n3=int(input("Enter num3 : "))
if n1>n2 and n1>n3:
    print("largest number is: ",n1)
elif n2>n1 and n2>n3:
    print("largest number is: ",n2)
else:
    print("largest number is: ",n3)
