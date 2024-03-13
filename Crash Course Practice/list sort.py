dept = ['cse', 'eee', 'ipe', 'pme', 'bme', 'che', 'te', 'appe']
dept.sort() #to sort in alphabetic order, permanently until changing

print(dept)

dept.sort(reverse=True) #sort in reverse order
print(dept)

dept_bba = ['ais', 'mkt', 'mgt', 'fb']

print(sorted(dept_bba)) #sort temporarily

print(dept_bba) #back to original

dept_bba.reverse()
print(dept_bba)

print(len(dept))