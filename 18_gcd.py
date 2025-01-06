#18. find gcd of 2 num

num1=int(input("Enter the first num1: "))
num2=int(input("Enter the first num2: "))
if num1<num2:
    min=num1
else:
    min=num2
gcd=1
for i in range(1,min+1):
    if num1%i ==0 and num2%i==0:
        gcd=i
print(f"The gcd od {num1} and {num2} is {gcd}")
