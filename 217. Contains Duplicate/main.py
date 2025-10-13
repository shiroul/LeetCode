class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = {}

        for x in nums:
            temp[x] = temp.get(x, 0) + 1
            if temp[x] == 2:
                return True
        return False