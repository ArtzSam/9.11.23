def a(numbers): 
    spisok = [] 
    for i in range(len(numbers)): 
        if (i + 1) % 3 == 0: 
            spisok.append(numbers[i]) 
    return spisok
 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
result = a(numbers) 
print(result)