def a(nums):
    indx_1 = -1
    indx_2 = -1
    total = 0

    for i in range(len(nums)):
        if nums[i] < 0:
            if indx_1 == -1:
                indx_1 = i
            indx_2 = i

    if indx_1 != -1 and indx_2 != -1:
        total = sum(nums[indx_1 + 1:indx_2])

    return total

b = [3, 4, -7, 5, -3, 8, -4, 2]
result = a(b)
print("сумма элементов списка, которые находятся между первым и последним отрицательными элементами：", result)