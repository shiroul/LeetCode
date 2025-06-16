class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumNumber = len(nums)

        for x in range(len(nums)):
            sumNumber += (x - nums[x])
        
        return sumNumber