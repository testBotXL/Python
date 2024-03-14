ages = []
for age in range(1,21):
    ages.append(age)
    
for age in ages:
    if age >=15 and age <=20:
        print("Admit")
    else:
        print("Don't")
        
for age in ages:
    if (age <=10) or (age >=18): #if statement can also use 'in'
        print("Not Teenager")
    else:
        print("Teenager")
