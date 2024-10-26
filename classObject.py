class Student:
    def __init__(self,studentRollNo,studentName,studentAge):
        self.name = studentName
        self.roll_no = studentRollNo
        self.age = studentAge

    def display_student(self):
        print(f"Roll NO : {self.roll_no} \n Name : {self.name} \n Age : {self.age}")


student_roll_no = input("Enter Roll Number : ")
student_name = input("Enter Name : ")
student_age = input("Enter Age : ")

student = Student(student_roll_no,student_name,student_age)

student.display_student()
