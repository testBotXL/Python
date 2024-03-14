numbers = list(range(0,10))

print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

#appending numbers in empty lists

squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

cubes = [value**3 for value in range(1,5)]
print(cubes)