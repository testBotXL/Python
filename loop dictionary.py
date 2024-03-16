student_0 = {
    "name": "Shahriar",
    "age": 23,
    "university": "JUST",
    "id" : 170120,
    }

for key, value in student_0.items(): #for k, v in student_0.items()
    print("\nkey: " + key.title())
    print("value: " + str(value))
    
for key in student_0.keys(): #default loop is key. example: for key in student:
    print("\nkey: " + key.title())