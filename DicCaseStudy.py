def display_choices():
     print("1.Enter N number of students")
     print("2.Add a new student")
     print("3.Remove a student of Roll No")
     print("4.Display the grade cards of all student")
     print("5.Display the grade of a particular student")
     print("6.Exit")

display_choices()

def grade_calculate():
    roll_no = input("Roll No : ")
    name = input("Student Name : ")
    marks = [int(x) for x in input("Ënter marks for Physics , Maths & Computer Science : ").split()]
    avg = sum(marks)/3
    if avg >= 90:
        grade = 'A'
    elif avg >= 80:
        grade = 'B'
    elif avg >= 70:
        grade = 'C'
    elif avg >= 60:
        grade = 'D'  
    elif avg >= 50:      
        grade = 'E'
    else:
        grade = 'F'   

    student_dict[roll_no] = {'name':name,'marks':marks,'grade':grade}

def add_n_students(no):
    for _ in range(no):
        grade_calculate()


def add_student():
    grade_calculate()

def remove_student(roll_no):
    student_dict.pop(roll_no)

def display_grades():
    print("Student Grade Card")
    for key,value in student_dict.items():
        print(key,value)

def display_grade(roll_no):
    if roll_no in student_dict.keys():
        print(student_dict[roll_no])
    

student_dict = {}
while True:
    choice = int(input("\n Enter your choice : "))
    if choice == 1:
        no = int(input("Enter the number of students : "))
        add_n_students(no)
    elif choice == 2:
        add_student()
    elif choice == 3:
        roll_no = input("Ënter the roll no of the student to be removed : ")
        remove_student(roll_no)    
    elif choice == 4:
        display_grades()
    elif choice == 5:
        roll_no = input("Ënter the roll no of the student : ")
        display_grade(roll_no)    
    elif choice == 6:
        break    
    else:
        print("sorry , invalid choice")

print("program ended")        