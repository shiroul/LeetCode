class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        current = 0

        while current < k:
            if nums[current] == val:
                nums[current] = nums[k-1]
                k-=1
            else:
                current+=1
        
        return k
            