class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        length = len(nums)
        if length == 1:
            return True

        for x in range(1, length):
            if nums[x]%2 == 0 and nums[x-1]%2 == 0:
                return False
            if nums[x]%2 != 0 and nums[x-1]%2 != 0:
                return False
        return True