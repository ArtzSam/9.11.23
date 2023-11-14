def a(lst):
    b = float('-inf')
    for i in range(len(lst) - 1):
        c = abs(lst[i] - lst[i+1])
        b = max(b, c)
    return b

spisok = [5, 10, 3, 8, 2]
max = a(spisok)
print("Наибольшая разница между соседними элементами списка:", max)