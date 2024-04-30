a = [[3, 4], [0, 6], [1, 2], [5, 7], [8, 9], [5, 9]]
a = sorted(a, key=lambda x: x[1])
print(a)
count = 1
completed = [a[0]]
finish = a[0][1]
for i in range(1, len(a)):
    if a[i][0] > finish and a[i] not in completed:
        completed.append(a[i])
        count += 1
        finish = a[i][1]
print(completed)
print(count)
