def a(numbers): 
    average = sum(numbers) / len(numbers) 
    for i in range(len(numbers)): 
        if numbers[i] > average: 
            numbers[i] = numbers[i] ** 2 
    return numbers 
 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
result = a(numbers) 
print(result)