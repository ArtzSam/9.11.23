a = [1, 2, -3, 4, -5, 6, -7, 8, -31, 43]
b = [x for x in a if x > 0]
average = sum(b) / len(b) if b else 0
print(average)
