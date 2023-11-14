a = [33, 45, 20, 42, 76, 87]
n = len(a)

for i in range(n):
    peregryppirovka = False
    for j in range(0, n-i-1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            peregryppirovka = True
    if not peregryppirovka:
        break

print(a)