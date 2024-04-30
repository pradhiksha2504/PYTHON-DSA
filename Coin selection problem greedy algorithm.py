n = 5550
curr = n
deno = [1, 2, 5, 10, 20, 50, 100, 200, 500]
count = 0
while curr!=0:
    for i in range(len(deno)-1, -1, -1):
        # if curr >= deno[i] and n != deno[i]:
        if curr >= deno[i]:
            # print("deno", deno[i])
            count += 1
            # print("count: ", count)
            curr -= deno[i]
            # print("n: ", curr)
            break
print(count)
