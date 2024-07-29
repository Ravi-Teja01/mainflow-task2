import csv

# Data to be written to the CSV file
data = [
    ['Name', 'Age', 'Gender'],
    ['Alice', 29, 'Female'],
    ['Bob', 34, 'Male'],
    ['Charlie', 23, 'Male'],
    ['Diana', 30, 'Female'],
    ['Eve', 25, 'Female']
]

# Writing to the CSV file
with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
