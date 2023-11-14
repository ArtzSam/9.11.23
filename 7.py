def a(lst):
    count = 0
    for i in range(1,len(lst)):
        if lst[i] > lst[i-1]:
            count += 1
    return count
nums = [1,2,3,4,5,6]
result = a(nums)
print(result)