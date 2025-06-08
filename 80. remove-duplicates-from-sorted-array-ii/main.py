#runtime: 77 ms
#beats: 91%

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        max = False

        for x in range(1, len(nums)):
            if nums[x] == nums[k]:
                if not max:
                    max = True
                    k+=1
                    nums[k] = nums[x]
                continue
            if nums[x] != nums[k]:
                k+=1
                nums[k] = nums[x]
                max = False
        
        return k+1

