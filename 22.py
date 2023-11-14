def a(numbers): 
    average = sum(numbers) / len(numbers) 
    count = 0 
    for num in numbers: 
        if num < average: 
            count += 1 
    return count 
 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
result = a(numbers) 
print(result)