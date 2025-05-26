class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        output = []
        for x in nums:
            output.append(nums[x])
        return output