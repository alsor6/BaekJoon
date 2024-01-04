student_list = list(range(1,31))

for i in range(28) :
    student = int(input())
    student_list.remove(student)
    
for bad_student in student_list :
    print(bad_student)