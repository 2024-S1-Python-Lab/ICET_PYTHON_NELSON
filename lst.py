
"""
#2. List comprehention

#A. generate a positive list num from a given list
#of integers using list comprehention

lst=[2,4,6,-2,-8,7,10]
lst2=[]
for i in lst:
    if i>0:
        lst2.append(i)
print(f"positive list={lst2}")
"""
"""
#B. square of n numbers
lst1=[1,2,3,4,5,6]
lst2=[i**2 for i in lst1]
print(lst2)
"""
"""
#C. from a list of vowels selected from a givrn word

word=input("enter a word:")
vowel=[i for i in word if i in "a,e,i,o,u,A,E,I,O,U"]
print(f"vowels are {vowel}")
"""
"""
#2.d list orginal value of each element of a word

w=input("Enter any character:")
orginal_val=[ord(i) for i in w]
print(orginal_val)
"""
"""
#3.
s= input ("Enter a sentance:");
print(s)
wordslist=s.split()
print(wordslist)
for i in wordslist:
    print(f"{i} occurs {wordslist.count(i)} times")
"""
"""
#4.
n = int(input("Total number of integer:"))
list1=[]
for i in range (n):
    a=int(input("Enter an integer:"))
    if a<100:
        list1.append (a)
    else:
        list1.append("over")
        print(list1)
"""
"""
#5
name=['nelson','saud','niyas','anal']
for i in name:
    print(" 'a' occur in ",i,"-",i.count('a'),"times")
"""
"""
#6. enter 2 integers.chech:

list1=[8,6,7,4,5]
list2=[5,4,3,2,1]

#a.check if the lists have the same length
if len(list1)==len(list2):
    print("a. the list have same length.")
else:
    print("a. the list have different lengths.")

#b.Chech if the list have the same sum

print(f"b.sum of list 1: {sum(list1)} & sum of list2: {sum(list2)}")
if sum(list1)==sum(list2):
    print("The list sum to the same value.")
else:
    print("The lists do not sum to the same value.")
    
#c. check if there are any common values in both lists

common_values=set(list1)&set(list2)
if common_values:
    print(f"c.common values in both lists: {common_values}")
else:
    print("c. there are no common values in both lists.")
"""
"""
#7

s=input("enter a word:")
c=s[0]
str1=s.replace(s[0],'$')
c+str1[1:]
"""
"""
#8

str1=input("enter a string:")
print(str1[-1]+str1[1:-1]+str1[0])
"""
"""
#9. accept the radius from the user and find the are of circle

r = int(input("Enter a radius: "))
area=3.14*r**2
print("Area of a circle=",area)
"""
"""
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
"""
"""
#11.accept the file name from the user and print an extention of that

filename = input("Enter the filename:")
extension=filename.split(".")
print("The extension of the file is:", extension[-1])
"""
"""
#12.create a list of colors from comma seperated color names entered by the user
#   display the first and last colors

color=[]
n=int(input("Enter total num of colors:"))
print("enter colors")
for i in range(n):
    ch=input()
    color.append(ch)
print(f"First color is : {color[0]} \nlast color is: {color[-1]}")
"""
"""
#13. Accept an integer n and compute n+nn+nnn

n=int(input("Enter an integer n: "))
nn = n * 11
nnn = n * 111
s=n+nn+nnn
print(f"(n)+(nn)+(nnn)={s}")
"""
"""
#14. print out all colors from color list1 not contained in color list2

list1=set(['red','blue','black','green'])
list2=set(['green','red','brown','pink'])
print(list1.difference(list2))
"""
"""
#15. create a single string

s1=input("Enter first string: ")
s2=input("Enter second string: ")
print(s2[0]+s1[1:],"",s1[0]+s2[1:])
"""
"""
#16. sort the dictonary

my_dict= {'banana': 3, 'apple':1, 'cherry':2, 'date':4}
print("orginal list:",my_dict)
asorted_dict=dict(sorted(my_dict.items()))
print("Ascenting order:", asorted_dict)
dsorted_dict=dict(sorted(my_dict.items(),reverse=True))
print("Decenting order:", dsorted_dict)
"""
"""
#17. merge 2 dict
dict1={"name": "alice","age":25}
dict2={"name":"ammu","occupation":"se","hobbies":["reading","writing","coding"]}
dict1.update(dict2)
print(dict1)
"""
"""
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
"""
"""
#19. create a list removing even numbers

list1=[1,2,3,4,5,6,7,8,9,10]
print(f"orginal list: {list1}")
list2=[x for x in list1 if x % 2 !=0]
print(f"list of odd numbers: {list2}")
"""






