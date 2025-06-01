#runtime: 0ms
#beats: 100%

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        return nums[(len(nums))//2]