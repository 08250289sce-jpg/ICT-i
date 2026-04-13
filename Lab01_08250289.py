#Initializ empty lists and dictionary
students_list = [] #it store the student's name
students_dict = {} #it will store age and grade

#Tell user to input name, age, grade
name = input("Enter the student name:")
age = int(input("enter the student age:"))
grade = int(input("enter the student grade:"))

#Insert the student name into the list
students_list.append(name) 
#Store the student's age and grade in the dictionary
students_dict[name]= {"age":age, "grade":grade}#here the student name act as key and age and grade as value

#print  confirmation that the student was added
print(f"students{name} added successfully!")

#Show the current data
print("students list:", students_list)
print("studentd details:", students_dict)

#ask user which student they want to find
search_name = input("enter the name of the student to search:")
#check wether the student exists in the dictionary
if search_name in students_dict:
    print(f"Found:{search_name}, Age:{students_dict[search_name]["age"]},Grade:{students_dict[search_name]["grade"]}")
else:
    print("students not found.")

#Remove operation
remove_name = input("enter the name of the students to remove:")#ask user which student should be removed
#Verify the students existence before deleting
if remove_name in students_dict:#remove from list
    students_list.remove(remove_name)#remove from list
    del students_dict[remove_name]#remove from dictionary
    print(f"students{remove_name}removed successfully!")
else:
    print("students not found.")
#Display the updated data after deleting
print("updated students:", students_list)
print("updated students details:", students_dict)