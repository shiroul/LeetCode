#run time 6 ms

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        count = {}

        for a, b in dominoes:
            if a > b:
                key = (a,b)
            else:
                key = (b,a)
            count[key] = count.get(key,0) + 1
        
        output = 0
        for x in count:
            temp = count[x]-1
            output += (temp * (temp + 1)) // 2
        return output