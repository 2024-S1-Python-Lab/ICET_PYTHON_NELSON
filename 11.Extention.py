#11.accept the file name from the user and print an extention of that

filename = input("Enter the filename:")
extension=filename.split(".")
print("The extension of the file is:", extension[-1])
