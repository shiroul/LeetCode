class Solution:
    def check(self, nums: List[int]) -> bool:
        found = 0
        for x in range(1, len(nums)):
            nums.append(nums[x-1])
            if nums[x-1] > nums[x]:
                found = x
                break
        if found == 0 : return True

        for x in range(found+1, len(nums)):
            if nums[x] < nums[x-1]:
                return False
        return True
