class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        decrement = [0] * (len(nums)+1)

        for l, r in queries:
            decrement[l] += 1

            decrement[r+1] -= 1
        temp = 0
        for x in range(len(nums)):
            temp += decrement[x]
            if nums[x] - temp > 0:
                return False
        return True