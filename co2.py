"""
#program to find factorial of a num

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
num = int(input("Enter a num:"))
if num<0:
    print("factorial is not defined for negative num.")
elif num == 0:
    print(f"{num}!=1")
else:
    fact = factorial(num)
    print(f"{num} != {fact}")
"""


#generate fibonacci series of N terms

def fib(n):
    f1=0
    f2=1
    print(f1)
    print(f2)
    for i in range(3,n+1):
        f3=f1+f2
        print(f3)
        f1=f2
        f2=f3
num=int(input("enter the limit: "))
fib(num)
