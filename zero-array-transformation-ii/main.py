
def minZeroArray(nums,queries):
    output=0
    for l, r, val in queries:

        if sum(nums) <= 0:
            return output
        output+=1
        for x in range(l,r+1):
            nums[x] = nums[x]-val if nums[x]-val>0 else 0

        print(nums)
    return output if sum(nums) == 0 else -1

nums = [8,6]
queries = [[0,1,2],[1,1,2],[1,1,3],[0,0,5],[0,1,4],[0,0,1],[0,1,2],[0,0,2],[1,1,3],[0,1,2],[0,0,1],[0,0,2],[0,0,3],[0,1,4],[1,1,4]]

print(minZeroArray(nums, queries))