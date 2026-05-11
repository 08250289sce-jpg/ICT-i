file = open('Students.xlsx', 'w')
file.write("Name, ID\n")
file.write("Wangchen, 001\n")
file.write("Dorji, 002\n")
file.write("Phurpa, 003\n")
file.write("Pema, 004\n")
file.write("Tshering, 005\n")
file.close()
file = open('Students.xlsx', 'r')
students = file.read()
print(students)
file.close()
searchN = input("Enter a name to search: ")
found = False
with open('Students.xlsx', 'r') as file:
    for student in file:
        if searchN.lower() in student.lower():
            print(student)
            found = True
            break
if not found:
    print("Name not found in the file.")
print()