#Runtime : 34 ms
#Beats : 86.80% 

class Solution:
    def possibleStringCount(self, word: str) -> int:
        prev = word[0]

        output = 1

        for x in range(1, len(word)):
            if word[x] == prev:
                output+=1
            else:
                prev = word[x]
        
        return output