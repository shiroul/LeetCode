# Runtime : 0ms
# Beats : 100%

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        output = 1

        for i in range(1, len(nums)):
            if  nums[i] != nums[i-1]:
                nums[output] = nums[i]
                output+=1
        return output