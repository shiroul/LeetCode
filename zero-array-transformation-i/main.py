def isZeroArray(nums, queries):
    temp = [0] * (len(nums)+1)

    for l, r in queries:
        temp[l] += 1

        temp[r+1] -= 1
    
    print(temp)
    y = 0
    for x in range(len(nums)):
        y += temp[x]
        if nums[x] - y > 0:
            return False
    return True

num = [0,10]
q = [[0,0],[0,1],[1,1],[0,1],[1,1],[1,1],[1,1],[1,1],[0,1],[0,1],[0,1],[0,1],[1,1],[0,1],[1,1]]


print(isZeroArray(num, q))