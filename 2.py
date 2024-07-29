import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Alice'],
    'Age': [29, 34, None, 30, 25, 29],  # Note: Charlie's Age is missing
    'Gender': ['Female', 'Male', 'Male', 'Female', 'Female', 'Female']
}

# Create DataFrame
df = pd.DataFrame(data)

# Print original DataFrame
print("Original DataFrame:")
print(df)

# Handling Missing Values
# Fill missing values in 'Age' with the mean of 'Age'
df['Age'] = df['Age'].fillna(df['Age'].mean())
print("\nDataFrame with Missing Values Filled:")
print(df)

# Removing Duplicates
# Remove duplicate rows
df_unique = df.drop_duplicates()
print("\nDataFrame with Duplicates Removed:")
print(df_unique)

# Removing Duplicates Based on Specific Columns
# Remove duplicates based on the 'Name' column
df_unique_name = df.drop_duplicates(subset=['Name'])
print("\nDataFrame with Duplicates Removed Based on 'Name':")
print(df_unique_name)
