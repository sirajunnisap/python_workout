student_name = input("Enter your Name : ")
mark_list = input("Enter your mark list : ")

list_of_marks = list(map(int,mark_list.split()))

sumof = sum(list_of_marks)
print(sumof)

num_of_sub = len(list_of_marks)
print(num_of_sub)

totalMark = num_of_sub*100
print(totalMark)

average = sumof/totalMark*100
print(average)

if average >= 90:
    print("A")
elif average >= 80:
    print("B")
elif average >= 70:
    print("C")
elif average >= 60:
    print("D")
else:
    print("F")
    
print(list_of_marks)


