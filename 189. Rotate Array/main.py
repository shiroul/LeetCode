#runtime: 4ms
#beats: 60%

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        temp = nums[-k:]
        
        for x in range(len(nums)-k, 0, -1):
            nums[k+x-1] = nums[x-1]
        
        for x in range(k):
            nums[x] = temp[x]

            