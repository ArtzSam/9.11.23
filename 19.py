a = [1, 2, 3, 4, 5, 6, 7, 8]
b = (sum(a) - max(a) - min(a)) / (len(a) - 2) # среднее
c = abs(max(a) - min(a) - b) # нахождение разницы

print(c)