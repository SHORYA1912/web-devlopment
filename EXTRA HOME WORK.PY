import pandas as pd

# Question 1: Student Data Table
student_data = pd.DataFrame({
    'Student Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [20, 21, 19, 22, 20],
    'Marks': [32, 70, 85, 80, 90]
})
print('Question 1: Student Data Table')
print(student_data, end='\n\n')

# Question 2: Display Specific Columns
print('Question 2: Display Specific Columns')
print('Student Names:')
print(student_data['Student Name'], end='\n\n')
print('Marks:')
print(student_data['Marks'], end='\n\n')

# Question 3: Find Average Marks
marks_df = pd.DataFrame({'Marks': student_data['Marks']})
print('Question 3: Find Average Marks')
print('Average marks:', marks_df['Marks'].mean())
print('Highest marks:', marks_df['Marks'].max())
print('Lowest marks:', marks_df['Marks'].min(), end='\n\n')

# Question 4: Add New Column
student_data['Grade'] = student_data['Marks'].apply(
    lambda m: 'A' if m >= 90 else 'B' if m >= 80 else 'C' if m >= 70 else 'D' if m >= 50 else 'F'
)
print('Question 4: Add New Column')
print(student_data, end='\n\n')

# Question 5: Filter Data
filtered = student_data[student_data['Marks'] > 80]
print('Question 5: Filter Data (Marks > 80)')
print(filtered, end='\n\n')

# Question 6: CSV File Handling
csv_path = 'student_data.csv'
student_data.to_csv(csv_path, index=False)
read_csv = pd.read_csv(csv_path)
print('Question 6: CSV File Handling')
print(read_csv.head(), end='\n\n')

# Question 7: Missing Values
missing_df = pd.DataFrame({
    'Student Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Maths': [90, None, 78, 85, None],
    'English': [88, 76, None, 82, 94]
})
print('Question 7: Missing Values')
print('Missing values:')
print(missing_df.isnull(), end='\n\n')
missing_replaced = missing_df.fillna({
    'Maths': missing_df['Maths'].mean(),
    'English': missing_df['English'].mean()
})
print('Missing values replaced:')
print(missing_replaced, end='\n\n')

# Question 8: Sort Data
print('Question 8: Sort Data')
print('Ascending by marks:')
print(student_data.sort_values(by='Marks')[['Student Name', 'Age', 'Marks', 'Grade']], end='\n\n')
print('Descending by marks:')
print(student_data.sort_values(by='Marks', ascending=False)[['Student Name', 'Age', 'Marks', 'Grade']], end='\n\n')

# Question 9: Student Attendance System
attendance = pd.DataFrame({
    'Student Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Attendance Percentage': [92, 68, 80, 74, 88]
})
print('Question 9: Student Attendance System')
print(attendance, end='\n\n')
print('Students below 75% attendance:')
print(attendance[attendance['Attendance Percentage'] < 75], end='\n\n')

# Question 10: Mini Project – School Report Analyzer
report = pd.DataFrame({
    'Student Name': student_data['Student Name'],
    'Marks': student_data['Marks']
})
average = report['Marks'].mean()
topper = report.loc[report['Marks'].idxmax()]
print('Question 10: Mini Project – School Report Analyzer')
print(report, end='\n\n')
print('Average marks:', average)
print('Topper:', topper['Student Name'], 'with', topper['Marks'], 'marks')

