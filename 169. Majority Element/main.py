class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for x in nums:
            count[x] = count.get(x, 0) + 1
        
        majority = -1
        mostCount = -1

        keyList = list(count.keys())

        for x in keyList:
            if count[x] > mostCount:
                mostCount = count[x]
                majority = x
        
        return majority