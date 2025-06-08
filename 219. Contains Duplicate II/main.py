class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        temp = {}

        for x in range(1, len(nums)+1):
            if nums[x-1] not in temp:
                temp[nums[x-1]] = x
            elif abs(temp[nums[x-1]] - x) <= k:
                return True
            else:
                temp[nums[x-1]] = x
        return False