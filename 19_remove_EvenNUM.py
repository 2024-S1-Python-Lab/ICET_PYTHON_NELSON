#19. create a list removing even numbers

list1=[1,2,3,4,5,6,7,8,9,10]
print(f"orginal list: {list1}")
list2=[x for x in list1 if x % 2 !=0]
print(f"list of odd numbers: {list2}")
