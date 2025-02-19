s = ""

dict = {')': '(', ']': '[', '}': '{'}
temp = []

for x in s:
    if x in dict:
        if not temp:
            print('false')
            exit()
        if dict[x] == temp[-1]:
            temp.pop()
            continue
        break
    temp.append(x)

print(temp)
print(len(temp) == 0)
    # if x not in dict:
    #     temp.append(x)
    #     continue
    # if temp[-1] != dict[x]:
    #     print('false')
    #     exit()
    # temp.pop()
    