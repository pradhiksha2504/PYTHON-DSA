min_run = 32


def minrunc(n):
    r = 0
    while n >= min_run:
        n >>= 1
        return n + r


def insertion(arr, left, right):
    for j in range(left, right + 1):
        for i in range(1, right + 1):
            key = i
            if arr[key] < arr[i - 1]:
                (arr[key], arr[i - 1]) = (arr[i - 1], arr[key])


def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])
    i, j, k = 0, 0, l
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1
    #print("Merge: ", arr)


def timsort(arr):
    n = len(arr)
    minrun = minrunc(n)
    for st in range(0, n, minrun):
        end = min(st + minrun - 1, n - 1)
        insertion(arr, st, end)
    size = minrun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right)
        size = 2 * size


a = [57, 23, 91, 12, 68, 35, 42, 79, 18, 63, 87, 50, 29, 96, 10, 71, 84, 31, 52, 16, 77,
     95, 40, 55, 27, 81, 37, 46, 75, 21, 93, 14, 69, 82, 48, 65, 25, 73, 90, 81]
timsort(a)
print(a)
