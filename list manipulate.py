elements = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F']
print(elements)

elements.append('Ne')
print(elements)

neutral_elements = []

#neutral_elements.append('He')
neutral_elements.append('Ne')
neutral_elements.append('Ar')
neutral_elements.append('Kr')

print(neutral_elements)

neutral_elements.insert(0, 'He')
print(neutral_elements)

del elements[9]
del elements[8]
del elements[7]

print(elements)

#del clears the memory allocated, to get the data back, use pop() #usually the last item
elements.pop(0)
print(elements)
print(elements.pop()) #returns which one was got popped last

#remove items from the list by value
elements.remove('Li')
print(elements)

e_pollution = 'C'
elements.remove(e_pollution)
print(elements)
print("\nA " + e_pollution + " is removed from the list.")