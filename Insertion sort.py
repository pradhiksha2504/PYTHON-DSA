a = list(map(int, input().split()))
'''n = len(arr)
for j in range(n):
    for i in range(1, n):
        key = i
        if a[key] < a[i - 1]:
            (a[key], a[i-1]) = (a[i-1], a[key])
print(a)'''
left = 0
right= len(a)-1
"""for i in range (left + 1, right + 1):
    j = i
    while j > left and arr[j] < arr[j - 1]:
        arr[j], arr[j - 1] = arr[j - 1], arr[j]
        j -= 1"""
for j in range (left, right + 1):
    for i in range (1, right + 1):
        key = i
        if a[key] < a[i - 1]:
            (a[key], a[i - 1]) = (a[i - 1], a[key])
print(a)