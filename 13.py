def a(nums):
    num = list(set(nums))
    num.sort()
# сортировочка и уборка повторов
    if len(num) < 2:
        return "В списке меньше двух элементов"

    a1 = num[1]
    b1 = num[-2]
    return a1, b1

numbers = [3, 8, 1, 4, 5, 7, 9, 2, 6]
result = a(numbers)
print(result)
