import pandas as pd

# Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Miami']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Basic statistics
print("\nMean age:", df['Age'].mean())
print("Maximum age:", df['Age'].max())

# Filtering
print("\nPeople in their 30s:")
print(df[df['Age'] >= 30])

# Data selection
print("\nName of the first person:", df.loc[0, 'Name'])

# Sorting
print("\nSorted by age:")
print(df.sort_values(by='Age'))

# Adding a new column
df['Salary'] = [60000, 70000, 80000, 90000, 100000]
print("\nDataFrame with a 'Salary' column:")
print(df)

# Grouping and aggregation
grouped = df.groupby('City')
print("\nAverage salary by city:")
print(grouped['Salary'].mean())

# Handling missing data
df.loc[1, 'Age'] = None
print("\nDataFrame with missing data:")
print(df)

# Drop rows with missing data
df = df.dropna()
print("\nDataFrame after dropping rows with missing data:")
print(df)