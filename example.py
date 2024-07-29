import pandas as pd

# Read CSV file
df = pd.read_csv('example.csv')

# Display the first few rows
print(df.head())

# Access a specific column
ages = df['Age']

# Filter data
adults = df[df['Age'] > 18]

# Modify data - Create a new column with ages in days
df['Age_in_days'] = df['Age'] * 365

# Group by and aggregate
average_age = df.groupby('Gender')['Age'].mean()

# Save the modified DataFrame to a new CSV file
df.to_csv('modified_example.csv', index=False)
