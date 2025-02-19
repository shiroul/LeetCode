class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        output = 0

        for i, num in enumerate(nums):
            output = target - num

            if output in temp:
                return [temp[output] , i]

            temp[num] = i