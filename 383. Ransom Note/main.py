class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        temp = {}

        for x in magazine:
            temp[x] = temp.get(x, 0) + 1
        
        for x in ransomNote:
            if x not in temp: return False
            elif temp[x] == 0: return False
            else: temp[x]-=1
            
        return True
            