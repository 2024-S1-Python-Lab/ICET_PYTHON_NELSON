filename1 = input ("enter Source file name ") # Input the source file name
with open(filename1, 'r') as file1: # Read all lines from the source file
    lines = file1.readlines()
filename2 = input ("enter destination file name ") # Input the destination file name
with open(filename2, 'w') as file2:
    for i in range(len(lines)): # Iterate through the lines
        if i % 2 == 0: # Copy only odd lines
            file2.write(lines[i])
print(f"\nOdd lines copied to '{filename2}'.")
print("\nContent of the source file:") # Display the content of the source file
with open(filename1, 'r') as file1:
    print(file1.read())
print("\n Content of the destination file:") # Display the content of the destination file
with open(filename2, 'r') as file2:
    print(file2.read())
