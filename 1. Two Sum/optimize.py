class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}

        for x in range(len(nums)):
            if nums[x] in temp:return [temp[nums[x]], x]

            temp[target-nums[x]] = x
