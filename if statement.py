cars = ['bmw', 'Audi', 'marcedes', 'toyota']
for car in cars:
    if car == 'Bmw': #case sensitive
        print('True')
    else:
        print('False')
print("\n")        
for car in cars:
    if car.lower() == 'audi':
        print(True)
    else:
        print(False)
        
