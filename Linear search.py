def linear(arr, x):
    for i in arr:
        if i == x:
            return arr.index(i)
    return -1


a = list(map(int, input().split()))
k = int(input())
res = linear(a, k)
if res == -1:
    print("Element Not Found")
else:
    print("Element found at index: ", res)
