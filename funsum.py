"""
def sum(a,b):
    sum=a+b
    return sum
a=int(input("enter a"))
b=int(input("enter b"))
s=sum(a,b)
#print(f"{a}+{b}=",s)
print(a,"+",b,"=",s)
"""

def swap(a,b):
    a=a+b
    b=a-b
    a=b-a
    return a,b
a=int(input("enter a:"))
b=int(input("enter b:"))
a,b=swap(a,b)
print("before swapping become :",a)
print("after swapping become :",b)
