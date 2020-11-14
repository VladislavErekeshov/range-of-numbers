list_of_nums = [1, 4, 5, 2, 3, 9, 8, 11, 0]
ans = []


list = sorted(list_of_nums)
ans.append(list[0])
for i in range(0, len(list)):
    if list[i] != list[i-1]+1 and i != 0:
        if list[i-1] in ans:
            ans.append(',')
            ans.append(str(list[i]))
        else:
            ans.append('-')
            ans.append(str(list[i-1]))
            ans.append(',')
            ans.append(str(list[i]))
    elif i == len(list) - 1 and len(ans) == 1:
        ans.append('-')
        ans.append(str(list[i]))
ansv = ''
for i in ans:
    ansv += str(i)
print(ansv)