#find unique element
numbers = [1, 2, 1, 5, 6, 10]
unique = []

for element in numbers:
    if element not in unique:
        unique.append(element)

print(unique)
