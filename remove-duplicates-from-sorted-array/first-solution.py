# Runtime = 55ms
# beats = 11.66%

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)-1
        current = 0
        tail = 1

        while current < length:
            if nums[current] == nums[tail]:
                nums.pop(tail)
            else:
                current+=1
                tail += 1
            length-=1

        return len(nums)
            

