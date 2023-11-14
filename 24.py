def find(numbers): 
    def krat(a, b): 
        while b: 
            a, b = b, a % b 
        return a 
 
    def lcm(a, b): 
        return a * b // krat(a, b) 
 
    krat_result = numbers[0] 
    for i in range(1, len(numbers)): 
        krat_result = lcm(krat_result, numbers[i]) 
    return krat_result 
 
numbers = [2, 3, 4, 5] 
result = find(numbers) 
print(result)