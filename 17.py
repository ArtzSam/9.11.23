a = [1, 2, 3, 4, 8, 16, 32, 64, 128]
b = sum(1 for x in a if x != 0 and (x & (x - 1)) == 0)
print(b)
