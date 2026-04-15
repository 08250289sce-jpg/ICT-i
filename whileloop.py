no_of_students = int(input("Enter the number of students:"))
i = 1
student_names={}
while i <= no_of_students:
    name = input("Enter the name of sudents:")
    print("The name of student{} is {}". format(i, name))
    i +=1
    student_names[i] = name

print(student_names)

while True:
    print("This is an infinite loop. presS Ctrl + c to stop it.")