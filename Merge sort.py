"""def mergesort(arr, beg, end):
    if beg <= end:
        return
    mid = (beg + end) // 2
    mergesort(arr, beg, mid)
    mergesort(arr, mid + 1, end)
    mergesort(arr, beg, end)


def merge(a, beg, mid, end):
    left = a[beg:mid+1]
    right = a[mid+1:end+1]
    left_beg = 0
    right_beg = 0
    sorted_ind = beg"""


def mergesort(ar):
    if len(ar) > 1:
        mid = len(ar)//2
        lar = ar[:mid]
        rar = ar[mid:]
        mergesort(lar)
        mergesort(rar)
        i = 0
        j = 0
        k = 0
        while i < len(lar) and j < len(rar):
            if lar[i] < rar[j]:
                ar[k] = lar[i]
                k += 1
                i += 1
            else:
                ar[k] = rar[j]
                j += 1
                k += 1
        while i<len(lar):
            ar[k] = lar[i]
            k += 1
            i += 1
        while j < len(rar):
            ar[k] = rar[j]
            k += 1

