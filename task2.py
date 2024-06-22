import pandas as pd

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('2.csv')

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Filter data: Select only rows where Age is greater than 30
filtered_df = df[df['Age'] > 30]
print("\nFiltered DataFrame (Age > 30):")
print(filtered_df)

# Handle missing values: Fill missing Salary with the mean Salary
mean_salary = df['Salary'].mean()
df['Salary'].fillna(mean_salary, inplace=True)
print("\nDataFrame after filling missing Salary with mean value:")
print(df)

# Handle missing values: Drop rows with any missing values
cleaned_df = df.dropna()
print("\nDataFrame after dropping rows with any missing values:")
print(cleaned_df)

# Calculate summary statistics for the 'Age' and 'Salary' columns
summary_statistics = df[['Age', 'Salary']].describe()
print("\nSummary Statistics for 'Age' and 'Salary':")
print(summary_statistics)

# Additional summary statistics: Mean, Median, and Standard Deviation
mean_age = df['Age'].mean()
median_age = df['Age'].median()
std_age = df['Age'].std()

mean_salary = df['Salary'].mean()
median_salary = df['Salary'].median()
std_salary = df['Salary'].std()

print(f"\nAdditional Summary Statistics:")
print(f"Mean Age: {mean_age}")
print(f"Median Age: {median_age}")
print(f"Standard Deviation of Age: {std_age}")
print(f"Mean Salary: {mean_salary}")
print(f"Median Salary: {median_salary}")
print(f"Standard Deviation of Salary: {std_salary}")
