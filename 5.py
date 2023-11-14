def a(lst):
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            return True
    return False

nums = [1,2,3,4,5,5]
result = a(nums)
print(result)
