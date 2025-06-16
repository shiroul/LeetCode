class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for x in range(1, len(nums)):
            if nums[x] - nums[x-1] != 1:
                return nums[x-1] + 1
        return 0 if nums[0] != 0 else nums[-1] + 1