def a(lst):
    if len(lst) < 3:
        return 0
    return sum(lst[1:-1])


numbers = [1, 2, 3, 4, 5]
result = a(numbers)
print(result)