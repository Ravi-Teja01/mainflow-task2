import pandas as pd
# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [29, 34, 23, 30, 25],
    'Gender': ['Female', 'Male', 'Male', 'Female', 'Female']
}
# Create DataFrame
df = pd.DataFrame(data)
# Print original DataFrame
print("Original DataFrame:")
print(df)
# Filtering Data
# Filter rows where Age is greater than 25
filtered_df = df[df['Age'] > 25]
print("\nFiltered DataFrame (Age > 25):")
print(filtered_df)
# Filter rows where Gender is 'Female' and Age is less than 30
filtered_df_combined = df[(df['Gender'] == 'Female') & (df['Age'] < 30)]
print("\nFiltered DataFrame (Gender = 'Female' and Age < 30):")
print(filtered_df_combined)
# Sorting Data
# Sort by Age in ascending order
sorted_df = df.sort_values(by='Age')
print("\nSorted DataFrame by Age (Ascending):")
print(sorted_df)
# Sort by Age in descending order
sorted_df_desc = df.sort_values(by='Age', ascending=False)
print("\nSorted DataFrame by Age (Descending):")
print(sorted_df_desc)
# Sort by multiple columns
sorted_df_multi = df.sort_values(by=['Gender', 'Age'])
print("\nSorted DataFrame by Gender and Age:")
print(sorted_df_multi)
# Grouping Data
# Group by Gender and calculate the mean age
grouped_df = df.groupby('Gender')['Age'].mean()
print("\nMean Age by Gender:")
print(grouped_df)
# Group by Gender and calculate multiple aggregations
grouped_df_multi = df.groupby('Gender').agg({
    'Age': ['mean', 'sum', 'count']  # Mean, sum, and count of Age
})
print("\nGrouped DataFrame with Multiple Aggregations by Gender:")
print(grouped_df_multi)