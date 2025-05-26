## runtime : 20ms

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        mpp = {}

        for x in dominoes:
            temp = ''
            if x[0] < x[1]:
                temp = ','.join(map(str, x))
            else:
                temp = ','.join(map(str, x[::-1]))
            
            if temp in mpp:
                mpp[temp]+=1
            else:
                mpp[temp]=1
        
        output = 0

        for x in mpp:
            temp = mpp[x]-1
            output += (temp * (temp + 1)) // 2
        return output