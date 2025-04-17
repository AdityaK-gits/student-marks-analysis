# Student Marks Analysis Project

import pandas as pd
import matplotlib.pyplot as plt

# Create a simple dataset using a dictionary
data = {
    'Name': ['Aditya', 'Rohan', 'Sneha', 'Kiran', 'Zoya'],
    'Math': [85, 78, 92, 70, 88],
    'Science': [90, 80, 85, 75, 95],
    'English': [88, 76, 90, 72, 84]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Display the dataset
print("Student Marks Data:")
print(df)

# Calculate average marks for each student
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)
print("\nAverage Marks:")
print(df[['Name', 'Average']])

# Find the highest and lowest average scores
highest_avg = df.loc[df['Average'].idxmax()]
lowest_avg = df.loc[df['Average'].idxmin()]

print(f"\nTop Performer: {highest_avg['Name']} with {highest_avg['Average']} average marks.")
print(f"Lowest Performer: {lowest_avg['Name']} with {lowest_avg['Average']} average marks.")

# Bar chart of average marks
plt.figure(figsize=(8,5))
plt.bar(df['Name'], df['Average'], color='skyblue')
plt.title('Average Marks of Students')
plt.xlabel('Student Name')
plt.ylabel('Average Marks')
plt.grid(axis='y')
plt.show()

# Pie chart of one student's subject-wise marks (e.g., Aditya)
aditya_marks = df[df['Name'] == 'Aditya'][['Math', 'Science', 'English']].values.flatten()
subjects = ['Math', 'Science', 'English']

plt.figure(figsize=(6,6))
plt.pie(aditya_marks, labels=subjects, autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99'])
plt.title("Aditya's Marks Distribution")
plt.show()
