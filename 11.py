nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = [index for index, num in enumerate(nums) if num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))]

print("Исходный список:", nums)
print("Индексы простых чисел в списке:", a)