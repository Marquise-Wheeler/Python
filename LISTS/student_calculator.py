# Example Program: Student Grade Calculator

# Initialize lists to store student names and their grades
student_names = ["Alice", "Bob", "Charlie", "David"]
grades = [85, 92, 78, 95]

# Display the original data
print("Original Data:")
for i in range(len(student_names)):
    print(f"{student_names[i]}: {grades[i]}")

# Calculate the average grade
average_grade = sum(grades) / len(grades)

# Display the average Grade
print("\nAverage Grade:", average_grade)

# Identify student above the average
above_average_students = [student_names[i] for i in range(len(grades)) if grades[i] > average_grade]

# Display the student above the average grade
print("\nStudents Above Average:")
for student in above_average_students:
    print(student)
