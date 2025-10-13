class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0

        for x in nums:
            if gas < 0:
                return False
            if x > gas:
                gas = x
            gas-=1
        return True