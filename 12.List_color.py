#12.create a list of colors from comma seperated color names entered by the user
#   display the first and last colors


color=[]
n=int(input("Enter total num of colors:"))
print("enter colors")
for i in range(n):
    ch=input()
    color.append(ch)
print(f"First color is : {color[0]} \nlast color is: {color[-1]}")
