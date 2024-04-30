a = [20, 12, 10, 15, 2]
# a = list(map(int, input().split())))
n = len(a)
for i in range(n):
    key = i
    for j in range(i+1, n):
        if a[key] > a[j]:
            key = j
    (a[key], a[i]) = (a[i], a[key])
print(a)
