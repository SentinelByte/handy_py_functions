import csv

# Read from a .CSV file
# Print each row seperatly
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Write to a .CSV file
# Make sure to change the input U would like to write in the write.writerow() functions
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['John', '30'])
