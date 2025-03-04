#Runtime 28ms
#Beats 72.44%

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        right, middle, left = [],[],[]

        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                middle.append(num)
        return left+middle+right