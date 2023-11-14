def a(nums):
    b = [number for number in nums if (number ** 0.5).is_integer()]
    return b

numbers = [1, 4, 7, 9, 16, 25, 36]
result = a(numbers)
print(result)
