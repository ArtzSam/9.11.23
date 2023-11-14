def a(lst):
    count = 0
    for num in lst:
        if num % 2 == 0 or num % 5 == 0:
            count = count + 1
    return count
nums = [1,2,3,4,5,6]
result = a(nums)
print(result)