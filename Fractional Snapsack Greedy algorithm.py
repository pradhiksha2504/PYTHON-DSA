# arr = [profit, weight]
# arr = [[100, 20], [60, 10], [120, 30]]
arr = [[10, 2], [5, 3], [15, 5], [7, 7], [6, 1], [18, 4], [3, 1]]
w = 15
arr = sorted(arr, key=lambda x: x[0] / x[1], reverse=True)
# print(arr)
profit = arr[0][0]
# print(profit)
curr = w - arr[0][1]
count = 1
completed = []
for i in range(1, len(arr)):
    # print("curr: ", curr)
    # print("profit: ", profit)
    # print("currprofit: ", arr[i][0])
    if curr != 0 and arr[i] not in completed:
        if arr[i][1] < curr:
            curr -= arr[i][1]
            count+=1
            profit += arr[i][0]
        else:
            # print("a", arr[i])
            profit += (curr * (arr[i][0]/arr[i][1]))
            curr -= curr
        completed.append(arr[i])
# print(count)
print(profit)
print(completed)
