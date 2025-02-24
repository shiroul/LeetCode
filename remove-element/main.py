class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        current = 0

        while current < length:
            if nums[current] == val:
                nums.pop(current)
                length-=1
                continue
            current+=1
        return len(nums)    
            