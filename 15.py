elem = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 1]
unique_elements = []
for element in elem:
    if elem.count(element) == 1:
        unique_elements.append(element)

print(unique_elements)
