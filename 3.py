def a(lst):
    b = sum(lst) / len(lst)
    count = 0
    for num in lst:
        if num > b:
            count += 1
    return count

numbers = [5, 100, 222, 300, 444]
result = a(numbers)
print(result)