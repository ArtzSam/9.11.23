def sum(lst):
    sum = 0
    for num in lst:
        if num % 3 == 0:
            sum += num
    return sum

numbers = [5, 6, 9, 12, 15]
result = sum(numbers)
print(result)