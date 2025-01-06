#14. print out all colors from color list1 not contained in color list2

list1=set(['red','blue','black','green'])
list2=set(['green','red','brown','pink'])
print(list1.difference(list2))
