## 0ms runtime

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maximum = nums[-1]
        output = -1

        for x in range(len(nums)-1, -1, -1):
            if nums[x] > maximum:
                maximum = nums[x]
            
            output = max(output, maximum-nums[x])

        return -1 if output == 0 else output