#16. sort the dictonary

my_dict= {'banana': 3, 'apple':1, 'cherry':2, 'date':4}
print("orginal list:",my_dict)
asorted_dict=dict(sorted(my_dict.items()))
print("Ascenting order:", asorted_dict)
dsorted_dict=dict(sorted(my_dict.items(),reverse=True))
print("Decenting order:", dsorted_dict)
