# Input from user
student_name = input("Enter your Name: ")
mark_list = input("Enter your mark list (separated by space): ")

# Converting the string input into a list of integers
list_of_marks = list(map(int, mark_list.split()))

# Calculating the sum of marks
sumof = sum(list_of_marks)

# Number of subjects
num_of_sub = len(list_of_marks)

# Total maximum marks possible (assuming each subject is out of 100)
totalMark = num_of_sub * 100

# Calculating average percentage
average_percentage = (sumof / totalMark) * 100

# Assigning grade based on the average percentage
if average_percentage >= 90:
    grade = 'A'
elif average_percentage >= 80:
    grade = 'B'
elif average_percentage >= 70:
    grade = 'C'
elif average_percentage >= 60:
    grade = 'D'
else:
    grade = 'F'

# Output
print(f"Student Name: {student_name}")
print(f"Marks List: {list_of_marks}")
print(f"Sum of Marks: {sumof}")
print(f"Average Percentage: {average_percentage:.2f}%")
print(f"Grade: {grade}")
