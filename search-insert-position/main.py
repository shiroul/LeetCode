class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        temp = 0

        for x in range(len(nums)):
            if nums[x] == target:
                return x
            if nums[x] < target:
                temp+=1
        return temp