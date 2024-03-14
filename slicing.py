subjects = ['bangla', 'english', 'math', 'science', 'computer']
print(subjects[0:3])

print(subjects[:2])
print(subjects[2:])

print(subjects[-3:]) # print unknown last items from a list

for subject in subjects[:3]:
    print(subject.capitalize()) 

#[:] can copy the entire list without replacing