admitted_students = ['sakib', 'akib', 'rakib', 'dinar', 'minar', 'safiq'] 

new_students = ['rafiq', 'nazmul', 'akib', 'israq', 'rakib', 'dinar']

# if students: #checks if the lis is empty or not
#     for student in students:
#         print("Admit " + student + ".")
# else:
#     print("No Students")

for new_student in new_students:
    if new_student in admitted_students:
        print( "Student name " + new_student.title() + " is already taken, please choose a different name.")
    else:
        print("Admit " + new_student.title() + ".")
        
print("\nAdmission Completed!")