class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits)-1

        while index >= 0:
            digits[index] +=1
            if digits[index] == 10:
                digits[index] = 0
            else:
                break
            index-=1
        
        if digits[0] == 0:
            digits[0] = 0
            digits.insert(0,1)
        
        return digits