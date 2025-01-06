#5. Display the given pyramid with step number accepted from user.

#Eg: N=4
#1
#2 4
#3 6 9
#4 8 12 16

def disp_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(i * j, end=" ")
            print()
n = int(input("Enter the number of steps: "))
if n < 1:
    print("Please enter a positive integer.")
else:
    disp_pyramid(n)
