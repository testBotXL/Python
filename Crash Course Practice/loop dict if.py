students = {
    'atik' : 'ipe',
    'rony' : 'physics',
    'salman' : 'che',
    'nayeem' : 'cse',
    'asif' : 'gebt',
    'sohan' : 'mgt',
}

engineering = ['cse', 'eee', 'ipe', 'pme', 'che', 'te']
for people, subject in students.items():
    print(people.title())
    
    if subject in engineering:
        print('Hey ' + people.title() + '! come to the conference room!')