import csv
filename1 = input("Enter the csv file name: ")
with open(filename1,'r')as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)
