#running time: 7ms
#beats: 57%

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        majority = -1
        mostCount = 0

        for x in nums:
            count[x] = count.get(x, 0) + 1
            if count[x] > mostCount:
                mostCount = count[x]
                majority = x
        
        return majority
