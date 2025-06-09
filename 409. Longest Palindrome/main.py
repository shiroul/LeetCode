class Solution:
    def longestPalindrome(self, s: str) -> int:
        temp = {}
        output = 0

        for x in s:
            temp[x] = temp.get(x, 0) + 1

        for x in temp:
            if temp[x] % 2 == 0:
                output+=temp[x]
            else:
                output+=(temp[x] -1)
        
        return output+1 if output < len(s) else output