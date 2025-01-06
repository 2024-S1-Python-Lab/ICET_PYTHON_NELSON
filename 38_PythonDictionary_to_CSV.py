import csv
# Define the dictionary to be written to the CSV file
data_dict = {"Name": ["John", "Jane", "Alice", "Bob"],
             "Age": [28, 34, 25, 30],
             "City": ["New York", "Los Angeles", "Chicago", "Miami"]
}
filename = "output.csv" #Write the dictionary to a CSV file
with open(filename, mode='w', newline='') as file: # Open the file in write mode
    writer = csv.DictWriter(file, fieldnames=data_dict.keys())
    writer.writeheader() # Write the header (keys of the dictionary)
    for i in range(len(data_dict["Name"])): # Write the rows
        writer.writerow({key: data_dict[key][i] for key in data_dict})
print(f"Dictionary written to {filename}.")
with open(filename, mode='r') as file: # Read the CSV file and display the content
    csvreader = csv.reader(file)
    for row in csvreader: # Read and print each row from the CSV file
        print(row)
